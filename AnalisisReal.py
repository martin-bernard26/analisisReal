import streamlit as st
import requests
import time
from datetime import datetime

st.set_page_config(layout="wide")
if 'kumpulan' not in st.session_state:
    st.session_state['kumpulan'] = {'pendahuluan':True,'catatan':False,'hasil':False,'pertemuan1':False,
                        'pertemuan2':False,'pertemuan3':False, 'pertemuan4':False,'pertemuan5':False}

#======definisi+++++++++

def kover():
    tulisanHTML='''
    <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cover Analisis Real</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Crimson+Pro:ital,wght@0,300;0,400;0,600;1,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {
    --ink: #0a0a0f;
    --cream: #f5f0e8;
    --gold: #c9a84c;
    --gold-light: #e8c97a;
    --deep-blue: #0d1b3e;
    --mid-blue: #1a3060;
    --accent-red: #8b1a1a;
    --silver: #c8c8d0;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    width:auto;
    height: 1123px;
    overflow: hidden;
    font-family: 'Crimson Pro', serif;
    background: var(--deep-blue);
  }

  .page {
    width: 100%;
    height: 1123px;
    position: relative;
    background: var(--deep-blue);
    overflow: hidden;
  }

  /* ── Background layers ── */
  .bg-gradient {
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% 20%, #1e3a70 0%, #0d1b3e 55%, #050c1f 100%);
  }

  .grid-lines {
    position: absolute; inset: 0;
    background-image:
      linear-gradient(rgba(201,168,76,0.06) 1px, transparent 1px),
      linear-gradient(90deg, rgba(201,168,76,0.06) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: gridDrift 20s linear infinite;
  }

  @keyframes gridDrift {
    0%   { transform: translate(0, 0); }
    100% { transform: translate(40px, 40px); }
  }

  /* ── Math symbols floating ── */
  .math-field {
    position: absolute; inset: 0;
    pointer-events: none;
  }

  .sym {
    position: absolute;
    font-family: 'Playfair Display', serif;
    color: rgba(201,168,76,0.12);
    font-style: italic;
    animation: floatSym 12s ease-in-out infinite;
    user-select: none;
  }

  @keyframes floatSym {
    0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.1; }
    50%       { transform: translateY(-18px) rotate(4deg); opacity: 0.2; }
  }

  /* ── Decorative arcs ── */
  .arc-svg {
    position: absolute; inset: 0;
    width: 100%; height: 100%;
  }

  /* ── Corner ornaments ── */
  .corner {
    position: absolute;
    width: 90px; height: 90px;
  }
  .corner svg { width: 100%; height: 100%; }
  .corner--tl { top: 22px; left: 22px; }
  .corner--tr { top: 22px; right: 22px; transform: scaleX(-1); }
  .corner--bl { bottom: 22px; left: 22px; transform: scaleY(-1); }
  .corner--br { bottom: 22px; right: 22px; transform: scale(-1); }

  /* ── Border frame ── */
  .frame-outer {
    position: absolute;
    top: 18px; left: 18px; right: 18px; bottom: 18px;
    border: 1.5px solid rgba(201,168,76,0.35);
  }
  .frame-inner {
    position: absolute;
    top: 26px; left: 26px; right: 26px; bottom: 26px;
    border: 0.5px solid rgba(201,168,76,0.18);
  }

  /* ── Top band ── */
  .top-band {
    position: absolute;
    top: 38px; left: 38px; right: 38px;
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    opacity: 0.7;
  }
  .bottom-band {
    position: absolute;
    bottom: 38px; left: 38px; right: 38px;
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    opacity: 0.7;
  }

  /* ── Publisher label (top) ── */
  .pub-label {
    position: absolute;
    top: 52px;
    left: 0; right: 0;
    text-align: center;
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    letter-spacing: 5px;
    color: rgba(201,168,76,0.55);
    text-transform: uppercase;
  }

  /* ── Emblem / crest ── */
  .emblem {
    position: absolute;
    top: 78px;
    left: 50%;
    transform: translateX(-50%);
    width: 90px;
    height: 90px;
  }
  .emblem svg { width: 100%; height: 100%; }

  /* ── Main title block ── */
  .title-block {
    position: absolute;
    top: 185px;
    left: 50px; right: 50px;
    text-align: center;
  }

  .title-subtitle {
    font-family: 'Space Mono', monospace;
    font-size: 9.5px;
    letter-spacing: 6px;
    color: var(--gold);
    text-transform: uppercase;
    opacity: 0.8;
    margin-bottom: 14px;
    animation: fadeSlide 1.2s ease forwards;
  }

  .title-main {
    font-family: 'Playfair Display', serif;
    font-weight: 900;
    font-size: 72px;
    line-height: 0.95;
    color: var(--cream);
    letter-spacing: -1px;
    animation: fadeSlide 1.2s 0.2s ease both;
    text-shadow: 0 4px 40px rgba(201,168,76,0.3);
  }

  .title-main span {
    display: block;
    color: var(--gold);
    font-style: italic;
    font-size: 80px;
    text-shadow: 0 6px 50px rgba(201,168,76,0.5);
  }

  .title-divider {
    display: flex;
    align-items: center;
    gap: 12px;
    justify-content: center;
    margin: 22px 0 18px;
    animation: fadeSlide 1.2s 0.4s ease both;
  }
  .title-divider::before,
  .title-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold));
    opacity: 0.5;
  }
  .title-divider::after {
    background: linear-gradient(270deg, transparent, var(--gold));
  }
  .divider-diamond {
    width: 7px; height: 7px;
    background: var(--gold);
    transform: rotate(45deg);
    box-shadow: 0 0 10px var(--gold);
  }

  @keyframes fadeSlide {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* ── Material list ── */
  .materials-wrap {
    position: absolute;
    top: 370px;
    left: 50px; right: 50px;
    animation: fadeSlide 1.2s 0.6s ease both;
  }

  .materials-header {
    font-family: 'Space Mono', monospace;
    font-size: 8px;
    letter-spacing: 5px;
    color: rgba(201,168,76,0.6);
    text-align: center;
    text-transform: uppercase;
    margin-bottom: 16px;
  }

  .materials-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7px 24px;
  }

  .mat-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 8px 12px;
    background: rgba(201,168,76,0.04);
    border-left: 2px solid rgba(201,168,76,0.3);
    border-bottom: 1px solid rgba(201,168,76,0.08);
    position: relative;
    transition: background 0.3s;
  }

  .mat-num {
    font-family: 'Space Mono', monospace;
    font-size: 8.5px;
    color: var(--gold);
    opacity: 0.7;
    min-width: 18px;
    margin-top: 1px;
    letter-spacing: 1px;
  }

  .mat-text {
    font-family: 'Crimson Pro', serif;
    font-size: 18px;
    color: rgba(245,240,232,0.82);
    line-height: 1.38;
    font-style: italic;
  }

  /* ── Bottom author block ── */
  .author-block {
    position: absolute;
    bottom: 58px;
    left: 50px; right: 50px;
    text-align: center;
    animation: fadeSlide 1.2s 0.9s ease both;
  }

  .author-rule {
    width: 200px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 0 auto 14px;
    opacity: 0.6;
  }

  .author-prefix {
    font-family: 'Space Mono', monospace;
    font-size: 8px;
    letter-spacing: 4px;
    color: rgba(201,168,76,0.5);
    text-transform: uppercase;
    margin-bottom: 5px;
  }

  .author-name {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-weight: 700;
    color: var(--cream);
    letter-spacing: 1px;
  }

  .author-title {
    font-family: 'Crimson Pro', serif;
    font-size: 13px;
    color: var(--gold);
    font-style: italic;
    margin-top: 3px;
  }

  /* ── Glow spots ── */
  .glow {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    pointer-events: none;
  }
  .glow-1 {
    width: 400px; height: 300px;
    top: 0; left: -100px;
    background: rgba(201,168,76,0.07);
  }
  .glow-2 {
    width: 350px; height: 350px;
    bottom: 0; right: -80px;
    background: rgba(30,80,160,0.15);
  }
  .glow-3 {
    width: 200px; height: 200px;
    top: 300px; left: 50%;
    transform: translateX(-50%);
    background: rgba(201,168,76,0.05);
    filter: blur(50px);
  }
</style>
</head>
<body>
<div class="page">

  <!-- Background layers -->
  <div class="bg-gradient"></div>
  <div class="grid-lines"></div>

  <!-- Glow -->
  <div class="glow glow-1"></div>
  <div class="glow glow-2"></div>
  <div class="glow glow-3"></div>

  <!-- Decorative arc SVG -->
  <svg class="arc-svg" viewBox="0 0 794 1123" fill="none" xmlns="http://www.w3.org/2000/svg">
    <ellipse cx="397" cy="-60" rx="380" ry="280" stroke="rgba(201,168,76,0.10)" stroke-width="1"/>
    <ellipse cx="397" cy="1183" rx="380" ry="280" stroke="rgba(201,168,76,0.10)" stroke-width="1"/>
    <path d="M 0 560 Q 397 400 794 560" stroke="rgba(201,168,76,0.06)" stroke-width="1" fill="none"/>
    <circle cx="397" cy="165" r="130" stroke="rgba(201,168,76,0.08)" stroke-width="0.5" stroke-dasharray="4 8"/>
    <circle cx="397" cy="165" r="105" stroke="rgba(201,168,76,0.06)" stroke-width="0.5"/>
  </svg>

  <!-- Floating math symbols -->
  <div class="math-field">
    <div class="sym" style="font-size:42px;top:140px;left:60px;animation-delay:0s">∑</div>
    <div class="sym" style="font-size:34px;top:250px;left:32px;animation-delay:2s">∫</div>
    <div class="sym" style="font-size:28px;top:460px;left:44px;animation-delay:4s">ε</div>
    <div class="sym" style="font-size:38px;top:600px;left:28px;animation-delay:1s">δ</div>
    <div class="sym" style="font-size:32px;top:760px;left:55px;animation-delay:3s">∞</div>
    <div class="sym" style="font-size:40px;top:140px;right:60px;animation-delay:1.5s">ℝ</div>
    <div class="sym" style="font-size:30px;top:280px;right:38px;animation-delay:3.5s">∀</div>
    <div class="sym" style="font-size:36px;top:450px;right:50px;animation-delay:0.5s">∃</div>
    <div class="sym" style="font-size:26px;top:620px;right:36px;animation-delay:2.5s">⊂</div>
    <div class="sym" style="font-size:34px;top:780px;right:52px;animation-delay:4.5s">≤</div>
    <div class="sym" style="font-size:22px;top:920px;left:80px;animation-delay:1s">lim</div>
    <div class="sym" style="font-size:22px;top:920px;right:80px;animation-delay:2s">sup</div>
  </div>

  <!-- Border frame -->
  <div class="frame-outer"></div>
  <div class="frame-inner"></div>
  <div class="top-band"></div>
  <div class="bottom-band"></div>

  <!-- Corner ornaments -->
  <div class="corner corner--tl">
    <svg viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M5 85 L5 5 L85 5" stroke="rgba(201,168,76,0.6)" stroke-width="1.5"/>
      <path d="M5 55 L5 5 L55 5" stroke="rgba(201,168,76,0.3)" stroke-width="0.7"/>
      <circle cx="5" cy="5" r="3" fill="rgba(201,168,76,0.6)"/>
      <rect x="0" y="0" width="6" height="6" fill="rgba(201,168,76,0.2)" transform="rotate(45 3 3)"/>
    </svg>
  </div>
  <div class="corner corner--tr">
    <svg viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M5 85 L5 5 L85 5" stroke="rgba(201,168,76,0.6)" stroke-width="1.5"/>
      <path d="M5 55 L5 5 L55 5" stroke="rgba(201,168,76,0.3)" stroke-width="0.7"/>
      <circle cx="5" cy="5" r="3" fill="rgba(201,168,76,0.6)"/>
    </svg>
  </div>
  <div class="corner corner--bl">
    <svg viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M5 85 L5 5 L85 5" stroke="rgba(201,168,76,0.6)" stroke-width="1.5"/>
      <path d="M5 55 L5 5 L55 5" stroke="rgba(201,168,76,0.3)" stroke-width="0.7"/>
      <circle cx="5" cy="5" r="3" fill="rgba(201,168,76,0.6)"/>
    </svg>
  </div>
  <div class="corner corner--br">
    <svg viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M5 85 L5 5 L85 5" stroke="rgba(201,168,76,0.6)" stroke-width="1.5"/>
      <path d="M5 55 L5 5 L55 5" stroke="rgba(201,168,76,0.3)" stroke-width="0.7"/>
      <circle cx="5" cy="5" r="3" fill="rgba(201,168,76,0.6)"/>
    </svg>
  </div>

  <!-- Publisher label -->
  <div class="pub-label">Matematika · Analisis · Teori Bilangan</div>

  <!-- Emblem -->
  <div class="emblem">
    <svg viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg">
      <polygon points="45,4 83,26 83,64 45,86 7,64 7,26" stroke="rgba(201,168,76,0.7)" stroke-width="1.2" fill="rgba(201,168,76,0.05)"/>
      <polygon points="45,12 77,30 77,60 45,78 13,60 13,30" stroke="rgba(201,168,76,0.35)" stroke-width="0.6" fill="none"/>
      <circle cx="45" cy="45" r="18" stroke="rgba(201,168,76,0.5)" stroke-width="0.8" fill="rgba(13,27,62,0.5)"/>
      <text x="45" y="52" text-anchor="middle" font-family="Playfair Display,serif" font-size="22" font-style="italic" fill="rgba(201,168,76,0.9)">ℝ</text>
    </svg>
  </div>

  <!-- Title block -->
  <div class="title-block">
    <div class="title-subtitle">Buku Teks Perguruan Tinggi</div>
    <div class="title-main">
      Analisis<span>Real</span>
    </div>
    <div class="title-divider"><div class="divider-diamond"></div></div>
  </div>

  <!-- Material list -->
  <div class="materials-wrap">
    <div class="materials-header">— Pokok Bahasan —</div>
    <div class="materials-grid">

      <div class="mat-item">
        <div class="mat-num">01</div>
        <div class="mat-text">Bilangan Real Sebagai Bentuk Desimal</div>
      </div>
      <div class="mat-item">
        <div class="mat-num">02</div>
        <div class="mat-text">Sifat-sifat Aljabar dan Urutan</div>
      </div>

      <div class="mat-item">
        <div class="mat-num">03</div>
        <div class="mat-text">Akar, Persamaan Kuadrat &amp; Nilai Mutlak</div>
      </div>
      <div class="mat-item">
        <div class="mat-num">04</div>
        <div class="mat-text">Paradoks Zeno dan Himpunan Terbatas</div>
      </div>

      <div class="mat-item">
        <div class="mat-num">05</div>
        <div class="mat-text">Sifat Kelengkapan &amp; Manipulasi Supremum dan Infimum</div>
      </div>
      <div class="mat-item">
        <div class="mat-num">06</div>
        <div class="mat-text">Masalah Maksimum, Minimum, Interval</div>
      </div>

      <div class="mat-item">
        <div class="mat-num">07</div>
        <div class="mat-text">Prinsip Induksi Matematika</div>
      </div>
      <div class="mat-item">
        <div class="mat-num">08</div>
        <div class="mat-text">Barisan dan Kekonvergenan Barisan</div>
      </div>

      <div class="mat-item">
        <div class="mat-num">09</div>
        <div class="mat-text">Teorema-teorema Limit dan Barisan Monoton</div>
      </div>
      <div class="mat-item">
        <div class="mat-num">10</div>
        <div class="mat-text">Sub Barisan &amp; Teorema Bolzano-Weierstrass</div>
      </div>

      <div class="mat-item">
        <div class="mat-num">11</div>
        <div class="mat-text">Barisan Cauchy dan Barisan Divergen Sejati</div>
      </div>
      <div class="mat-item">
        <div class="mat-num">12</div>
        <div class="mat-text">Deret, Kekonvergenan &amp; Deret Suku-suku Positif</div>
      </div>

      <div class="mat-item">
        <div class="mat-num">13</div>
        <div class="mat-text">Sifat-sifat Dasar Deret dan Kriteria Cauchy</div>
      </div>
      <div class="mat-item">
        <div class="mat-num">14</div>
        <div class="mat-text">Kekonvergenan Mutlak dan Bersyarat</div>
      </div>

    </div>
  </div>

  <!-- Author block -->
  <div class="author-block">
    <div class="author-rule"></div>
    <div class="author-prefix">Disusun Oleh</div>
    <div class="author-name">Martin Bernard</div>
    <div class="author-title">M.Pd</div>
  </div>

</div>
</body>
</html>
    '''
    st.components.v1.html(tulisanHTML, height=1100)

