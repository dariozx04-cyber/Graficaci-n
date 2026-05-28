# Reporte de proyecto 1

Dario Padilla Moreno

## Objetivo (qué debe hacer tu demo);

Construye un demo que muestre, de forma clara, temas del curso:

Escenas: mínimo 6 escenas controladas por una *timeline.

Curvas paramétricas: mínimo 6 curvas distintas (ej. Lissajous, espiral, rosa polar, lemniscata etc ) dibujadas con cv2.polylines.

Transformaciones: mínimo 2 de estas (y que se note):
traslación / rotación / escala (matrices afines 2x3)
espejo, shear
composición por capas (addWeighted, máscaras)

Primitivas: uso visible de line/circle/ellipse/fillPoly.
Post o filtro: mínimo 1 (blur, posterize, vignette, umbral, etc.).
Export final: video .mp4 o frames.

## Codigo: 

import time

import math

import numpy as np

import cv2

W, H = 800, 600

FPS = 30

DURATION = 36.0

def clamp01(x):

    return 0.0 if x < 0.0 else (1.0 if x > 1.0 else x)

def smoothstep(a, b, x):

    x = clamp01((x - a) / (b - a))
    return x * x * (3 - 2 * x)

def hsv_to_bgr(h, s, v):

    hsv = np.uint8([[[h % 180, np.clip(s, 0, 255), np.clip(v, 0, 255)]]])
    return tuple(int(x) for x in cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)[0, 0])

def poly_param(fx, fy, t0, t1, n, cx, cy, sx, sy):

    ts = np.linspace(t0, t1, n, dtype=np.float32)
    xs = fx(ts) * sx + cx
    ys = fy(ts) * sy + cy
    return np.round(np.stack([xs, ys], 1)).astype(np.int32).reshape((-1, 1, 2))

def post_vignette(img, strength=0.45):

    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    nx = (xx - W * 0.5) / (W * 0.5)
    ny = (yy - H * 0.5) / (H * 0.5)
    r2 = nx * nx + ny * ny
    mask = np.clip(1.0 - strength * r2, 0.0, 1.0)
    return (img.astype(np.float32) * mask[..., None]).astype(np.uint8)

def post_scanlines(img, strength=0.08):

    out = img.astype(np.float32)
    y = np.arange(H, dtype=np.float32)
    m = 1.0 - strength * (0.5 + 0.5 * np.sin(2 * np.pi * y / 3.0))
    out *= m[:, None, None]
    return np.clip(out, 0, 255).astype(np.uint8)

