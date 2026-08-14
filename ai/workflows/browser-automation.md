# Workflow — Browser automation

Prefer the **machine API** over clicking coordinates.

## Load

```
file:///Users/…/Aventura_L3_Studio/Lower_Third_Studio.html
# or
https://vfxtraining-hub.github.io/lower-third-studio-web/
```

Wait until `window.L3Studio` exists:

```js
await page.waitForFunction(() => window.L3Studio && window.L3Studio.version);
```

## Canonical script

```js
const L3 = window.L3Studio;
console.log(await L3.describeForAI());

L3.setMode("simple");
L3.setExportDefaults({
  deliver: "pngseq",
  fps: 24,
  mbSamples: 16,
  width: 1920,
  height: 1080,
  logoPlayMode: "once",
});

// Optional: refresh roster
// await L3.liveUpdateRoster();

// Optional: wizard is interactive; for headless, apply preset instead:
await L3.applyPreset("Aventura Civic Gold");

// Full roster animation export (triggers browser downloads)
const job = await L3.renderAll({ download: true });
console.log(job);
L3.downloadJobManifest(); // L3_job_manifest.json
```

## Download folder

Chrome writes to the user’s Downloads directory. Tell the agent to:

1. Watch `~/Downloads` for `L3_*_pngseq.zip` or batch ZIPs  
2. Run `scripts/unpack_l3_exports.py`  
3. Hand off to Resolve  

## Wizard (semi-auto)

Full wizard needs UI interaction (logo file pickers). API helpers:

```js
await L3.openWizard();
// drive steps with DOM if required, or stop and apply preset
await L3.closeWizard();
```

For unattended runs, **skip wizard** and use presets + `setExportDefaults`.

## Selectors (fallback only)

| Action | Selector / id |
|--------|----------------|
| Download all animations | `#btnDlBatchSimple` |
| Download one | `#btnDlOneSimple` |
| New Design | `#btnNewDesign` |
| Preset select | `#simplePresetSelect` |
| Live update | `#btnLiveUpdate` |
| Mode Simple | `#modeSimple` |

Prefer API methods over these IDs — IDs may gain aliases but API is the contract.