def materi1():
    tulisanHTML = '''
    <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Judul Bar - Bilangan Real</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Cinzel:wght@400;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #0e1117;
    padding: 40px 20px;
  }

  .wrapper {
    width: 100%;
    max-width: 900px;
  }

  /* ── MAIN BAR ── */
  .title-bar {
    position: relative;
    width: 100%;
    padding: 0;
    overflow: hidden;
    border-radius: 4px;
    box-shadow:
      0 0 0 1px rgba(201,168,76,0.25),
      0 8px 60px rgba(0,0,0,0.6),
      0 0 80px rgba(201,168,76,0.08);
  }

  .bar-bg {
    position: absolute; inset: 0;
    background:
      linear-gradient(105deg,
        #0a1628 0%,
        #0f2044 30%,
        #14286a 52%,
        #0f1e50 72%,
        #080e20 100%
      );
  }

  .bar-shimmer {
    position: absolute; inset: 0;
    background: linear-gradient(
      110deg,
      transparent 20%,
      rgba(201,168,76,0.07) 45%,
      rgba(201,168,76,0.12) 50%,
      rgba(201,168,76,0.07) 55%,
      transparent 80%
    );
    animation: shimmer 4s ease-in-out infinite;
  }
  @keyframes shimmer {
    0%   { transform: translateX(-100%); }
    60%  { transform: translateX(100%); }
    100% { transform: translateX(100%); }
  }

  .bar-texture {
    position: absolute; inset: 0;
    background-image: repeating-linear-gradient(
      -55deg,
      transparent,
      transparent 18px,
      rgba(255,255,255,0.012) 18px,
      rgba(255,255,255,0.012) 19px
    );
  }

  .bar-line-top {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2.5px;
    background: linear-gradient(90deg,
      transparent 0%,
      rgba(201,168,76,0.3) 10%,
      rgba(201,168,76,0.9) 30%,
      #e8c97a 50%,
      rgba(201,168,76,0.9) 70%,
      rgba(201,168,76,0.3) 90%,
      transparent 100%
    );
  }

  .bar-line-bottom {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg,
      transparent 0%,
      rgba(201,168,76,0.2) 15%,
      rgba(201,168,76,0.6) 50%,
      rgba(201,168,76,0.2) 85%,
      transparent 100%
    );
  }

  .bar-accent-left {
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 6px;
    background: linear-gradient(180deg,
      transparent,
      rgba(201,168,76,0.9) 20%,
      #e8c97a 50%,
      rgba(201,168,76,0.9) 80%,
      transparent
    );
  }

  .bar-accent-right {
    position: absolute;
    right: 0; top: 0; bottom: 0;
    width: 6px;
    background: linear-gradient(180deg,
      transparent,
      rgba(201,168,76,0.9) 20%,
      #e8c97a 50%,
      rgba(201,168,76,0.9) 80%,
      transparent
    );
  }

  .bar-glow {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 60%; height: 160%;
    background: radial-gradient(ellipse, rgba(201,168,76,0.07) 0%, transparent 70%);
    pointer-events: none;
  }

  /* ── CONTENT ── */
  .bar-content {
    position: relative;
    z-index: 2;
    display: flex;
    align-items: center;
    padding: 28px 48px 28px 38px;
    gap: 26px;
  }

  .ornament {
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
  }
  .orn-symbol {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 38px;
    color: rgba(201,168,76,0.85);
    line-height: 1;
    text-shadow: 0 0 20px rgba(201,168,76,0.5);
    animation: pulse 3s ease-in-out infinite;
  }
  @keyframes pulse {
    0%, 100% { opacity: 0.85; text-shadow: 0 0 20px rgba(201,168,76,0.4); }
    50%       { opacity: 1;    text-shadow: 0 0 35px rgba(201,168,76,0.8); }
  }
  .orn-dot {
    width: 4px; height: 4px;
    background: rgba(201,168,76,0.6);
    border-radius: 50%;
  }
  .orn-line {
    width: 1px;
    height: 28px;
    background: linear-gradient(180deg, rgba(201,168,76,0.6), transparent);
  }

  .divider-v {
    flex-shrink: 0;
    width: 1px;
    height: 64px;
    background: linear-gradient(180deg, transparent, rgba(201,168,76,0.5) 30%, rgba(201,168,76,0.5) 70%, transparent);
  }

  .text-block {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .text-label {
    font-family: 'Space Mono', monospace;
    font-size: 8.5px;
    letter-spacing: 5px;
    color: rgba(201,168,76,0.55);
    text-transform: uppercase;
    animation: fadeIn 1s ease forwards;
  }

  .text-title {
    font-family: 'Cinzel', serif;
    font-weight: 700;
    font-size: 28px;
    line-height: 1.1;
    color: #f5f0e8;
    letter-spacing: 0.5px;
    text-shadow: 0 2px 20px rgba(0,0,0,0.5);
    animation: fadeIn 1s 0.2s ease both;
  }

  .text-title em {
    color: #e8c97a;
    font-style: normal;
    text-shadow: 0 0 25px rgba(232,201,122,0.4);
  }

  .text-sub {
    display: flex;
    align-items: center;
    gap: 8px;
    animation: fadeIn 1s 0.4s ease both;
  }
  .text-sub-line {
    width: 28px; height: 1px;
    background: rgba(201,168,76,0.5);
  }
  .text-sub-text {
    font-family: 'Space Mono', monospace;
    font-size: 8px;
    letter-spacing: 3px;
    color: rgba(201,168,76,0.45);
    text-transform: uppercase;
  }

  .chapter-badge {
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 64px;
    height: 64px;
    position: relative;
    animation: fadeIn 1s 0.3s ease both;
  }
  .chapter-badge svg {
    position: absolute; inset: 0;
    width: 100%; height: 100%;
  }
  .badge-num {
    position: relative;
    z-index: 1;
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 900;
    color: rgba(201,168,76,0.9);
    line-height: 1;
    text-shadow: 0 0 15px rgba(201,168,76,0.5);
  }
  .badge-label {
    position: relative;
    z-index: 1;
    font-family: 'Space Mono', monospace;
    font-size: 6.5px;
    letter-spacing: 2px;
    color: rgba(201,168,76,0.5);
    text-transform: uppercase;
    margin-top: 2px;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
  }
</style>
</head>
<body>
<div class="wrapper">
  <div class="title-bar">
    <div class="bar-bg"></div>
    <div class="bar-shimmer"></div>
    <div class="bar-texture"></div>
    <div class="bar-glow"></div>
    <div class="bar-line-top"></div>
    <div class="bar-line-bottom"></div>
    <div class="bar-accent-left"></div>
    <div class="bar-accent-right"></div>

    <div class="bar-content">

      <div class="ornament">
        <div class="orn-symbol">ℝ</div>
        <div class="orn-dot"></div>
        <div class="orn-line"></div>
      </div>

      <div class="divider-v"></div>

      <div class="text-block">
        <div class="text-label">Analisis Real &nbsp;·&nbsp; Materi 01</div>
        <div class="text-title">
          Bilangan <em>Real</em> Sebagai Bentuk Desimal
        </div>
        <div class="text-sub">
          <div class="text-sub-line"></div>
          <div class="text-sub-text">Real Number &nbsp;·&nbsp; Decimal Representation</div>
        </div>
      </div>

      <div class="chapter-badge">
        <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
          <polygon points="32,2 60,18 60,46 32,62 4,46 4,18"
            stroke="rgba(201,168,76,0.5)" stroke-width="1" fill="rgba(201,168,76,0.05)"/>
          <polygon points="32,8 55,21 55,43 32,56 9,43 9,21"
            stroke="rgba(201,168,76,0.2)" stroke-width="0.5" fill="none"/>
        </svg>
        <div class="badge-num">01</div>
        <div class="badge-label">Bab</div>
      </div>

    </div>
  </div>
</div>
</body>
</html>
    '''
    st.components.v1.html(tulisanHTML, height=200)
    st.image(["https://image.slidesharecdn.com/babisistembilanganriil-130824064846-phpapp02/75/Matematika-Dasar-Bab-I-Sistem-Bilangan-Riil-3-2048.jpg","https://image.slidesharecdn.com/babisistembilanganriil-130824064846-phpapp02/75/Matematika-Dasar-Bab-I-Sistem-Bilangan-Riil-2-2048.jpg"], width=400)
    with st.expander("Soal Diagnosa"):
        tulisanHTML3 = """
        <iframe src=' https://martin-bernard26.github.io/simulasiCauchy/soaldiagreal1.html' style="width:100%; height:1500px; border:none;">
        </iframe>
        """
        st.components.v1.html(tulisanHTML3,height=1000)
    st.subheader("A. Konstruksi Dasar: Dari Rasional ke Desimal")
    st.markdown(" ##### Secara deduktif, kita berangkat dari fakta bahwa setiap bilangan real x dapat dinyatakan dalam bentuk:")
    st.latex("x= a_{0},a_{1}a_{2}a_{3}\dots")
    st.markdown("""
    ##### Di mana:
    >* $a_{0}\in{Z}$
    >* $a_{n}\in{0, 1, 2,\dots,9},\\; \\forall{n}\in{N}$
    """)
    st.markdown("##### **Definisi Formal**")
    st.markdown("##### Secara matematis, ekspresi desimal di atas sebenarnya adalah representasi dari sebuah deret tak hingga:")
    st.latex("x=a_{0}+\sum_{n=1}^{\infty}{\\frac{a_{n}}{10^{n}}}")
    st.markdown("##### Karena $0≤a_n≤9$, deret ini dijamin konvergen berdasarkan uji banding dengan deret geometri yang konvergen, sehingga setiap barisan desimal selalu merujuk pada satu bilangan real spesifik.")
    st.subheader("B. Sifat-sifat Penting")
    st.markdown("#### 1. Ketunggalan (Uniqss) dan Masalah 0,999...")
    st.markdown("##### Satu aspek yang sering membingungkan adalah bahwa representasi desimal tidak selalu tunggal. Bilangan rasional yang penyebutnya memiliki faktor prima hanya 2 dan 5 (desimal terminasi) memiliki dua representasi.")
    st.markdown("""
    >* Contoh: $1,000...=0,999...$
    >* Aturan Formal: Untuk menjamin ketunggalan dalam analisis formal, kita biasanya menyepakati untuk tidak menggunakan barisan desimal yang berakhir dengan angka 9 berulang secara terus-menerus.
    """)
    st.markdown("#### 2. Sifat-sifat Penting")
    st.markdown("##### Di antara dua bilangan real sembarang, selalu terdapat bilangan real lainnya. Dalam bentuk desimal, ini terlihat dari kemampuan kita untuk menyisipkan digit di posisi desimal yang lebih dalam (n yang lebih besar).")
    st.markdown("#### 3. Hubungan dengan Rasionalitas")
    st.markdown("""
    >* Bilangan Rasional: Memiliki ekspresi desimal yang berhenti (terminating) atau berulang (repeating).
    >* Bilangan Irrasional: Memiliki ekspresi desimal yang tidak berhenti dan tidak berulang. Contoh klasik: √2 atau π.
    """)
    tulisanHTML1="""
    <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kalkulator Ilmiah</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #080c14;
    background-image:
      radial-gradient(ellipse 80% 60% at 50% 0%, #0d1f3c 0%, transparent 70%),
      repeating-linear-gradient(0deg, transparent, transparent 39px, rgba(0,200,255,0.03) 39px, rgba(0,200,255,0.03) 40px),
      repeating-linear-gradient(90deg, transparent, transparent 39px, rgba(0,200,255,0.03) 39px, rgba(0,200,255,0.03) 40px);
    font-family: 'Share Tech Mono', monospace;
  }

  .calc-shell {
    background: linear-gradient(160deg, #0f1923 0%, #0a1018 60%, #0d1520 100%);
    border: 1px solid rgba(0,200,255,0.15);
    border-radius: 20px;
    padding: 28px 24px 24px;
    width: 340px;
    box-shadow:
      0 0 0 1px rgba(0,200,255,0.06),
      0 30px 80px rgba(0,0,0,0.8),
      0 0 60px rgba(0,150,255,0.05),
      inset 0 1px 0 rgba(255,255,255,0.05);
    position: relative;
    overflow: hidden;
  }

  /* scanline effect */
  .calc-shell::before {
    content: '';
    position: absolute; inset: 0;
    background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.08) 2px, rgba(0,0,0,0.08) 4px);
    pointer-events: none;
    z-index: 10;
    border-radius: 20px;
  }

  /* top glow line */
  .calc-shell::after {
    content: '';
    position: absolute;
    top: 0; left: 20%; right: 20%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,200,255,0.6), transparent);
  }

  /* ── HEADER ── */
  .calc-header {
    text-align: center;
    margin-bottom: 18px;
  }
  .calc-brand {
    font-family: 'Orbitron', monospace;
    font-size: 11px;
    letter-spacing: 6px;
    color: rgba(0,200,255,0.5);
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .calc-model {
    font-family: 'Space Mono', monospace;
    font-size: 8px;
    letter-spacing: 3px;
    color: rgba(255,255,255,0.15);
  }

  /* ── DISPLAY ── */
  .display-wrap {
    background: #040a0f;
    border: 1px solid rgba(0,200,255,0.12);
    border-radius: 10px;
    padding: 14px 18px 12px;
    margin-bottom: 20px;
    position: relative;
    box-shadow: inset 0 2px 12px rgba(0,0,0,0.6), 0 0 20px rgba(0,200,255,0.04);
  }
  .display-wrap::before {
    content: '';
    position: absolute;
    top: 0; left: 10%; right: 10%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,200,255,0.2), transparent);
  }

  .display-expr {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    color: rgba(0,200,255,0.45);
    text-align: right;
    min-height: 18px;
    letter-spacing: 1px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-bottom: 6px;
  }

  .display-main {
    font-family: 'Orbitron', monospace;
    font-size: 34px;
    font-weight: 700;
    color: #00e5ff;
    text-align: right;
    letter-spacing: 1px;
    min-height: 44px;
    line-height: 1.1;
    text-shadow: 0 0 20px rgba(0,229,255,0.5), 0 0 40px rgba(0,229,255,0.2);
    overflow: hidden;
    word-break: break-all;
    transition: font-size 0.1s;
  }

  .display-status {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 8px;
  }
  .status-mode {
    font-size: 8px;
    letter-spacing: 3px;
    color: rgba(0,200,255,0.3);
    text-transform: uppercase;
  }
  .status-dot {
    width: 5px; height: 5px;
    background: #00e5ff;
    border-radius: 50%;
    box-shadow: 0 0 8px rgba(0,229,255,0.8);
    animation: blink 2s ease-in-out infinite;
  }
  @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.2; }
  }

  /* ── BUTTONS ── */
  .btn-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
  }

  .btn {
    position: relative;
    height: 56px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-family: 'Space Mono', monospace;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.5px;
    transition: all 0.12s ease;
    outline: none;
    overflow: hidden;
    -webkit-tap-highlight-color: transparent;
  }

  .btn::after {
    content: '';
    position: absolute;
    inset: 0;
    background: rgba(255,255,255,0);
    border-radius: 10px;
    transition: background 0.12s;
  }
  .btn:active::after { background: rgba(255,255,255,0.1); }
  .btn:active { transform: scale(0.94); }

  /* number buttons */
  .btn-num {
    background: linear-gradient(160deg, #1a2535 0%, #111b28 100%);
    color: #d0e8ff;
    border: 1px solid rgba(255,255,255,0.07);
    box-shadow: 0 4px 12px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05);
  }
  .btn-num:hover { background: linear-gradient(160deg, #1e2d40 0%, #152030 100%); border-color: rgba(0,200,255,0.2); }

  /* operator buttons */
  .btn-op {
    background: linear-gradient(160deg, #0d2a3a 0%, #081e2a 100%);
    color: #00ccff;
    border: 1px solid rgba(0,200,255,0.2);
    box-shadow: 0 4px 12px rgba(0,0,0,0.4), inset 0 1px 0 rgba(0,200,255,0.1);
    text-shadow: 0 0 10px rgba(0,200,255,0.4);
  }
  .btn-op:hover { background: linear-gradient(160deg, #103345 0%, #0a2535 100%); border-color: rgba(0,200,255,0.4); box-shadow: 0 4px 16px rgba(0,0,0,0.4), 0 0 12px rgba(0,200,255,0.1); }

  /* special function buttons */
  .btn-fn {
    background: linear-gradient(160deg, #1a1a30 0%, #111125 100%);
    color: #a78bfa;
    border: 1px solid rgba(167,139,250,0.2);
    box-shadow: 0 4px 12px rgba(0,0,0,0.4), inset 0 1px 0 rgba(167,139,250,0.08);
    font-size: 12px;
    text-shadow: 0 0 10px rgba(167,139,250,0.3);
  }
  .btn-fn:hover { border-color: rgba(167,139,250,0.4); box-shadow: 0 4px 16px rgba(0,0,0,0.4), 0 0 12px rgba(167,139,250,0.1); }

  /* equals button */
  .btn-eq {
    background: linear-gradient(160deg, #005580 0%, #003d5e 100%);
    color: #00e5ff;
    border: 1px solid rgba(0,229,255,0.35);
    box-shadow: 0 4px 20px rgba(0,150,200,0.25), inset 0 1px 0 rgba(0,229,255,0.15);
    font-size: 20px;
    text-shadow: 0 0 15px rgba(0,229,255,0.7);
  }
  .btn-eq:hover { background: linear-gradient(160deg, #006a9e 0%, #004d75 100%); box-shadow: 0 4px 24px rgba(0,180,230,0.35), 0 0 20px rgba(0,229,255,0.15); }

  /* clear button */
  .btn-clr {
    background: linear-gradient(160deg, #2a0d0d 0%, #1e0808 100%);
    color: #ff5555;
    border: 1px solid rgba(255,80,80,0.25);
    box-shadow: 0 4px 12px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,80,80,0.08);
    text-shadow: 0 0 10px rgba(255,80,80,0.3);
  }
  .btn-clr:hover { border-color: rgba(255,80,80,0.45); box-shadow: 0 4px 16px rgba(0,0,0,0.4), 0 0 12px rgba(255,80,80,0.15); }

  /* backspace */
  .btn-bs {
    background: linear-gradient(160deg, #1e1408 0%, #150e05 100%);
    color: #ffaa44;
    border: 1px solid rgba(255,170,68,0.2);
    box-shadow: 0 4px 12px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,170,68,0.05);
    font-size: 16px;
    text-shadow: 0 0 10px rgba(255,170,68,0.3);
  }
  .btn-bs:hover { border-color: rgba(255,170,68,0.4); }

  /* span 2 cols */
  .span2 { grid-column: span 2; }

  /* ── FOOTER ── */
  .calc-footer {
    margin-top: 16px;
    text-align: center;
    font-family: 'Space Mono', monospace;
    font-size: 7px;
    letter-spacing: 3px;
    color: rgba(255,255,255,0.08);
    text-transform: uppercase;
  }
</style>
</head>
<body>

<div class="calc-shell">
  <div class="calc-header">
    <div class="calc-brand">Scientific Calc</div>
    <div class="calc-model">Model · SR-01 · v2.0</div>
  </div>

  <div class="display-wrap">
    <div class="display-expr" id="expr"></div>
    <div class="display-main" id="display">0</div>
    <div class="display-status">
      <div class="status-mode" id="mode">ready</div>
      <div class="status-dot"></div>
    </div>
  </div>

  <div class="btn-grid">

    <!-- Row 1: functions -->
    <button class="btn btn-fn" onclick="calcSqrt()">√x</button>
    <button class="btn btn-fn" onclick="calcLog()">log</button>
    <button class="btn btn-fn" onclick="calcLn()">ln</button>
    <button class="btn btn-fn" onclick="insertPi()">π</button>

    <!-- Row 2: clear + ops -->
    <button class="btn btn-clr" onclick="clearAll()">AC</button>
    <button class="btn btn-bs" onclick="backspace()">⌫</button>
    <button class="btn btn-fn" onclick="calcPercent()">%</button>
    <button class="btn btn-op" onclick="inputOp('/')">÷</button>

    <!-- Row 3 -->
    <button class="btn btn-num" onclick="inputNum('7')">7</button>
    <button class="btn btn-num" onclick="inputNum('8')">8</button>
    <button class="btn btn-num" onclick="inputNum('9')">9</button>
    <button class="btn btn-op" onclick="inputOp('*')">×</button>

    <!-- Row 4 -->
    <button class="btn btn-num" onclick="inputNum('4')">4</button>
    <button class="btn btn-num" onclick="inputNum('5')">5</button>
    <button class="btn btn-num" onclick="inputNum('6')">6</button>
    <button class="btn btn-op" onclick="inputOp('-')">−</button>

    <!-- Row 5 -->
    <button class="btn btn-num" onclick="inputNum('1')">1</button>
    <button class="btn btn-num" onclick="inputNum('2')">2</button>
    <button class="btn btn-num" onclick="inputNum('3')">3</button>
    <button class="btn btn-op" onclick="inputOp('+')">+</button>

    <!-- Row 6 -->
    <button class="btn btn-num" onclick="inputNum('0')">0</button>
    <button class="btn btn-num" onclick="inputDot()">.</button>
    <button class="btn btn-eq span2" onclick="calculate()">=</button>

  </div>

  <div class="calc-footer">Analisis Real · Kalkulator Ilmiah</div>
</div>

<script>
  let current = '0';
  let stored = null;
  let operator = null;
  let justCalc = false;
  let expression = '';

  const display = document.getElementById('display');
  const exprEl  = document.getElementById('expr');
  const modeEl  = document.getElementById('mode');

  function updateDisplay(val) {
    let str = String(val);
    // shorten very long decimals
    if (!isNaN(parseFloat(str)) && str.includes('.') && !str.includes('e')) {
      let num = parseFloat(str);
      if (str.length > 12) str = parseFloat(num.toPrecision(10)).toString();
    }
    display.textContent = str;
    // shrink font for long numbers
    display.style.fontSize = str.length > 12 ? '20px' : str.length > 9 ? '26px' : '34px';
  }

  function setMode(txt) { modeEl.textContent = txt; }

  function inputNum(n) {
    if (justCalc) { current = n; expression = ''; justCalc = false; }
    else current = current === '0' ? n : current + n;
    updateDisplay(current);
    setMode('input');
  }

  function inputDot() {
    if (justCalc) { current = '0.'; justCalc = false; }
    if (!current.includes('.')) current += '.';
    updateDisplay(current);
  }

  function inputOp(op) {
    justCalc = false;
    if (stored !== null && operator) {
      let res = compute(stored, parseFloat(current), operator);
      stored = res;
      updateDisplay(res);
      expression = res + ' ' + opSymbol(op);
    } else {
      stored = parseFloat(current);
      expression = current + ' ' + opSymbol(op);
    }
    exprEl.textContent = expression;
    operator = op;
    current = '0';
    setMode('operator');
  }

  function opSymbol(op) {
    return { '+': '+', '-': '−', '*': '×', '/': '÷' }[op] || op;
  }

  function compute(a, b, op) {
    switch(op) {
      case '+': return a + b;
      case '-': return a - b;
      case '*': return a * b;
      case '/':
        if (b === 0) { setMode('error'); return 'Error: ÷0'; }
        return a / b;
    }
    return b;
  }

  function calculate() {
    if (stored === null || operator === null) return;
    let b = parseFloat(current);
    let exprFull = expression + ' ' + current;
    let res = compute(stored, b, operator);
    exprEl.textContent = exprFull + ' =';
    updateDisplay(res);
    current = String(res);
    stored = null; operator = null;
    justCalc = true;
    setMode('result');
  }

  function clearAll() {
    current = '0'; stored = null; operator = null; justCalc = false; expression = '';
    updateDisplay('0'); exprEl.textContent = ''; setMode('ready');
  }

  function backspace() {
    if (justCalc) { clearAll(); return; }
    current = current.length > 1 ? current.slice(0, -1) : '0';
    updateDisplay(current);
  }

  function calcSqrt() {
    let n = parseFloat(current);
    if (n < 0) { exprEl.textContent = '√(' + n + ')'; updateDisplay('Error: √<0'); setMode('error'); return; }
    let res = Math.sqrt(n);
    exprEl.textContent = '√(' + n + ') =';
    updateDisplay(res);
    current = String(res); justCalc = true;
    setMode('√ akar');
  }

  function calcLog() {
    let n = parseFloat(current);
    if (n <= 0) { updateDisplay('Error: log≤0'); setMode('error'); return; }
    let res = Math.log10(n);
    exprEl.textContent = 'log(' + n + ') =';
    updateDisplay(res);
    current = String(res); justCalc = true;
    setMode('log₁₀');
  }

  function calcLn() {
    let n = parseFloat(current);
    if (n <= 0) { updateDisplay('Error: ln≤0'); setMode('error'); return; }
    let res = Math.log(n);
    exprEl.textContent = 'ln(' + n + ') =';
    updateDisplay(res);
    current = String(res); justCalc = true;
    setMode('ln natural');
  }

  function insertPi() {
    current = String(Math.PI);
    updateDisplay(current);
    exprEl.textContent = 'π =';
    justCalc = false;
    setMode('π pi');
  }

  function calcPercent() {
    let n = parseFloat(current);
    let res = stored !== null ? stored * n / 100 : n / 100;
    exprEl.textContent = n + '% =';
    updateDisplay(res);
    current = String(res); justCalc = true;
    setMode('persen');
  }

  // keyboard support
  document.addEventListener('keydown', e => {
    if (e.key >= '0' && e.key <= '9') inputNum(e.key);
    else if (e.key === '.') inputDot();
    else if (e.key === '+') inputOp('+');
    else if (e.key === '-') inputOp('-');
    else if (e.key === '*') inputOp('*');
    else if (e.key === '/') { e.preventDefault(); inputOp('/'); }
    else if (e.key === 'Enter' || e.key === '=') calculate();
    else if (e.key === 'Backspace') backspace();
    else if (e.key === 'Escape') clearAll();
  });
</script>
</body>
</html>
    """
    st.components.v1.html(tulisanHTML1,height=650)
    st.subheader("C. Sifat Kelengkapan (Completness Property)")
    st.markdown("##### Ini adalah inti dari Analisis Real. Himpunan bilangan real R bersifat lengkap, artinya tidak ada 'lubang' dalam garis bilangan.Jika kita memiliki barisan desimal yang semakin panjang:")
    st.latex("x_{1}=0,a_{1}")
    st.latex("x_{2}=0,a_{1}a_{2}")
    st.latex("x_{3}=0,a_{1}a_{2}a_{3}")
    st.markdown("##### Maka barisan $x_{n}$ adalah barisan Cauchy yang konvergen ke suatu bilangan real 𝑥Hal ini tidak selalu terjadi di himpunan bilangan rasional 𝑄, karena limit dari barisan bilangan rasional bisa saja berupa bilangan irrasional.")
    tulisanHTML2 = """
    <iframe src=' https://martin-bernard26.github.io/simulasiCauchy/simulasi1.html' style="width:100%; height:1500px; border:none;">
    </iframe>
    """
    st.components.v1.html(tulisanHTML2,height=1500)
    st.subheader("Contoh dan Soal Penyelesaian")
    tulisanHTML3 = """
    <iframe src=' https://martin-bernard26.github.io/simulasiCauchy/contohsoal1.html' style="width:100%; height:1500px; border:none;">
    </iframe>
    """
    st.components.v1.html(tulisanHTML3,height=3000)
    tulisanHTML5 = """
    <iframe src=' https://martin-bernard26.github.io/simulasiCauchy/tugas.html' style="width:100%; height:1500px; border:none;">
    </iframe>
    """
    st.components.v1.html(tulisanHTML5,height=1000)