def post_posterize(img, q=16):
    return ((img // q) * q).astype(np.uint8)

def background_hsv_gradient(img, t, hue0=0, hue1=179):

    hsv = np.zeros((H, W, 3), np.uint8)
    ys = np.linspace(0, 1, H, dtype=np.float32)
    hue = (hue0 + (hue1 - hue0) * ys + 25 * np.sin(t * 0.8 + ys * 6.0)).astype(np.float32)
    hsv[:, :, 0] = np.clip(hue, 0, 179).astype(np.uint8)[:, None]
    hsv[:, :, 1] = 255
    hsv[:, :, 2] = (130 + 125 * (1 - ys)).astype(np.uint8)[:, None]
    img[:] = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def bg_stars(img, t):

    img[:] = (10, 10, 30)
    rng = np.random.default_rng(3)
    xs = rng.integers(0, W, 700)
    ys = rng.integers(0, H, 700)
    for x, y in zip(xs, ys):
        b = int(180 + 75 * math.sin(t * 4 + x * 0.05))
        cv2.circle(img, (x, y), 1, (b, b, b), -1)

def bg_waves(img, t):

    yy, xx = np.mgrid[0:H, 0:W]
    r = 127 + 127 * np.sin(xx * 0.03 + t * 2)
    g = 127 + 127 * np.sin(yy * 0.03 + t * 3)
    b = 127 + 127 * np.sin((xx + yy) * 0.02 + t)
    img[:, :, 0] = b.astype(np.uint8)
    img[:, :, 1] = g.astype(np.uint8)
    img[:, :, 2] = r.astype(np.uint8)

def bg_tunnel(img, t):

    yy, xx = np.mgrid[0:H, 0:W]
    xx = xx - W / 2
    yy = yy - H / 2
    d = np.sqrt(xx**2 + yy**2)
    ang = np.arctan2(yy, xx)
    v = 127 + 127 * np.sin(d * 0.05 - t * 8 + ang * 8)
    img[:, :, 0] = (v * 0.5).astype(np.uint8)
    img[:, :, 1] = (v * 0.8).astype(np.uint8)
    img[:, :, 2] = v.astype(np.uint8)

def bg_particles(img, t):
    img[:] = (0, 0, 0)
    for i in range(300):
        x = int(W / 2 + math.cos(i + t) * 300 + math.sin(t * 2 + i) * 100)
        y = int(H / 2 + math.sin(i + t) * 220)
        color = hsv_to_bgr(i + int(t * 40), 255, 255)
        cv2.circle(img, (x, y), 3, color, -1)

def bg_grid(img, t):

    img[:] = (20, 0, 40)
    for x in range(0, W, 40):
        shift = int(15 * math.sin(t + x * 0.02))
        cv2.line(img, (x + shift, 0), (x + shift, H), (100, 50, 255), 1)
    for y in range(0, H, 40):
        shift = int(15 * math.cos(t + y * 0.02))
        cv2.line(img, (0, y + shift), (W, y + shift), (255, 50, 100), 1)

def draw_particles(img, t, rng):

    n = 1500
    xs = rng.random(n) * W
    ys = rng.random(n) * H
    xs = (xs + 110 * np.sin(ys / 55.0 + t * 1.7)) % W
    ys = (ys + 85 * np.cos(xs / 75.0 + t * 1.2)) % H
    for x, y in zip(xs.astype(np.int32), ys.astype(np.int32)):
        color = hsv_to_bgr((x + y + int(t * 50)) % 180, 255, 255)
        cv2.circle(img, (x, y), 2, color, -1)

def draw_circle_shape(img, x, y, color):

    r = 18 + int(5 * math.sin(time.time() * 4 + x))
    cv2.circle(img, (x, y), r, color, -1, cv2.LINE_AA)

def draw_triangle_shape(img, x, y, color):

    s = 24 + int(4 * math.sin(time.time() * 4 + y))
    pts = np.array([[x, y - s], [x - s, y + s], [x + s, y + s]], np.int32)
    cv2.fillPoly(img, [pts], color)

def draw_square_shape(img, x, y, color):

    s = 18 + int(4 * math.sin(time.time() * 4 + x))
    cv2.rectangle(img, (x - s, y - s), (x + s, y + s), color, -1, cv2.LINE_AA)

def draw_star_shape(img, x, y, color):

    pts = []
    for i in range(10):

        ang = i * math.pi / 5
        r = 24 if i % 2 == 0 else 10
        px = int(x + r * math.cos(ang))
        py = int(y + r * math.sin(ang))
        pts.append([px, py])
    pts = np.array(pts, np.int32)
    cv2.fillPoly(img, [pts], color)

def orbit_shapes(img, t, cx, cy, count, radius, shape_func):

    for i in range(count):

        ang = (t * 0.9 + i * (2 * math.pi / count))
        wave = 25 * math.sin(t * 4 + i)
        rr = radius + wave
        x = int(cx + rr * math.cos(ang))
        y = int(cy + rr * math.sin(ang))
        color = hsv_to_bgr(i * 10 + int(t * 40), 255, 255)
        shape_func(img, x, y, color)

def scene_credits(img, t):

    background_hsv_gradient(img, t, 150, 30)
    rng = np.random.default_rng(1)
    xs = rng.integers(0, W, 500)
    ys = rng.integers(0, int(H * 0.7), 500)
    img[ys, xs] = (255, 255, 255)
    cv2.ellipse(img, (W // 2, H // 2), (280, 130), t * 20, 0, 360, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "proyecto final", (110, 240), cv2.FONT_HERSHEY_DUPLEX, 1.8, (255, 255, 255), 4, cv2.LINE_AA)
    cv2.putText(img, "si lee esto me da 100", (150, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 255, 255), 2, cv2.LINE_AA)

def scene1(img, t):

    bg_waves(img, t)
    draw_particles(img, t, np.random.default_rng(1))
    a = 3 + 0.7 * math.sin(t * 0.6)
    b = 2 + 0.7 * math.cos(t * 0.8)
    delta = math.pi / 2 + 0.4 * math.sin(t * 0.3)
    fx = lambda x: np.sin(a * x + delta)
    fy = lambda x: np.sin(b * x)
    pts = poly_param(fx, fy, 0, 2 * math.pi, 900, W * 0.5, H * 0.45, 260, 180)
    col = hsv_to_bgr(int(20 + 50 * np.sin(t)), 255, 255)
    total = len(pts)
    visible = int(total * (0.5 + 0.5 * math.sin(t * 2)))
    visible = max(20, visible)
    morph = pts[:visible].reshape(-1, 2).astype(np.float32)
    cx, cy = W * 0.5, H * 0.45
    for i in range(len(morph)):
        ang = (i / len(morph)) * 2 * math.pi
        r = 190 if i % 2 == 0 else 80
        sx = cx + r * math.cos(ang)
        sy = cy + r * math.sin(ang)
        morph[i][0] = (morph[i][0] * 0.55 + sx * 0.45)
        morph[i][1] = (morph[i][1] * 0.55 + sy * 0.45)
    morph = morph.astype(np.int32).reshape((-1, 1, 2))
    cv2.polylines(img, [morph], False, col, 5, cv2.LINE_AA)
    for i in range(18):
        ang = t * 0.7 + i * (2 * math.pi / 18)
        r = 280 if i % 2 == 0 else 140
        move = 20 * math.sin(t * 5 + i)
        x = int(cx + (r + move) * math.cos(ang))
        y = int(cy + (r + move) * math.sin(ang))
        draw_star_shape(img, x, y, hsv_to_bgr(i * 10 + int(t * 40), 255, 255))

def scene2(img, t):

    bg_tunnel(img, t)

    k = 5
    theta0 = t * 0.6
    fx = lambda th: (np.cos(k * th) * np.cos(th + theta0))
    fy = lambda th: (np.cos(k * th) * np.sin(th + theta0))
    pts = poly_param(fx, fy, 0, 2 * math.pi, 1400, W * 0.5, H * 0.45, 230, 230)
    col = hsv_to_bgr(int(145 + 30 * np.sin(t)), 255, 255)
    total = len(pts)
    visible = int(total * (0.5 + 0.5 * math.sin(t * 2)))
    visible = max(20, visible)
    curve = pts[:visible]
    cv2.polylines(img, [curve], False, col, 5, cv2.LINE_AA)
    orbit_shapes(img, t, W // 2, H // 2, 24, 260, draw_square_shape)

def scene3(img, t):

    bg_particles(img, t)
    fx = lambda th: (16 * np.sin(th) ** 3)
    fy = lambda th: (13 * np.cos(th) - 5 * np.cos(2 * th) - 2 * np.cos(3 * th) - np.cos(4 * th))
    pts = poly_param(fx, fy, 0, 2 * math.pi, 1600, W * 0.5, H * 0.45, 14, -14)
    col = hsv_to_bgr(int(170 + 10 * np.sin(t)), 255, 255)
    total = len(pts)
    visible = int(total * (0.5 + 0.5 * math.sin(t * 2)))
    visible = max(20, visible)
    curve = pts[:visible]
    cv2.polylines(img, [curve], False, col, 5, cv2.LINE_AA)
    cx = W // 2
    cy = H // 2
    size = 320
    tri = [(cx, cy - size), (cx - size, cy + size * 0.8), (cx + size, cy + size * 0.8)]
    for i in range(24):
        side = i % 3
        p = ((i // 3) / 8.0 + t * 0.15) % 1.0
        x1, y1 = tri[side]
        x2, y2 = tri[(side + 1) % 3]
        x = int(x1 * (1 - p) + x2 * p)
        y = int(y1 * (1 - p) + x2 * p)
        move = 15 * math.sin(t * 5 + i)
        nx = x - cx
        ny = y - cy
        dist = math.sqrt(nx * nx + ny * ny)
        if dist != 0:
            nx /= dist
            ny /= dist
        x += int(nx * move)
        y += int(ny * move)
        draw_triangle_shape(img, x, y, hsv_to_bgr(i * 15 + int(t * 50), 255, 255))

def scene4(img, t):

    bg_grid(img, t)
    cx = W // 2
    cy = H // 2
    rot = t * 0.9
    diamond = []
    for i in range(4):
        coordinates_ang = rot + i * math.pi / 2
        r = 230 if i % 2 == 0 else 130
        x = int(cx + r * math.cos(coordinates_ang))
        y = int(cy + r * math.sin(coordinates_ang))
        diamond.append([x, y])
    diamond.append(diamond[0])
    interp = []
    steps = 120
    for s in range(steps):

        p = s / steps
        if p < 0.25:
            a = p / 0.25
            x = diamond[0][0] * (1-a) + diamond[1][0] * a
            y = diamond[0][1] * (1-a) + diamond[1][1] * a
        elif p < 0.50:
            a = (p - 0.25) / 0.25
            x = diamond[1][0] * (1-a) + diamond[2][0] * a
            y = diamond[1][1] * (1-a) + diamond[2][1] * a
        elif p < 0.75:
            a = (p - 0.50) / 0.25
            x = diamond[2][0] * (1-a) + diamond[3][0] * a
            y = diamond[2][1] * (1-a) + diamond[3][1] * a
        else:
            a = (p - 0.75) / 0.25
            x = diamond[3][0] * (1-a) + diamond[0][0] * a
            y = diamond[3][1] * (1-a) + diamond[0][1] * a
        interp.append([x, y])
    interp = np.array(interp, np.int32).reshape((-1, 1, 2))
    total = len(interp)
    visible = int(total * (0.5 + 0.5 * math.sin(t * 2)))
    visible = max(10, visible)
    cv2.polylines(img, [interp[:visible]], False, hsv_to_bgr(int(t * 40), 255, 255), 6, cv2.LINE_AA)
    orbit_shapes(img, t, cx, cy, 20, 240, draw_circle_shape)

def scene5(img, t):

    bg_stars(img, t)
    fx = lambda th: np.cos(th) / (1 + np.sin(th)**2)
    fy = lambda th: (np.sin(th) * np.cos(th)) / (1 + np.sin(th)**2)
    pts = poly_param(fx, fy, -math.pi, math.pi, 600, W // 2, H // 2, 280, 280)
    total = len(pts)
    visible = int(total * (0.5 + 0.5 * math.sin(t * 2)))
    visible = max(20, visible)
    cv2.polylines(img, [pts[:visible]], True, (0, 255, 100), 5, cv2.LINE_AA)
    orbit_shapes(img, t, W // 2, H // 2, 12, 200, draw_star_shape)

def render_scene(img, scene, t):

    if scene == 0:
        scene_credits(img, t)
    elif scene == 1:
        scene1(img, t)
    elif scene == 2:
        scene2(img, t)
    elif scene == 3:
        scene3(img, t)
    elif scene == 4:
        scene4(img, t)
    else:
        scene5(img, t)

def main():

    buf = np.zeros((H, W, 3), np.uint8)
    total_frames = int(DURATION * FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter("proyecto_final.mp4", fourcc, FPS, (W, H))

    for i in range(total_frames):
        t = i / FPS
        
        block = int((t // 6) % 6)

        buf[:] = 0
        render_scene(buf, block, t)

        frame = post_vignette(buf, 0.45)
        frame = post_scanlines(frame, 0.08)
        frame = post_posterize(frame, 16)

        video_writer.write(frame)
        cv2.imshow("Proyecto Final", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    video_writer.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":

    main()

## Conclusion final
Este ejercicio demuestra la potencia de OpenCV no solo como herramienta de visión artificial, sino como un motor de síntesis gráfica de como se usan las primitivas y la importancia de las parametricas en greficaciones juntos con todas las operaciones aritmeticas.