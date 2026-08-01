import urllib.request as u
import ssl, sys

ctx = ssl.create_default_context()
sites = {
    "mirror_stats": "https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api?username=Mazeqi&theme=github_dark",
    "original_stats": "https://github-readme-stats.vercel.app/api?username=Mazeqi&theme=github_dark",
    "typing_svg": "https://readme-typing-svg.demolab.com/?font=Fira+Code&lines=test",
    "activity_graph": "https://github-readme-activity-graph.vercel.app/graph?username=Mazeqi",
    "skillicons": "https://skillicons.dev/icons?i=python",
    "komarev": "https://komarev.com/ghpvc/?username=Mazeqi",
}
for name, url in sites.items():
    try:
        req = u.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with u.urlopen(req, timeout=20, context=ctx) as r:
            body = r.read()
            # detect if it's actually an SVG image
            head = body[:200].decode("utf-8", "ignore")
            print(f"{name}: HTTP {r.status} | {len(body)} bytes | starts_with: {head.strip()[:60]!r}")
    except Exception as e:
        print(f"{name}: FAILED -> {type(e).__name__}: {e}")