def materi2():
    bagian = st.tabs(['test diagnosa','Materi dan latihan','Referensi'])
    with bagian[0]:
        FORM_ACTION_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdFbLvcyZnwUAA-QezDIN589jKN1sLL_gr_afX1UuPc_HtZRw/formResponse"
 
        ENTRY = {
    "nama":       "entry.2079486621",   # Nama Lengkap
    "nim":        "entry.217329210",   # NIM / Kode Mahasiswa
    "waktu":      "entry.1575527149",   # Waktu pengerjaan (auto)
    "durasi":     "entry.1792382505",   # Durasi pengerjaan (auto)
    "j1":         "entry.446929005",   # Jawaban Soal 1
    "j2":         "entry.1883968956",
    "j3":         "entry.1057599819",
    "j4":         "entry.239741653",
    "j5":         "entry.2068907983",
    "j6":         "entry.1016098720",
    "j7":         "entry.604854740",
    "j8":         "entry.1414322124",
    "j9":         "entry.453948995",
    "j10":        "entry.1621436441",   # Jawaban Soal 10
}
 
# ─────────────────────────────────────────────
    # CSS KUSTOM — Estetika Academic Dark
    # ─────────────────────────────────────────────
        st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,300&family=JetBrains+Mono:wght@400;600&display=swap');
 
