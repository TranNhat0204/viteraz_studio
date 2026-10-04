import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { DatabaseSync } from 'node:sqlite';

const ffmpegPath = path.resolve('.runtime/desktop/resources/ffmpeg/ffmpeg.exe');
console.log('Testing FFmpeg at:', ffmpegPath);

const output = execFileSync(ffmpegPath, ['-help', 'full'], { encoding: 'utf8', maxBuffer: 10 * 1024 * 1024 });
const hasOption = output.includes('-filter_complex_script');
console.log('Supports -filter_complex_script:', hasOption);

// Update database settings to ensure ffmpeg_path points to this exact binary
const db = new DatabaseSync('.runtime/user-data/studio.db');
const res = db.prepare("UPDATE settings SET value = ? WHERE key = 'ffmpeg_path'").run(ffmpegPath);
console.log('Updated ffmpeg_path in studio.db:', res.changes);

// Reset the failed export step so it can be retried immediately
const resSteps = db.prepare("UPDATE video_steps SET status = 'pending', error_code = NULL, error_message = NULL WHERE step_name = 'export' AND status = 'failed'").run();
console.log('Reset failed export steps:', resSteps.changes);
