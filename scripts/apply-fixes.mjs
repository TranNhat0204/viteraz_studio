import { DatabaseSync } from 'node:sqlite';

const db = new DatabaseSync('.runtime/user-data/studio.db');

console.log('--- Applying Database Triggers and Synchronizations ---');

// 1. Test json_set
const test = db.prepare(`SELECT json_set('{"config": {"voice": "old"}}', '$.config.voice', 'new_voice') as res`).get();
console.log('json_set capability test:', test.res);

// 2. Drop existing triggers if needed and create robust triggers
db.exec(`DROP TRIGGER IF EXISTS trg_sync_channel_profile_to_videos_update;`);
db.exec(`DROP TRIGGER IF EXISTS trg_sync_voice_on_tts_retry;`);
db.exec(`DROP TRIGGER IF EXISTS trg_sync_provider_on_storyboard_retry;`);

// Trigger 1: When channel_profile_json is updated in ai_schedule_configs, sync to all existing videos of that project
db.exec(`
CREATE TRIGGER trg_sync_channel_profile_to_videos_update
AFTER UPDATE OF channel_profile_json ON ai_schedule_configs
BEGIN
    UPDATE videos
    SET metadata_json = json_set(
        COALESCE(metadata_json, '{"config":{}}'),
        '$.config.voice', json_extract(NEW.channel_profile_json, '$.voice'),
        '$.config.tts_provider', json_extract(NEW.channel_profile_json, '$.tts_provider'),
        '$.config.provider', json_extract(NEW.channel_profile_json, '$.provider')
    )
    WHERE project_id = NEW.project_id;
END;
`);

// Trigger 2: When video_steps for 'tts' is set to 'pending' (e.g. user clicks "Tạo lại giọng"),
// automatically fetch latest voice and tts_provider from ai_schedule_configs for this video's project
db.exec(`
CREATE TRIGGER trg_sync_voice_on_tts_retry
AFTER UPDATE OF status ON video_steps
WHEN NEW.step_name = 'tts' AND NEW.status = 'pending'
BEGIN
    UPDATE videos
    SET metadata_json = json_set(
        COALESCE(metadata_json, '{"config":{}}'),
        '$.config.voice', (
            SELECT json_extract(channel_profile_json, '$.voice')
            FROM ai_schedule_configs
            WHERE project_id = videos.project_id
        ),
        '$.config.tts_provider', (
            SELECT json_extract(channel_profile_json, '$.tts_provider')
            FROM ai_schedule_configs
            WHERE project_id = videos.project_id
        )
    )
    WHERE id = NEW.video_id;
END;
`);

// Trigger 3: When video_steps for 'storyboard' is set to 'pending' (retry storyboard),
// sync latest provider from ai_schedule_configs for this video's project
db.exec(`
CREATE TRIGGER trg_sync_provider_on_storyboard_retry
AFTER UPDATE OF status ON video_steps
WHEN NEW.step_name = 'storyboard' AND NEW.status = 'pending'
BEGIN
    UPDATE videos
    SET metadata_json = json_set(
        COALESCE(metadata_json, '{"config":{}}'),
        '$.config.provider', (
            SELECT json_extract(channel_profile_json, '$.provider')
            FROM ai_schedule_configs
            WHERE project_id = videos.project_id
        )
    )
    WHERE id = NEW.video_id;
END;
`);

console.log('Triggers created successfully!');

// 3. Update current video 3c65a07611c84af893c2f2a6f3ae1353 metadata_json directly
const targetVideoId = '3c65a07611c84af893c2f2a6f3ae1353';
const video = db.prepare('SELECT id, project_id, metadata_json FROM videos WHERE id = ?').get(targetVideoId);
if (video) {
  const cfg = db.prepare('SELECT channel_profile_json FROM ai_schedule_configs WHERE project_id = ?').get(video.project_id);
  if (cfg) {
    const prof = JSON.parse(cfg.channel_profile_json);
    console.log('Project current profile:', {
      provider: prof.provider,
      tts_provider: prof.tts_provider,
      voice: prof.voice
    });

    const vMeta = JSON.parse(video.metadata_json || '{}');
    if (!vMeta.config) vMeta.config = {};
    vMeta.config.tts_provider = prof.tts_provider || 'vbee-tts';
    vMeta.config.voice = prof.voice || 'hn_male_minhquan_yt-stable';
    vMeta.config.provider = prof.provider || 'gemini';

    db.prepare('UPDATE videos SET metadata_json = ? WHERE id = ?').run(JSON.stringify(vMeta), targetVideoId);
    console.log('Updated video metadata_json:', vMeta);
  }
}

// 4. Update project 3ed9de3f49d54b5facbcefc4516e8f84 to use gemini as default provider (or keep chatgpt if preferred)
// Both are logged in, but Gemini has no rate limit for Vietnamese storyboard and audit
const projId = '3ed9de3f49d54b5facbcefc4516e8f84';
const currentCfg = db.prepare('SELECT channel_profile_json FROM ai_schedule_configs WHERE project_id = ?').get(projId);
if (currentCfg) {
  const p = JSON.parse(currentCfg.channel_profile_json);
  // Ensure voice is hn_male_minhquan_yt-stable
  p.voice = 'hn_male_minhquan_yt-stable';
  p.tts_provider = 'vbee-tts';
  p.provider = 'gemini';
  p.script_audit_provider = 'gemini';

  db.prepare('UPDATE ai_schedule_configs SET channel_profile_json = ? WHERE project_id = ?')
    .run(JSON.stringify(p), projId);
  console.log('Updated channel_profile_json for project:', projId);
}

// 5. Update settings translate_provider to gemini
db.prepare("UPDATE settings SET value = 'gemini' WHERE key = 'translate_provider'").run();
console.log('Updated translate_provider to gemini');

// 6. Reset failed steps for video
const resetRes = db.prepare(`
  UPDATE video_steps 
  SET status = 'pending', error_code = NULL, error_message = NULL 
  WHERE video_id = ? AND status = 'failed'
`).run(targetVideoId);
console.log('Reset failed video steps count:', resetRes.changes);

// 7. Verify final state
const steps = db.prepare('SELECT step_name, status, error_code, error_message FROM video_steps WHERE video_id = ?').all(targetVideoId);
console.log('Final video steps:');
for (const s of steps) {
  console.log(`  ${s.step_name}: ${s.status} ${s.error_code ? `(${s.error_code}: ${s.error_message})` : ''}`);
}
