"""Take a screenshot of a project page for the index.

    python tools/shots.py basal-web https://dfgrzyska.github.io/basal-web/ desktop
    python tools/shots.py kiusiu-trip https://dfgrzyska.github.io/kiusiu-trip/ phone

Writes img/<name>.webp: 960 x 600 for desktop pages, 500 x 900 for phone apps.
Needs Microsoft Edge (or Chrome, see BROWSERS) and Pillow.
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image

BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]
# Headless Chrome won't lay out narrower than ~500 px, so phone apps are shot at 500 wide.
SIZES = {"desktop": ((1280, 800), 960), "phone": ((500, 900), 500)}
IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img")


def main(name, url, kind):
    (w, h), out_w = SIZES[kind]
    browser = next(b for b in BROWSERS if os.path.exists(b))
    with tempfile.TemporaryDirectory() as tmp:
        png = os.path.join(tmp, "shot.png")
        subprocess.run([
            browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
            f"--user-data-dir={os.path.join(tmp, 'profile')}", "--force-device-scale-factor=2",
            f"--window-size={w},{h}", "--virtual-time-budget=9000", f"--screenshot={png}", url,
        ], check=True, timeout=90, capture_output=True)
        im = Image.open(png).convert("RGB")
    out_h = round(im.height * out_w / im.width)
    path = os.path.join(IMG, f"{name}.webp")
    im.resize((out_w, out_h), Image.LANCZOS).save(path, "WEBP", quality=80, method=6)
    print(path, (out_w, out_h))


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[3] not in SIZES:
        sys.exit(__doc__)
    main(*sys.argv[1:])