:root {
    --ink: #1a1208;
    --parchment: #f5efe0;
    --sienna: #8b3a0f;
    --gold: #c4922a;
    --gold-light: #e8c97a;
    --slate: #3d4f5c;
    --sage: #4a6741;
    --border: #c9b88a;
    --cream: #faf6ed;
}
 
/* Global */
html, body, [class*="css"] {
    font-family: 'Source Serif 4', Georgia, serif;
    color: var(--ink);
}
 
/* Header utama */
.main-header {
    background: #1a1208;
    border-radius: 10px;
    padding: 2rem 2rem 1.6rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.main-header::before {
    content: 'ℝ';
    position: absolute;
    right: 1.5rem; top: 50%;
    transform: translateY(-50%);
    font-size: 5rem;
    opacity: 0.06;
    font-family: 'Playfair Display', serif;
    color: #e8c97a;
    pointer-events: none;
}
.main-header .label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #e8c97a;
    opacity: 0.8;
    margin-bottom: 0.5rem;
}
.main-header h1 {
    font-family: 'Playfair Display', serif;
    font-size: 1.85rem;
    font-weight: 700;
    color: #f5efe0;
    line-height: 1.2;
    margin: 0;
}
.main-header .sub {
    font-size: 0.9rem;
    color: rgba(245,239,224,0.6);
    font-style: italic;
    margin-top: 0.4rem;
}
 
