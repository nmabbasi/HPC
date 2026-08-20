from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "_legacy" / "html"
TARGET = ROOT / ".migration"
TARGET.mkdir(exist_ok=True)

PAGES = {
    "connections": "connections.html",
    "commands": "BC.html",
    "job-scripts": "ss.html",
    "conda": "conda.html",
    "custom-modules": "CM.html",
    "support": "support.html",
    "requests": "QR.html",
}

for slug, source_name in PAGES.items():
    source = LEGACY / source_name
    soup = BeautifulSoup(source.read_text(encoding="utf-8", errors="replace"), "html.parser")
    content = soup.select_one(".page-content-card")
    if content is None:
        raise SystemExit(f"Missing .page-content-card in {source_name}")
    article = content.select_one("article.markdown-body")
    if article is not None:
        content = article
    for noisy in content.select("script, style"):
        noisy.decompose()
    html = content.decode_contents().replace("connections.html", "/docs/connections/").replace("BC.html", "/docs/commands/").replace("ss.html", "/docs/job-scripts/").replace("conda.html", "/docs/conda/").replace("CM.html", "/docs/custom-modules/").replace("support.html", "/docs/support/")
    (TARGET / f"{slug}.html").write_text(html, encoding="utf-8")
    print(f"Extracted {source_name} → {slug}.html")
