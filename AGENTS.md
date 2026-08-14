# AGENTS.md — VFXtraining AI Assist · Lower Third Studio

Instructions for any coding / operator agent working in this repo.

## Product

**VFXtraining AI Assist** hosts **Lower Third Studio** — a single-file HTML broadcast graphics tool. Default brand: City of Aventura 30-year package. Output: full-frame **animated PNG sequences with alpha** for NLE overlay (Resolve first).

Public Pages URL is password-gated (client-side) for authorized preview only.

| Path | Role |
|------|------|
| `Lower_Third_Studio.html` | Canonical app (local) |
| `web/index.html` | GitHub Pages copy |
| `ai/` | AI operator package |
| `llms.txt` | Short machine summary |
| `scripts/` | Unpack + Resolve import + Fusion switcher builder |
| `fusion/` | Fusion Title: rendered L3 person switcher (+ VM) |
| `people_cityofaventura.json` | Roster snapshot |
| `logo_frames/` | Reference PNG logo sequence |

### Render & package UX + Fusion + ID person

**Studio (simple):** left panel **Render & package**
- **Render** on each person · **Render this title** · **Render all titles**
- Checkbox **both styles** (Civic + Dual)
- **Build Fusion template…** → `Build_L3_Fusion_Template.command` (unpack + install title)
- **Resolve tools…** → installs **L3 Identify Person Under Playhead**

**Resolve:** Effects → Titles → **Aventura_L3_Animated_Switcher**  
Controls: Person · Style · Vice Mayor · Opacity  
**ID person:** Workspace → Scripts → L3 Identify Person Under Playhead (matches clip/marker name under playhead → sets Person).

CLI fallback: `scripts/build_fusion_l3_switcher.py`, `scripts/id_person_under_playhead.py` · see `fusion/README.md`.

## Do this first

1. Read `ai/OPERATOR_PROMPT.md` (operator contract).
2. Read `ai/machine-api.json` if automating the browser.
3. Prefer **not** re-architecting the 4MB HTML unless fixing a bug; inject small APIs / docs instead.

## Always push / sync Pages after every change

**Standing rule (Yan):** after any meaningful edit to the studio, **always** sync and push GitHub Pages — do not wait to be asked.

```bash
# from package root
./scripts/sync_pages.sh "short commit message"
```

What it does: copies `Lower_Third_Studio.html` → `web/index.html` (plus `llms.txt`, `AGENTS.md`, `START_HERE.md`, `ai/`), commits, `git push origin main`.

Live: https://vfxtraining-hub.github.io/lower-third-studio-web/  
Password: `L3Dstudio`

## Operator loop (happy path)

```
open HTML → (optional) wizard/preset → renderAll PNG seq → unpack → Resolve import → timeline
```

Default quality: `pngseq`, 16-sample motion blur, logo play once→hold, 1920×1080 alpha.

## In-page hooks

After load, `window.L3Studio` is the stable automation surface. Do not scrape brittle CSS selectors unless the API is missing a method — then extend `L3Studio` and document it in `ai/machine-api.json`.

## Resolve

- Script: `scripts/import_l3_to_resolve.py` (Resolve Studio scripting API).
- MCP (when available): `resolve_status`, `import_media`, `create_bin`, `create_timeline` / `open_timeline`, `append_clips`.
- Details: `ai/workflows/resolve.md`.

## Editing rules

- Keep Simple mode usable for non-experts.
- Never force still-PNG as the primary export path.
- Logo sequences must not wipe the preset list (localStorage quota).
- When changing UI, update `llms.txt` + `ai/machine-api.json` if API/UX contracts change.

## Publish

```bash
cp Lower_Third_Studio.html web/index.html
# also sync ai/ + llms.txt into web/ when publishing
cd web && git add -A && git commit -m "…" && git push
```

Pages: https://vfxtraining-hub.github.io/lower-third-studio-web/

## Success report template

```
Titles rendered: N
Export folder: …
Resolve project: …
Timeline: …
Bin: …
FPS: …
Notes: …
```


## Timeline → L3 automation

- Prerequisites: `resolve-ai-ready/`
- Pipeline: `scripts/run_timeline_l3_pipeline.py`
- Skills: `resolve-ai-ready`, `timeline-lower-thirds`, `lower-third-studio`, linked `resolve-mcp` / `resolve-edit`
- Markers: `L3: Full Name` or `L3: Name | Title`