/* Card soal */
.soal-card {
    background: #faf6ed;
    border: 1.5px solid #c9b88a;
    border-left: 4px solid #8b3a0f;
    border-radius: 8px;
    padding: 1.2rem 1.4rem 0.8rem;
    margin-bottom: 1.2rem;
}
.soal-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #8b3a0f;
    margin-bottom: 0.4rem;
}
.soal-text {
    font-size: 1rem;
    line-height: 1.65;
    color: #1a1208;
    margin-bottom: 0.3rem;
}
.math-tag {
    font-family: 'JetBrains Mono', monospace;
    background: rgba(139,58,15,0.1);
    color: #7a2f08;
    padding: 0.12em 0.4em;
    border-radius: 3px;
    font-size: 0.9em;
}
 
/* Info box */
.info-box {
    background: #f0f5ff;
    border-left: 3px solid #1e3a5f;
    border-radius: 0 6px 6px 0;
    padding: 0.8rem 1rem;
    margin: 0.8rem 0;
    font-size: 0.88rem;
    color: #1e3a5f;
}
 
/* Progress */
.progress-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #3d4f5c;
    margin-bottom: 0.3rem;
    letter-spacing: 0.08em;
}
 
/* Footer */
.footer {
    text-align: center;
    font-size: 0.78rem;
    color: rgba(26,18,8,0.4);
    font-style: italic;
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid #c9b88a;
}
 
