"""Inline the generated key art into site.src.html and write site.html (single file, no external images)."""
import base64, re, pathlib
here = pathlib.Path(__file__).parent
src = (here / "site.src.html").read_text()
def uri(m):
    p = here / "assets" / (m.group(1) + ".jpg")
    return "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()
out = re.sub(r"\{\{IMG:([\w-]+)\}\}", uri, src)
(here / "site.html").write_text(out)
print(len(out) // 1024, "KB")
