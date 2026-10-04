import { DatabaseSync } from 'node:sqlite';

const dbPath = '.runtime/user-data/studio.db';
const db = new DatabaseSync(dbPath);

console.log('--- Updating Revo Studio AI Provider to Gemini ---');

// 1. Update translate_provider
const res1 = db.prepare("UPDATE settings SET value = 'gemini' WHERE key = 'translate_provider'").run();
console.log('Updated translate_provider:', res1.changes);

// 2. Update competitor_llm_provider
const res2 = db.prepare("UPDATE settings SET value = 'gemini' WHERE key = 'competitor_llm_provider'").run();
console.log('Updated competitor_llm_provider:', res2.changes);

// 3. Reset failed research step
const res3 = db.prepare("UPDATE video_steps SET status = 'pending', error_code = NULL, error_message = NULL WHERE step_name = 'research' AND status = 'failed'").run();
console.log('Reset failed video_steps:', res3.changes);

// Verify settings
const rows = db.prepare("SELECT key, value FROM settings WHERE key IN ('translate_provider', 'competitor_llm_provider', 'gemini_model')").all();
console.log('Current settings:', rows);
