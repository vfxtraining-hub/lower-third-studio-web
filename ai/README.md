# AI package — Lower Third Studio

This folder makes the studio **operable by any out-of-the-box AI** with a single prompt.

## Give a fresh AI this

1. Path or URL to the project / site  
2. The full contents of **[OPERATOR_PROMPT.md](./OPERATOR_PROMPT.md)**

That is enough to: run the wizard, render all titles, and push into Resolve.

## Files

| File | Purpose |
|------|---------|
| `OPERATOR_PROMPT.md` | **Paste-ready** system/operator prompt |
| `machine-api.json` | JSON schema for `window.L3Studio` |
| `workflows/resolve.md` | DaVinci Resolve import & timeline |
| `workflows/browser-automation.md` | Playwright / Chrome DevTools |
| `workflows/generic-nle.md` | AE / FCP / Premiere later |
| `../llms.txt` | One-page summary (also at site root) |
| `../AGENTS.md` | Repo map for coding agents |
| `../scripts/unpack_l3_exports.py` | Unzip Downloads → clean folder |
| `../scripts/import_l3_to_resolve.py` | Media pool + timeline |

## Discovery conventions

Agents should look for, in order:

1. `llms.txt`  
2. `AGENTS.md`  
3. `ai/OPERATOR_PROMPT.md`  
4. `ai/machine-api.json`  
5. In-page `window.L3Studio.describeForAI()`  
6. HTML meta: `name="ai-operator"` / `link rel="llms-txt"`

## Version

AI surface version: **1.0.0** (keep in sync with `L3Studio.version` in the HTML).
