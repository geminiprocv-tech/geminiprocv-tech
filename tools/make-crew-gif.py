#!/usr/bin/env python3
"""
Dựng hoạt cảnh 3 mascot đi qua lại CÓ HIỆU ỨNG -> assets/crew-walk.gif

Hiệu ứng đang bật:
  · travel      — đi qua lại, dừng 1 nhịp ở mỗi đầu, tự lật mặt
  · bob         — nhấp nhô theo nhịp bước, lệch pha 3 con
  · squash      — co giãn dọc/ngang theo nhịp (nén khi chạm đất, giãn khi lên đỉnh)
  · sway        — nghiêng nhẹ qua lại
  · glow        — quầng sáng sau lưng mỗi con, đập theo nhịp
  · shadow      — bóng dưới chân, to nhỏ theo độ cao
  · dust        — hạt sáng bay lên, lặp đúng 1 chu kỳ nên không bị "nhảy"

Dùng:
    pip install pillow cairosvg
    python3 tools/make-crew-gif.py
"""
import math, os
import cairosvg
from PIL import Image, ImageDraw, ImageFilter

# ---------------- cấu hình ----------------
W, H, GROUND = 780, 180, 150
HEIGHTS  = [96, 88, 66]          # chiều cao từng con (cân theo diện tích hiển thị)
CX       = [315, 390, 470]        # tâm từng con
AMP      = 172                    # biên độ đi qua lại
N, FPS   = 32, 11                 # số frame / tốc độ
STEP_HZ  = 2.1                    # nhịp bước (bước/giây)
BOB      = 6                      # nhấp nhô (px)
SQUASH   = 0.055                  # độ co giãn (0 = tắt)
SWAY     = 2.4                    # nghiêng (độ)
GLOW_ON  = True
DUST_ON  = True
COLORS   = 48
DISPOSAL = 1
LABEL_L  = "THREE MODELS, ONE STUDENT"
LABEL_R  = "THE COMMITS ARE MINE"
CAPTION  = "THEY ARGUE &#183; I DECIDE &#183; THEN I MEASURE IT"

GLOW_RGB = [(141, 214, 255), (110, 150, 245), (255, 160, 130)]   # m1, m2, m3
PAD      = 16                     # đệm trong suốt để xoay/co giãn không bị cắt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STAGE = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="'DejaVu Sans Mono',monospace">
  <defs>
    <pattern id="g" width="22" height="22" patternUnits="userSpaceOnUse">
      <path d="M22 0H0V22" fill="none" stroke="#1e6f8f" stroke-width="0.35" opacity="0.2"/>
    </pattern>
    <linearGradient id="fx" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#8fd6ff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#8fd6ff" stop-opacity="0.42"/>
      <stop offset="1" stop-color="#8fd6ff" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="11" fill="#061218" stroke="#1e6f8f" stroke-width="1"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="11" fill="url(#g)"/>
  <g stroke="#8fd6ff" stroke-width="1.3" fill="none" opacity="0.65">
    <path d="M11 28V13h15"/><path d="M{W-11} 28V13h-15"/>
    <path d="M11 168v15h15"/><path d="M{W-11} 168v15h-15"/>
  </g>
  <text x="28" y="28" font-size="9.5" letter-spacing="2" fill="#4fb8e8">{LABEL_L}</text>
  <text x="{W-28}" y="28" font-size="9.5" letter-spacing="1.5" fill="#5b8399" text-anchor="end">{LABEL_R}</text>
  <rect x="18" y="{GROUND}" width="{W-36}" height="1" fill="url(#fx)"/>
  <text x="28" y="{H-11}" font-size="9.5" letter-spacing="1.2" fill="#5b8399">{CAPTION}</text>