/* Streamlit tweaks */
div[data-testid="stRadio"] > label {
    font-family: 'Source Serif 4', serif;
    font-size: 0.95rem;
}
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    font-family: 'Source Serif 4', serif;
    font-size: 0.95rem;
}
.stButton > button {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-weight: 600;
    border-radius: 5px;
    transition: all 0.15s;
}
</style>
""", unsafe_allow_html=True)
 
# ─────────────────────────────────────────────
# BANK SOAL — 10 Soal Diagnosa
# type: 'pilihan' atau 'isian'
# ─────────────────────────────────────────────
        SOAL = [
            {
        "no": 1,
        "topik": "Sifat Aljabar — Aksioma Lapangan",
        "tipe": "pilihan",
        "pertanyaan": (
            "Manakah pernyataan berikut yang merupakan aksioma lapangan (field axiom) "
            "dari ℝ yang paling tepat mendeskripsikan sifat invers perkalian?"
        ),
        "pilihan": [
            "A. Untuk setiap a ∈ ℝ, terdapat (−a) ∈ ℝ sehingga a + (−a) = 0",
            "B. Untuk setiap a ∈ ℝ dengan a ≠ 0, terdapat a⁻¹ ∈ ℝ sehingga a · a⁻¹ = 1",
            "C. Untuk setiap a, b ∈ ℝ, berlaku a · b = b · a",
            "D. Terdapat 1 ∈ ℝ sedemikian sehingga a · 1 = a untuk semua a ∈ ℝ",
        ],
    },
    {
        "no": 2,
        "topik": "Sifat Aljabar — Teorema Turunan",
        "tipe": "pilihan",
        "pertanyaan": (
            "Pernyataan berikut dapat dibuktikan dari aksioma lapangan. "
            "Manakah langkah pembuktian yang tepat untuk menunjukkan bahwa a · 0 = 0 untuk semua a ∈ ℝ?"
        ),
        "pilihan": [
            "A. Gunakan langsung aksioma identitas perkalian M4 karena 0 adalah identitas",
            "B. Tulis 0 = 0 + 0, distribusikan: a·0 = a·(0+0) = a·0 + a·0, lalu gunakan hukum pembatalan",
            "C. Karena 0 adalah elemen paling kecil di ℝ, maka perkalian dengan 0 selalu menghasilkan 0",
            "D. Gunakan aksioma O3 (tertutup terhadap perkalian) pada bilangan positif",
        ],
    },
    {
        "no": 3,
        "topik": "Sifat Aljabar — Sifat Distributif",
        "tipe": "pilihan",
        "pertanyaan": (
            "Seorang mahasiswa ingin membuktikan bahwa −(a + b) = (−a) + (−b) untuk semua a, b ∈ ℝ. "
            "Strategi pembuktian yang paling tepat adalah…"
        ),
        "pilihan": [
            "A. Tunjukkan bahwa (−a) + (−b) memenuhi definisi invers penjumlahan dari (a + b), yaitu (a+b) + ((−a)+(−b)) = 0",
            "B. Langsung substitusi nilai numerik untuk memeriksa kebenarannya",
            "C. Gunakan aksioma trikotomi karena semua kasus tanda sudah tercakup",
            "D. Kalikan kedua ruas dengan (−1) lalu gunakan aksioma komutatif",
        ],
    },
    {
        "no": 4,
        "topik": "Sifat Aljabar — Tidak Ada Pembagi Nol",
        "tipe": "pilihan",
        "pertanyaan": (
            "Misalkan a, b ∈ ℝ dan diketahui a · b = 0. "
            "Pernyataan manakah yang pasti benar berdasarkan teorema lapangan?"
        ),
        "pilihan": [
            "A. a = 0 dan b = 0 (keduanya harus nol)",
            "B. a = 0 atau b = 0 (paling sedikit satu di antara keduanya nol)",
            "C. a · b = 0 hanya mungkin jika a = b",
            "D. Tidak dapat disimpulkan apapun tanpa informasi tambahan",
        ],
    },
    {
        "no": 5,
        "topik": "Sifat Urutan — Aksioma & Trikotomi",
        "tipe": "pilihan",
        "pertanyaan": (
            "Aksioma trikotomi pada bilangan real menyatakan bahwa untuk setiap a, b ∈ ℝ, "
            "tepat satu dari kondisi berikut berlaku. Kondisi tersebut adalah…"
        ),
        "pilihan": [
            "A. a < b,  a ≤ b,  atau  a ≥ b",
            "B. a < b,  a = b,  atau  a > b",
            "C. a ≤ b  atau  a > b  (dua kemungkinan)",
            "D. a + b > 0,  a + b = 0,  atau  a + b < 0",
        ],
    },
    {
        "no": 6,
        "topik": "Sifat Urutan — Perkalian Bilangan Negatif",
        "tipe": "pilihan",
        "pertanyaan": (
            "Diketahui a < b dan c < 0. Berdasarkan sifat urutan lapangan terurut, "
            "manakah pernyataan yang benar?"
        ),
        "pilihan": [
            "A. ac < bc  (tanda urutan tetap saat dikali c negatif)",
            "B. ac > bc  (tanda urutan berbalik saat dikali bilangan negatif)",
            "C. ac = bc  (perkalian dengan nilai sama menghasilkan nilai sama)",
            "D. Tidak ada hubungan urutan yang dapat disimpulkan",
        ],
    },
    {
        "no": 7,
        "topik": "Sifat Urutan — Kuadrat Non-negatif",
        "tipe": "pilihan",
        "pertanyaan": (
            "Dari aksioma urutan bilangan real, dapat dibuktikan bahwa a² ≥ 0 untuk semua a ∈ ℝ. "
            "Konsekuensi langsung dari teorema ini adalah…"
        ),
        "pilihan": [
            "A. Bilangan negatif tidak memiliki akar kuadrat di ℝ  (karena a² ≥ 0 selalu)",
            "B. Setiap bilangan real adalah bilangan kuadrat",
            "C. Kuadrat dua bilangan yang berbeda selalu berbeda",
            "D. Perkalian dua bilangan negatif adalah negatif",
        ],
    },
    {
        "no": 8,
        "topik": "Nilai Mutlak — Ketaksamaan Segitiga",
        "tipe": "pilihan",
        "pertanyaan": (
            "Ketaksamaan segitiga menyatakan |a + b| ≤ |a| + |b| untuk semua a, b ∈ ℝ. "
            "Kapan kesamaan |a + b| = |a| + |b| berlaku?"
        ),
        "pilihan": [
            "A. Selalu berlaku untuk semua a, b ∈ ℝ",
            "B. Ketika a = b",
            "C. Ketika a · b ≥ 0  (a dan b bertanda sama atau salah satunya nol)",
            "D. Ketika a dan b keduanya bilangan bulat",
        ],
    },
    {
        "no": 9,
        "topik": "Sifat Urutan — Densitas ℝ",
        "tipe": "isian",
        "pertanyaan": (
            "Teorema densitas bilangan real menyatakan: jika a < b, maka terdapat c ∈ ℝ "
            "dengan a < c < b. Sebutkan satu konstruksi eksplisit nilai c tersebut "
            "(nyatakan dalam a dan b) dan jelaskan secara singkat mengapa c memenuhi a < c < b!"
        ),
    },
    {
        "no": 10,
        "topik": "Sifat Aljabar & Urutan — Analisis Mendalam",
        "tipe": "isian",
        "pertanyaan": (
            "Diketahui a ∈ ℝ dengan 0 < a < 1. "
            "Buktikan atau jelaskan mengapa a² < a dengan menggunakan sifat urutan "
            "(sebutkan aksioma atau sifat urutan yang Anda gunakan pada setiap langkah)!"
        ),
    },
]
 
# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
        if "halaman" not in st.session_state:
            st.session_state.halaman = "identitas"
        if "waktu_mulai" not in st.session_state:
            st.session_state.waktu_mulai = None
        if "jawaban" not in st.session_state:
            st.session_state.jawaban = {}
        if "submitted" not in st.session_state:
            st.session_state.submitted = False
 
# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
        st.markdown("""
<div class="main-header">
  <div class="label">Analisis Real · Tes Diagnosa</div>
  <h1>Sifat Aljabar &amp; Sifat Urutan</h1>
  <div class="sub">10 Soal Pilihan Ganda &amp; Isian · Tanpa Kunci Jawaban</div>
</div>
        """, unsafe_allow_html=True)
 
# ─────────────────────────────────────────────
# HALAMAN 1 — IDENTITAS MAHASISWA
# ─────────────────────────────────────────────
        if st.session_state.halaman == "identitas":
            st.markdown("### 📋 Identitas Mahasiswa")
            st.markdown("""
    <div class="info-box">
    Tes ini terdiri atas <strong>8 soal pilihan ganda</strong> dan <strong>2 soal isian singkat</strong>.
    Kerjakan secara mandiri. Hasil akan dikirim otomatis ke sistem dosen setelah Anda menekan <em>Kirim Jawaban</em>.
    </div>
    """, unsafe_allow_html=True)
 
            with st.form("form_identitas"):
                nama = st.text_input("Nama Lengkap *", placeholder="Contoh: Martin Bernard")
                nim  = st.text_input("NIM / Kode Mahasiswa *", placeholder="Contoh: 2201234567")
                setuju = st.checkbox("Saya menyatakan akan mengerjakan tes ini secara jujur dan mandiri.")
                mulai  = st.form_submit_button("▶  Mulai Tes", use_container_width=True)
 
                if mulai:
                    if not nama.strip():
                        st.error("⚠️ Nama lengkap wajib diisi.")
                    elif not nim.strip():
                        st.error("⚠️ NIM wajib diisi.")
                    elif not setuju:
                        st.error("⚠️ Anda harus menyetujui pernyataan kejujuran akademik.")
                    else:
                        st.session_state.nama = nama.strip()
                        st.session_state.nim  = nim.strip()
                        st.session_state.waktu_mulai = datetime.now()
                        st.session_state.halaman = "tes"
                        st.rerun()
 
# ─────────────────────────────────────────────
# HALAMAN 2 — SOAL TES
# ─────────────────────────────────────────────
        elif st.session_state.halaman == "tes" and not st.session_state.submitted:
 
            # Progress
            dijawab = len(st.session_state.jawaban)
            pct = int(dijawab / len(SOAL) * 100)
            st.markdown(f'<div class="progress-label">Progress: {dijawab}/{len(SOAL)} soal dijawab ({pct}%)</div>', unsafe_allow_html=True)
            st.progress(pct / 100)
 
            st.markdown(f"""
            <div style="font-size:0.85rem; color:#3d4f5c; margin-bottom:1.2rem; font-family:'JetBrains Mono',monospace;">
            Peserta: <strong>{st.session_state.nama}</strong> &nbsp;|&nbsp; NIM: <strong>{st.session_state.nim}</strong>
            </div>
            """, unsafe_allow_html=True)
 
            st.markdown("---")
 
            # Render setiap soal
            for s in SOAL:
                no  = s["no"]
                key = f"j{no}"
 
                st.markdown(f"""
                <div class="soal-card">
                  <div class="soal-num">Soal {no} &mdash; {s['topik']}</div>
                  <div class="soal-text">{s['pertanyaan']}</div>
                </div>
                """, unsafe_allow_html=True)
 
                if s["tipe"] == "pilihan":
                    default_idx = None
                    if key in st.session_state.jawaban:
                        try:
                            default_idx = s["pilihan"].index(st.session_state.jawaban[key])
                        except ValueError:
                            default_idx = None
 
                    jawaban = st.radio(
                        label=f"Pilih jawaban untuk Soal {no}:",
                        options=s["pilihan"],
                        index=default_idx,
                        key=f"radio_{no}",
                        label_visibility="collapsed",
                    )
                    if jawaban:
                            st.session_state.jawaban[key] = jawaban
 
                else:  # isian
                    default_val = st.session_state.jawaban.get(key, "")
                    jawaban = st.text_area(
                        label=f"Jawaban Soal {no}:",
                        value=default_val,
                        height=140,
                        key=f"text_{no}",
                        placeholder="Tuliskan jawaban dan penjelasan Anda di sini…",
                        label_visibility="collapsed",
                    )
                    if jawaban.strip():
                        st.session_state.jawaban[key] = jawaban.strip()
 
                st.markdown("<div style='margin-bottom:0.5rem'></div>", unsafe_allow_html=True)
 
            # Tombol kirim
            st.markdown("---")
            belum_dijawab = [s["no"] for s in SOAL if f"j{s['no']}" not in st.session_state.jawaban or not st.session_state.jawaban.get(f"j{s['no']}")]
 
            if belum_dijawab:
                st.warning(f"⚠️ Soal yang belum dijawab: {', '.join(map(str, belum_dijawab))}")
 
            col1, col2 = st.columns([3, 1])
            with col1:
                kirim = st.button(
                    "✉  Kirim Jawaban ke Google Forms",
                    use_container_width=True,
                    type="primary",
                    disabled=bool(belum_dijawab),
                )
            with col2:
                reset = st.button("↺  Reset", use_container_width=True)
 
            if reset:
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
 
            if kirim and not belum_dijawab:
                # Hitung durasi
                selesai = datetime.now()
                durasi_detik = int((selesai - st.session_state.waktu_mulai).total_seconds())
                menit = durasi_detik // 60
                detik = durasi_detik % 60
 
                # Susun payload Google Forms
                payload = {
                    ENTRY["nama"]:   st.session_state.nama,
                    ENTRY["nim"]:    st.session_state.nim,
                    ENTRY["waktu"]:  selesai.strftime("%Y-%m-%d %H:%M:%S"),
                    ENTRY["durasi"]: f"{menit} menit {detik} detik",
                }
                for s in SOAL:
                    key = f"j{s['no']}"
                    entry_key = ENTRY.get(key, "")
                    if entry_key:
                        payload[entry_key] = st.session_state.jawaban.get(key, "(tidak dijawab)")
 
                # Kirim ke Google Forms
                with st.spinner("Mengirim jawaban ke server…"):
                    try:
                        resp = requests.post(
                            FORM_ACTION_URL,
                            data=payload,
                            timeout=10,
                            headers={"Content-Type": "application/x-www-form-urlencoded"},
                        )
                        kirim_berhasil = resp.status_code in [200, 302]
                    except Exception as e:
                        kirim_berhasil = False
                        st.session_state.error_msg = str(e)
 
                st.session_state.durasi_str = f"{menit} menit {detik} detik"
                st.session_state.kirim_berhasil = kirim_berhasil
                st.session_state.submitted = True
                st.rerun()
 
# ─────────────────────────────────────────────
# HALAMAN 3 — KONFIRMASI PENGIRIMAN
# ─────────────────────────────────────────────
        elif st.session_state.submitted:
            berhasil = st.session_state.get("kirim_berhasil", False)
 
            if berhasil:
                st.success("✅ Jawaban berhasil dikirim ke Google Forms!")
                st.balloons()
            else:
                st.warning("⚠️ Pengiriman ke Google Forms gagal atau URL Form belum dikonfigurasi.")
                st.markdown("""
        <div class="info-box">
        <strong>Untuk instruktur:</strong> Pastikan <code>FORM_ACTION_URL</code> dan semua <code>ENTRY</code>
        sudah diisi dengan benar dari Google Forms Anda.
        Lihat bagian konfigurasi di bagian atas kode.
        </div>
        """, unsafe_allow_html=True)
 
            st.markdown(f"""
    <div style="background:#faf6ed;border:1.5px solid #c9b88a;border-radius:8px;padding:1.3rem 1.5rem;margin:1.2rem 0;">
      <div style="font-family:'JetBrains Mono',monospace;font-size:0.7rem;letter-spacing:0.15em;text-transform:uppercase;color:#8b3a0f;margin-bottom:0.6rem;">Ringkasan Pengerjaan</div>
      <table style="width:100%;font-size:0.9rem;border-collapse:collapse;">
        <tr><td style="padding:0.3rem 0;color:#3d4f5c;">Nama</td><td><strong>{st.session_state.nama}</strong></td></tr>
        <tr><td style="padding:0.3rem 0;color:#3d4f5c;">NIM</td><td><strong>{st.session_state.nim}</strong></td></tr>
        <tr><td style="padding:0.3rem 0;color:#3d4f5c;">Waktu Selesai</td><td><strong>{datetime.now().strftime('%d %B %Y, %H:%M')}</strong></td></tr>
        <tr><td style="padding:0.3rem 0;color:#3d4f5c;">Durasi</td><td><strong>{st.session_state.get('durasi_str', '—')}</strong></td></tr>
        <tr><td style="padding:0.3rem 0;color:#3d4f5c;">Soal Dijawab</td><td><strong>{len(st.session_state.jawaban)} / {len(SOAL)}</strong></td></tr>
      </table>
    </div>
    """, unsafe_allow_html=True)
 
            st.markdown("""
    <div class="info-box">
    Jawaban Anda telah tercatat. Hasil evaluasi akan disampaikan oleh dosen pada sesi berikutnya.
    Tidak ada kunci jawaban yang ditampilkan di sini.
    </div>
    """, unsafe_allow_html=True)
 
            if st.button("↺  Mulai Ulang (Peserta Baru)", use_container_width=True):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
 
# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
        st.markdown("""
