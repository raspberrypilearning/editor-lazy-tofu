#!/usr/bin/env python3
"""Make labelled sprite cards from the starter's saved costumes.

Requires Pillow, rsvg-convert (for SVG costumes), and an Arial-compatible font.
Run with --font PATH when Arial is not installed at the macOS default path.
"""

import argparse
import io
import json
from pathlib import Path
import subprocess
import zipfile

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[2]
STARTER = ROOT / 'en/code/editor-lazy-tofu-starter/editor-lazy-tofu-starter.sb3'
SCALE = 4


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font', default='/System/Library/Fonts/Supplemental/Arial.ttf')
    args = parser.parse_args()
    font = ImageFont.truetype(args.font, 9 * SCALE)
    with zipfile.ZipFile(STARTER) as archive:
        project = json.loads(archive.read('project.json'))
        for target in project['targets']:
            costume = target['costumes'][target['currentCostume']]
            payload = archive.read(costume['md5ext'])
            if costume['dataFormat'] == 'svg':
                payload = subprocess.run(
                    ['rsvg-convert', '--zoom', str(SCALE)], input=payload,
                    stdout=subprocess.PIPE, check=True,
                ).stdout
            artwork = Image.open(io.BytesIO(payload)).convert('RGBA')
            bounds = artwork.getchannel('A').getbbox()
            if bounds:
                artwork = artwork.crop(bounds)
            artwork = ImageOps.contain(
                artwork, (48 * SCALE, 34 * SCALE), Image.Resampling.LANCZOS,
            )
            card = Image.new('RGBA', (80 * SCALE, 70 * SCALE))
            draw = ImageDraw.Draw(card)
            draw.rounded_rectangle(
                (SCALE, SCALE, 79 * SCALE, 69 * SCALE), radius=7 * SCALE,
                fill='#e8f1ff', outline='#b9c2cd', width=SCALE,
            )
            card.alpha_composite(
                artwork, ((card.width - artwork.width) // 2, 8 * SCALE + (34 * SCALE - artwork.height) // 2),
            )
            draw.text((40 * SCALE, 55 * SCALE), target['name'], font=font, fill='#374151', anchor='mm')
            destination = ROOT / 'en/images' / f"sprite-{target['name'].lower()}.png"
            card.resize((80, 70), Image.Resampling.LANCZOS).save(destination)
            print(destination.relative_to(ROOT))


if __name__ == '__main__':
    main()