</svg>'''


def ease(t):
    return t * t * (3 - 2 * t)


def travel(p):
    hold = 0.07
    if p < hold:
        return -AMP, 1
    if p < 0.5 - hold:
        u = (p - hold) / (0.5 - 2 * hold)
        return -AMP + 2 * AMP * ease(u), 1
    if p < 0.5 + hold:
        return AMP, -1
    if p < 1 - hold:
        u = (p - 0.5 - hold) / (0.5 - 2 * hold)
        return AMP - 2 * AMP * ease(u), -1
    return -AMP, 1


def radial_glow(color, size, bands=4):
    """Quầng sáng dạng 4 dải phẳng — nhìn vẫn mềm nhưng nén GIF tốt hơn hẳn gradient."""
    g = Image.new('L', (size, size), 0)
    d = ImageDraw.Draw(g)
    alphas = [12, 18, 24, 32]
    radii  = [0.72, 0.54, 0.36, 0.20]
    for i, (rr, al) in enumerate(zip(radii, alphas)):
        r = size / 2 * rr
        d.ellipse([size/2 - r, size/2 - r*0.74, size/2 + r, size/2 + r*0.74], fill=al)
    g = g.filter(ImageFilter.GaussianBlur(size * 0.10))
    out = Image.new('RGBA', (size, size), color + (0,))
    out.putalpha(g)
    return out


def main():
    cairosvg.svg2png(bytestring=STAGE.encode(), write_to='/tmp/_stage.png',
                     output_width=W, output_height=H, background_color='#061218')
    base = Image.open('/tmp/_stage.png').convert('RGBA')

    sprites = []
    for idx, hgt in zip((1, 2, 3), HEIGHTS):
        im = Image.open(os.path.join(ROOT, f'assets/mascots/m{idx}.png'))
        r = hgt / im.size[1]
        im = im.resize((max(1, round(im.size[0] * r)), hgt), Image.LANCZOS)
        canvas = Image.new('RGBA', (im.size[0] + PAD*2, im.size[1] + PAD*2), (0, 0, 0, 0))
        canvas.alpha_composite(im, (PAD, PAD))
        sprites.append(canvas)

    glows = [radial_glow(GLOW_RGB[k], sprites[k].size[0] * 5 // 2) for k in range(3)]

    # hạt sáng: mỗi hạt đi đúng 1 vòng trong 1 chu kỳ GIF -> lặp liền mạch
    dust = [(0.08 + 0.86 * ((i * 0.37) % 1.0),      # x (tỉ lệ)
             (i * 0.19) % 1.0,                       # pha y
             1 + (i % 3),                            # bán kính
             40 + (i * 13) % 60)                     # alpha
            for i in range(12)]

    frames = []
    for f in range(N):
        p = f / N
        t = p * N / FPS
        dxf, facing = travel(p)
        dx = int(round(dxf))
        fr = base.copy()
        overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)

        # ---- hạt sáng bay lên ----
        if DUST_ON:
            for xr, yph, rad, al in dust:
                yy = (1.0 - ((yph + t / (N / FPS)) % 1.0)) * (GROUND - 20) + 16
                xx = xr * (W - 80) + 40 + math.sin(2 * math.pi * (t / 3 + xr)) * 6
                od.ellipse([xx - rad, yy - rad, xx + rad, yy + rad],
                           fill=(141, 214, 255, al))

        # ---- quầng sáng sau lưng ----
        if GLOW_ON:
            g = Image.new('RGBA', (W, H), (0, 0, 0, 0))
            for k in range(3):
                pulse = 0.86 + 0.14 * math.sin(2 * math.pi * 1.0 * t + k * 2.094)
                gl = glows[k]
                sz = int(gl.size[0] * pulse)
                gl2 = gl.resize((sz, sz), Image.LANCZOS)
                a = int(46 * pulse)
                gl2.putalpha(gl2.getchannel('A').point(lambda v: v * a // 255))
                gx = CX[k] + dx - sz // 2
                gy = int(GROUND - sprites[k].size[1] * 0.55) - sz // 2
                g.alpha_composite(gl2, (gx, gy))
            overlay = Image.alpha_composite(overlay, g)

        fr.alpha_composite(overlay)

        # ---- bóng dưới chân ----
        shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(shadow)

        # ---- 3 nhân vật ----
        for k, sp in enumerate(sprites):
            ph = k * 2.094
            s = abs(math.sin(2 * math.pi * STEP_HZ * t + ph))       # 0..1 nhịp bước
            bob = int(round(-s * BOB))
            sy = 1 + SQUASH * (s - 0.5) * 2
            sx = 1 - SQUASH * (s - 0.5) * 2
            ang = SWAY * math.sin(2 * math.pi * STEP_HZ * t + ph + 1.2)

            im = sp.resize((max(1, int(sp.size[0] * sx)), max(1, int(sp.size[1] * sy))), Image.LANCZOS)
            if abs(ang) > 0.05:
                im = im.rotate(ang, resample=Image.BICUBIC, expand=False)
            if facing < 0:
                im = im.transpose(Image.FLIP_LEFT_RIGHT)
            bb = im.getbbox()
            if bb:
                im = im.crop(bb)
            x = int(CX[k] + dx - im.size[0] // 2)
            y = int(GROUND + bob - im.size[1])
            fr.alpha_composite(im, (x, y))

            # bóng: to khi ở đỉnh nhảy, nhỏ khi chạm đất
            ew = int(im.size[0] * (0.60 - 0.10 * s))
            cxs = int(CX[k] + dx)
            sd.ellipse([cxs - ew // 2, GROUND + 1, cxs + ew // 2, GROUND + 7],
                       fill=(2, 10, 15, int(150 - 50 * s)))
        fr.alpha_composite(shadow)
        frames.append(fr.convert('RGB'))

    # palette chung -> không nhấp nháy
    step = 6
    smp = Image.new('RGB', (W, H * ((len(frames) + step - 1) // step)))
    for i, x in enumerate(frames[::step]):
        smp.paste(x, (0, i * H))
    pal = smp.quantize(colors=COLORS, method=Image.MEDIANCUT)
    pf = [x.quantize(palette=pal, dither=Image.NONE) for x in frames]

    gif = os.path.join(ROOT, 'assets/crew-walk.gif')
    pf[0].save(gif, save_all=True, append_images=pf[1:], duration=int(1000 / FPS),
               loop=0, optimize=True, disposal=DISPOSAL)
    frames[N // 5].save(os.path.join(ROOT, 'assets/crew-walk.png'))
    print(f'OK  {gif}  {os.path.getsize(gif)/1024:.0f} KB  ({N} frames @ {FPS}fps)')


if __name__ == '__main__':
    main()