<div class="footer">
  Tes Diagnosa Analisis Real &mdash; Sifat Aljabar &amp; Sifat Urutan<br>
  Dikembangkan untuk keperluan pembelajaran · Referensi: Bartle &amp; Sherbert, <em>Introduction to Real Analysis</em>, 4th ed.
</div>
""", unsafe_allow_html=True)
        with bagian[1]:
            tulisanHTML6 = """
        <iframe src=' https://martin-bernard26.github.io/simulasiCauchy/analisisReal2.html' style="width:100%; height:1500px; border:none;">
        </iframe>
           """
            st.components.v1.html(tulisanHTML6,height=1000)
            with st.expander("Forum Diskusi"):
                # URL Firebase Realtime Database
                FIREBASE_URL = "https://vba-modul-diskusi-default-rtdb.firebaseio.com/chat1.json"

                st.title("💬 Chatbot Firebase + Streamlit")

                # session chat
                if "messages" not in st.session_state:
                    st.session_state.messages = []

                # fungsi kirim pesan ke firebase
                def send_message(user, text):
                    data = {
                        "user": user,
                        "message": text,
                        "time": time.time()
                    }

                    requests.post(FIREBASE_URL, json=data)


                # fungsi ambil pesan
                def get_messages():

                    response = requests.get(FIREBASE_URL)

                    if response.status_code == 200 and response.json() != None:
                        data = response.json()
                        return list(data.values())

                    return []


                # input nama
                username = st.text_input("Nama Anda")

                # tampilkan pesan
                messages = get_messages()

                for msg in messages:
                    st.write(f"**{msg['user']}** : {msg['message']}")

                # input chat
                chat = st.text_input("Tulis pesan")
                if st.button("Kirim"):
                    if username and chat:
                        send_message(username, chat)
                        st.rerun()
            st.markdown("---")
            tulisanHTML11 = """
        <iframe src=' https://martin-bernard26.github.io/simulasiCauchy/tulisan.html' style="width:100%; height:1500px; border:none;">
        </iframe>
           """
            st.components.v1.html(tulisanHTML11,height=1000)
        with bagian[2]:
            pdf_display = '<iframe src="https://drive.google.com/file/d/1qZ_Fu1jbqxo9_xx38G2u2CxflpoPP4NQ/preview" width="100%" height="800px" allow="autoplay"></iframe>'
    
            # Menampilkan ke Streamlit
            st.markdown(pdf_display, unsafe_allow_html=True)

def hasilnya():
    st.title("Upload Jawaban Tulisan Tangan")
    nama = st.text_input("Nama")
    nim = st.text_input("NIM")

    foto = st.camera_input("Foto Jawaban")

    if st.button("Upload"):

        if foto is not None:

            url = "https://api.cloudinary.com/v1_1/ikip-siliwangi/image/upload"

            files = {"file": foto.getvalue()}

            data = {
                "upload_preset": "upload_jawaban",
                "public_id": f"{nama}_{nim}"
            }

            response = requests.post(url, files=files, data=data)

            result = response.json()

            if "secure_url" in result:
                st.success("Upload berhasil")
                st.write(result["secure_url"])
            else:
                st.error("Upload gagal")
                st.write(result)
def materi3():
    menu1 = st.tabs(['Test Diagnosa','Materi','Latihan','catatan (Aksioma Peano)','praktek koding'])
    with menu1[1]:
        tulisanHTML8 = """
        <iframe src=' https://martin-bernard26.github.io/simulasiCauchy/pertemuan3.html' style="width:100%; height:1500px; border:none;">
        </iframe>
           """
        st.components.v1.html(tulisanHTML8,height=2000)
    with menu1[0]:
        tulisanHTML7 = """
        <iframe src='https://martin-bernard26.github.io/simulasiCauchy/testDiag3.html' style="width:100%; height:1500px; border:none;">
        </iframe>
           """
        st.components.v1.html(tulisanHTML7,height=2000)
    with menu1[2]:
        tulisanHTML9 = """
        <iframe src='https://martin-bernard26.github.io/simulasiCauchy/latihanAkar.html' style="width:100%; height:1500px; border:none;">
        </iframe>
           """
        st.components.v1.html(tulisanHTML9,height=2000)
        st.markdown("---")
        tulisanHTML11 = """
        <iframe src='https://martin-bernard26.github.io/simulasiCauchy/tulisan.html' style="width:100%; height:1500px; border:none;">
        </iframe>
           """
        st.components.v1.html(tulisanHTML11,height=2000)
    with menu1[3]:
        st.markdown("""
### Mengapa $1 + 1 = 2$ dalam Analisis Riil?

Dalam analisis riil dan sistem bilangan formal, pernyataan $1 + 1 = 2$ bukanlah sekadar asumsi umum, melainkan hasil logis yang diturunkan dari **Aksioma Peano**.

#### 1. Definisi Dasar (Penerus)
Dalam sistem ini, setiap bilangan asli memiliki "penerus" (*successor*), yang dilambangkan dengan $S(n)$. Secara definisi:
*   $2$ adalah penerus dari $1$, sehingga: **$2 = S(1)$**.

#### 2. Aturan Penjumlahan
Operasi penjumlahan didefinisikan secara rekursif. Salah satu aturan dasarnya adalah:
*   $a + S(b) = S(a + b)$

#### 3. Langkah Pembuktian
Untuk membuktikan $1 + 1 = 2$, kita substitusikan nilai-nilainya:

1.  Kita tahu bahwa $1$ adalah penerus dari $0$, atau bisa ditulis $1 = S(0)$.
2.  Maka, $1 + 1$ dapat ditulis sebagai $1 + S(0)$.
3.  Menggunakan aturan penjumlahan di atas:
    $$1 + S(0) = S(1 + 0)$$
4.  Karena bilangan apa pun ditambah $0$ adalah bilangan itu sendiri ($1 + 0 = 1$), maka:
    $$S(1 + 0) = S(1)$$
5.  Karena secara definisi $S(1) = 2$, maka:
    **$1 + 1 = 2$**

