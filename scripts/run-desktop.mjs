import { spawn } from 'node:child_process';
import { mkdir } from 'node:fs/promises';
import {
  desktopExecutable,
  desktopRoot,
  inspectRuntime,
  printRuntimeReport,
  userDataDirectory,
} from './doctor.mjs';

// The Electron main process verifies backend integrity before spawning it.
// Avoid hashing the same 31 MB executable twice on every normal launch.
const report = await inspectRuntime({ verifyBackendHash: false });
if (!report.ok) {
  printRuntimeReport(report);
  process.exitCode = 1;
} else {
  await mkdir(userDataDirectory, { recursive: true });
  const environment = {
    ...process.env,
    VS_DEV: '0',
    REVO_LICENSE_ENFORCE: '0',
    REVO_HIDE_BROWSER: '1',
    FLOW_SHOW: '0',
  };
  delete environment.ELECTRON_RUN_AS_NODE;
  console.log('Starting Viteraz Studio from recovered/app.');
  console.log(`Local application data: ${userDataDirectory}`);
  const child = spawn(desktopExecutable, [`--user-data-dir=${userDataDirectory}`], {
    cwd: desktopRoot,
    env: environment,
    windowsHide: false,
    stdio: 'inherit',
  });
  child.once('error', (error) => {
    console.error(`Cannot start Revo Studio: ${error.message}`);
    process.exitCode = 1;
  });
  child.once('exit', (code, signal) => {
    if (signal) console.error(`Revo Studio exited after signal ${signal}.`);
    process.exitCode = code ?? 1;
  });
}
