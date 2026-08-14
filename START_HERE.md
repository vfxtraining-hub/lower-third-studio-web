# VFXtraining AI Assist · Lower Third Studio

**Prime-time path** (what to do every session)

## Open
- Local: `Lower_Third_Studio.html` (Chrome)
- Web: https://vfxtraining-hub.github.io/lower-third-studio-web/?v=prime  
  Password: `L3Dstudio` · use **Cmd+Shift+R** if UI looks stale

## Workflow (Simple mode)

1. **Style** — Civic Gold or Aventura Dual  
2. **People** — select a person · optional Vice Mayor  
3. **On-air text** — edit name/title if needed (or click type on stage)  
4. **Size** — open “Size & position” only if the plate feels big/small  
5. **Render this** / **Render all** — full PNG **animations** (both styles checkbox)  
6. **Fusion template…** — double-click the downloaded `.command` to unpack + install  
7. **Resolve** — Titles → **Aventura_L3_Animated_Switcher**  
8. **ID person** — Scripts → **L3 Identify Person Under Playhead** (clip/marker name match)

### Shortcuts
| Key | Action |
|-----|--------|
| `R` | Render this person |
| `⇧R` | Render all |

## What “good” looks like
- Left column: **1 Render · 2 Style · 3 People · 4 On-air** in that order  
- Top bar: **Render this · Render all · Fusion · Preview · 16:9/9:16**  
- Each person row has its own **Render** button  
- Stage chips show current style, person, aspect  

## Files that matter
| Path | Role |
|------|------|
| `Lower_Third_Studio.html` | The app |
| `scripts/build_fusion_l3_switcher.py` | Fusion title from PNG sequences |
| `scripts/id_person_under_playhead.py` | Resolve: ID speaker → set Person |
| `scripts/unpack_l3_exports.py` | Unzip L3 downloads |
| `fusion/README.md` | Fusion / Resolve details |
| `people_cityofaventura.json` | Roster |

## Advanced mode
Colors, type, logo sequences, stills, WebM — only when you need to leave the happy path.