### Kesimpulan
Secara matematis, $1 + 1 = 2$ adalah benar karena **2 didefinisikan sebagai simbol untuk penerus dari bilangan 1** dalam urutan logis bilangan asli.

        """)
    with menu1[4]:
        tulisanHTML12 = """
        <iframe src="https://trinket.io/embed/python3/055c60f8a0" width="100%" height="1000" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
           """
        st.components.v1.html(tulisanHTML12,height=5000)

def pendapat():
    menu2 = st.tabs(['Archimedian','Bernouli'])
    with menu2[0]:
        st.markdown('''
        ### Sifat Archimedes (Archimedean Property)

Sifat ini merupakan salah satu pilar penting dalam analisis riil yang menghubungkan bilangan asli dengan bilangan riil.

#### 1. Pernyataan Formal
Untuk setiap bilangan riil $x \in \mathbb{R}$, selalu terdapat bilangan asli $n \in \mathbb{N}$ sedemikian sehingga:
$$n > x$$

#### 2. Bentuk Alternatif (Versi "Kecil")
Sifat ini juga sering dinyatakan untuk menunjukkan adanya bilangan yang sangat kecil:
Untuk setiap $\\varepsilon > 0$ (sekecil apa pun), selalu terdapat $n \in \mathbb{N}$ sedemikian sehingga:
$$\\frac{1}{n} < \\varepsilon$$

#### 3. Mengapa Ini Penting?
Tanpa sifat ini, struktur matematika kita akan berbeda. Sifat Archimedes menjamin bahwa:
*   **Tidak ada bilangan riil terbesar:** Sebesar apa pun angka yang kamu bayangkan, kamu selalu bisa menambahkannya dengan 1.
*   **Kekonvergenan:** Kita bisa membuktikan bahwa limit dari $\\frac{1}{n}$ adalah $0$ saat $n$ menuju tak hingga.
*   **Kerapatan Bilangan Rasional:** Sifat ini digunakan untuk membuktikan bahwa di antara dua bilangan riil sembarang, selalu ada bilangan rasional (Sifat Kerapatan).

#### 4. Inti Analisis
Sifat ini sebenarnya adalah konsekuensi dari **Sifat Kelengkapan** (*Completeness Property*) dari bilangan riil. Jika $\mathbb{N}$ memiliki batas atas, maka ia
harus memiliki *Supremum* (batas atas terkecil). Namun, dalam sistem bilangan riil, kita bisa membuktikan bahwa asumsi adanya batas atas untuk $\mathbb{N}$ akan
berujung pada kontradiksi.
        ''')
    with menu2[1]:
        st.markdown('''
        # Analisis Real: Ketaksamaan Bernoulli

Dalam analisis real, **Ketaksamaan Bernoulli** adalah instrumen fundamental yang digunakan untuk memberikan estimasi batas bawah dari perpangkatan bentuk $(1+x)$. Teorema ini sangat krusial dalam membuktikan kekonvergenan barisan dan sifat-sifat fungsi eksponensial.

---

### 1. Pernyataan Teorema
Untuk setiap bilangan riil $x > -1$ dan setiap bilangan asli $n \in \mathbb{N}$, berlaku:

$$(1 + x)^n \geq 1 + nx$$

### 2. Analisis Kondisi
*   **Kasus $x = 0$:** Kedua ruas bernilai $1$, sehingga terjadi kesamaan (ekualitas).
*   **Kasus $n = 1$:** Kedua ruas bernilai $1+x$, sehingga terjadi kesamaan.
*   **Ketaksamaan Ketat:** Jika $x \\neq 0$ dan $n > 1$, maka berlaku $(1 + x)^n > 1 + nx$.
*   **Batasan $x > -1$:** Syarat ini wajib dipenuhi agar $(1+x)$ selalu bernilai positif, sehingga tanda ketaksamaan tidak berbalik saat dilakukan operasi perkalian dalam pembuktian.

---

### 3. Pembuktian (Metode Induksi Matematika)

**Langkah Basis:**
Untuk $n = 1$:
$(1 + x)^1 \geq 1 + (1)x \implies 1 + x \geq 1 + x$ (Pernyataan benar).

**Langkah Induksi:**
Asumsikan pernyataan benar untuk $n = k$, yaitu:
$$(1 + x)^k \geq 1 + kx$$

Kita harus membuktikan bahwa pernyataan juga benar untuk $n = k + 1$. Kalikan kedua ruas dengan $(1 + x)$. Karena $x > -1$, maka $(1 + x) > 0$:

$$(1 + x)^k \cdot (1 + x) \geq (1 + kx) \cdot (1 + x)$$
$$(1 + x)^{k+1} \geq 1 + x + kx + kx^2$$
$$(1 + x)^{k+1} \geq 1 + (k + 1)x + kx^2$$

Karena $kx^2 \geq 0$ untuk semua $k \in \mathbb{N}$ dan $x \in \mathbb{R}$, maka:
$$1 + (k + 1)x + kx^2 \geq 1 + (k + 1)x$$

Berdasarkan sifat transitif, maka:
$$(1 + x)^{k+1} \geq 1 + (k + 1)x$$
**Q.E.D.**

---

### 4. Relevansi dalam Analisis Real

Ketaksamaan ini bukan sekadar angka, melainkan "jembatan" untuk membuktikan konsep-konsep limit yang lebih kompleks:

1.  **Limit Barisan Geometri:** Digunakan untuk membuktikan bahwa $\lim_{n \to \infty} r^n = 0$ jika $|r| < 1$.
2.  **Definisi Bilangan $e$:** Membantu menunjukkan bahwa barisan $a_{n} = (1 + \\frac{1}{n})^n$ adalah barisan yang monoton naik dan terbatas.
3.  **Kekonvergenan:** Memberikan cara cepat untuk membandingkan barisan eksponensial dengan barisan linier yang lebih sederhana.
        ''')

def materi4():
    menu1 = st.tabs(["Test Awal","Materi","Latihan","Tugas"])
    with menu1[1]:
        tulisanHTML1 = """
        <iframe src="https://martin-bernard26.github.io/simulasiCauchy/pertemuan5.html" width="100%" height="1000" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
           """
        st.components.v1.html(tulisanHTML1,height=1000)
        st.write("<h4>Media Geogebra<h4>",unsafe_allow_html=True)
        tulisanHTML = """
        <iframe src="https://martin-bernard26.github.io/simulasiCauchy/geogebra.html" width="100%" height="1000" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
           """
        st.components.v1.html(tulisanHTML,height=1000)
    with menu1[0]:
        tulisanHTML = """
        <iframe src="https://martin-bernard26.github.io/simulasiCauchy/testAwal4.html" width="100%" height="1000" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
           """
        st.components.v1.html(tulisanHTML,height=5000)
        st.write("<h4>Media Geogebra<h4>",unsafe_allow_html=True)
        
    with menu1[2]:
        tulisanHTML = """
        <iframe src="https://martin-bernard26.github.io/simulasiCauchy/latihan4.html" width="100%" height="1000" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
           """
        st.components.v1.html(tulisanHTML,height=1000)
        st.write("<h4>Media Geogebra<h4>",unsafe_allow_html=True)
        tulisanHTML2 = """
        <iframe src="https://martin-bernard26.github.io/simulasiCauchy/geogebra.html" width="100%" height="1000" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
           """
        st.components.v1.html(tulisanHTML2,height=1000)
    with menu1[3]:
        tulisanHTML = """
        <iframe src="https://martin-bernard26.github.io/simulasiCauchy/soal4.html" width="100%" height="1000" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
           """
        st.components.v1.html(tulisanHTML,height=1000)
        st.write("<h4>Kirimkan Tugas<h4>",unsafe_allow_html=True)
        tulisanHTML2 = """
        <iframe src="https://martin-bernard26.github.io/simulasiCauchy/postest4.html" width="100%" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
           """
        st.components.v1.html(tulisanHTML2,height=500)
#==========Materi++++++

if st.session_state['kumpulan']['pendahuluan']:
    kover()
if st.session_state['kumpulan']['pertemuan1']:
    materi1()
if st.session_state['kumpulan']['pertemuan2']:
    materi2()
if st.session_state['kumpulan']['pertemuan3']:
    materi3()
if st.session_state['kumpulan']['hasil']:
    hasilnya()
if st.session_state['kumpulan']['catatan']:
    pendapat()
if st.session_state['kumpulan']['pertemuan4']:
    materi4()
#===========Kontrol++++++

if st.sidebar.button("Pendahuluan"):
    st.session_state['kumpulan'] = {'pendahuluan':True,'catatan':False,'hasil':False,'pertemuan1':False,
                        'pertemuan2':False,'pertemuan3':False,'pertemuan4':False, 'pertemuan5':False}
    st.rerun()
if st.sidebar.button("Catatan Penting"):
    st.session_state['kumpulan'] = {'pendahuluan':False,'catatan':True,'hasil':False,'pertemuan1':False,
                        'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,'pertemuan5':False}
    st.rerun()
st.sidebar.markdown("---")
if st.sidebar.button("Pertemuan 1"):
    st.session_state['kumpulan'] = {'pendahuluan':False,'catatan':False,'hasil':False,'pertemuan1':True,
                        'pertemuan2':False,'pertemuan3':False, 'pertemuan4':False,'pertemuan5':False}
    st.rerun()
if st.sidebar.button("Pertemuan 2"):
    st.session_state['kumpulan'] = {'pendahuluan':False,'catatan':False,'hasil':False,'pertemuan1':False,
                        'pertemuan2':True,'pertemuan3':False, 'pertemuan4':False,'pertemuan5':False}
    st.rerun()
if st.sidebar.button("Pertemuan 3"):
    st.session_state['kumpulan'] = {'pendahuluan':False,'catatan':False,'hasil':False,'pertemuan1':False,
                        'pertemuan2':False,'pertemuan3':True, 'pertemuan4':False,'pertemuan5':False}
    st.rerun()
if st.sidebar.button("Pertemuan 4"):
    st.session_state['kumpulan'] = {'pendahuluan':False,'catatan':False,'hasil':False,'pertemuan1':False,
                        'pertemuan2':False,'pertemuan3':False, 'pertemuan4':True,'pertemuan5':False}
    st.rerun()
st.sidebar.markdown("---")
if st.sidebar.button("Upload file hasil"):
    st.session_state['kumpulan'] = {'pendahuluan':False,'catatan':False,'hasil':True,'pertemuan1':False,
                        'pertemuan2':False,'pertemuan3':False, 'pertemuan4':False,'pertemuan5':False}
    st.rerun()
