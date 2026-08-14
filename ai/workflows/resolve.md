# Workflow — DaVinci Resolve

End-to-end: Studio export → disk → media pool → timeline.

## Prerequisites

- DaVinci **Resolve Studio** running (scripting / MCP need Studio)
- Project open (or create one)
- Know target **timeline** name (or create `L3 Titles`)
- PNG sequences unzipped (not left as `.zip`)

## Path A — Python script (local)

```bash
# 1) Collect ZIPs from Downloads into a clean tree
python3 scripts/unpack_l3_exports.py ~/Downloads \
  --out ~/Movies/L3_Aventura_Exports \
  --pattern 'L3_*'

# 2) Import + place on timeline
python3 scripts/import_l3_to_resolve.py \
  --source ~/Movies/L3_Aventura_Exports \
  --bin L3_Aventura \
  --timeline "L3 Titles" \
  --fps 24 \
  --mode append \
  --track 2
```

### Modes

| `--mode` | Behavior |
|----------|----------|
| `import_only` | Bin only, no timeline edit |
| `append` | Create/open timeline, append each sequence in order |
| `markers` | Place at timeline markers named like person ids (if present) |

## Path B — Resolve MCP (Grok / Claude)

```
1. resolve_status
2. create_bin  name=L3_Aventura   (if missing)
3. import_media  paths=[absolute dirs or first frame of each seq]  bin_name=L3_Aventura
4. open_timeline name=<user timeline>  OR  create_timeline name="L3 Titles"
5. append_clips  clips=[{name: <pool clip name>, track: 2}, ...]
6. open_page page=edit
```

### Image sequences

Resolve may import a folder of `*_00001.png …` as one clip when “Import as image sequence” is on. The Python script sets sequence import flags when the API allows; if MCP imports stills only, re-import from Media Storage UI once with sequence enabled, or use the Python script.

## Path C — Manual (fallback)

1. Media Storage → navigate to export folder  
2. Import as image sequence @ **24 fps** (or job FPS)  
3. Bin: `L3_Aventura`  
4. Drag to **V2** on Edit page  
5. Composite: normal over picture (alpha)

## QC

- [ ] Alpha edges clean over gray and over plate  
- [ ] FPS matches timeline (no 24-on-30 drift without convert)  
- [ ] Hold is long enough to read name  
- [ ] Logo plays once then freezes (not looping unless requested)  
- [ ] 9:16 jobs only if timeline is vertical  

## Job manifest

After `L3Studio.renderAll()`, download or read `L3_job_manifest.json` — it lists each title’s `base`, frame count, and Resolve hints. Feed that into the import script:

```bash
python3 scripts/import_l3_to_resolve.py \
  --manifest ~/Downloads/L3_job_manifest.json \
  --source ~/Movies/L3_Aventura_Exports \
  --timeline "Show Open"
```
