from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('assets', exist_ok=True)

# Banner
w, h = 1200, 360
img = Image.new('RGB', (w, h), (12, 16, 22))
d = ImageDraw.Draw(img)
for y in range(h):
    ratio = y / (h - 1)
    r = int(12 + (30 - 12) * ratio)
    g = int(16 + (40 - 16) * ratio)
    b = int(22 + (48 - 22) * ratio)
    d.line([(0, y), (w, y)], fill=(r, g, b))

try:
    font_large = ImageFont.truetype('arial.ttf', 62)
    font_small = ImageFont.truetype('arial.ttf', 24)
except Exception:
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

def text_size(text, font):
    bbox = d.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

text = 'Arthur Duarte'
fw, fh = text_size(text, font_large)
d.text(((w - fw) / 2, 88), text, fill=(238, 242, 248), font=font_large)
sub = 'Software Engineering Student'
fw, fh = text_size(sub, font_small)
d.text(((w - fw) / 2, 178), sub, fill=(168, 186, 212), font=font_small)
sub2 = 'Cybersecurity Enthusiast'
fw, fh = text_size(sub2, font_small)
d.text(((w - fw) / 2, 214), sub2, fill=(168, 186, 212), font=font_small)
sub3 = 'Why not you?'
fw, fh = text_size(sub3, font_small)
d.text(((w - fw) / 2, 250), sub3, fill=(255, 255, 255), font=font_small)

for x in range(100, w, 160):
    d.line([(x, 0), (x, h)], fill=(20, 30, 44), width=1)
for y in range(80, h, 80):
    d.line([(0, y), (w, y)], fill=(20, 30, 44), width=1)

img.save('assets/banner.png')

# Coffee GIF
w, h = 360, 240
frames = []
for f in range(12):
    frame = Image.new('RGBA', (w, h), (10, 14, 22, 255))
    draw = ImageDraw.Draw(frame)
    draw.rectangle([40, 130, 320, 200], fill=(22, 28, 38, 255), outline=(58, 84, 118, 255), width=2)
    draw.ellipse([70, 100, 160, 140], fill=(18, 24, 34, 255), outline=(58, 84, 118, 255))
    draw.rectangle([82, 114, 122, 176], fill=(34, 44, 62, 255))
    draw.polygon([(122, 120), (218, 120), (198, 178), (142, 178)], fill=(20, 26, 36, 255))
    draw.ellipse([144, 118, 204, 138], fill=(10, 14, 20, 255))
    alpha = Image.new('L', (w, h), 0)
    ad = ImageDraw.Draw(alpha)
    for i, x in enumerate([166, 182, 198]):
        y = 70 - ((f * 2) % 20) + i * 18
        ad.ellipse([x - 10, y - 30, x + 10, y + 8], fill=180)
    steam = Image.new('RGBA', (w, h), (255, 255, 255, 0))
    steam.putalpha(alpha)
    frame = Image.alpha_composite(frame, steam)
    frames.append(frame.convert('P', palette=Image.ADAPTIVE))
frames[0].save('assets/coffee.gif', save_all=True, append_images=frames[1:], duration=120, loop=0, disposal=2)

print('assets generated')
