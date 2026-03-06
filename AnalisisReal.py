import streamlit as st


st.set_page_config(layout="wide")
if 'kumpulan' not in st.session_state:
    st.session_state['kumpulan'] = {'pendahuluan':True,'pertemuan1':False,
                        'pertemuan2':False,'pertemuan3':False}

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
    width: 794px;
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
#==========Materi++++++

if st.session_state['kumpulan']['pendahuluan']:
    kover()
if st.session_state['kumpulan']['pertemuan1']:
    materi1()


#===========Kontrol++++++

if st.sidebar.button("Pendahuluan"):
    st.session_state['kumpulan'] = {'pendahuluan':True,'pertemuan1':False,
                        'pertemuan2':False,'pertemuan3':False}
    st.rerun()

if st.sidebar.button("Pertemuan 1"):
    st.session_state['kumpulan'] = {'pendahuluan':False,'pertemuan1':True,
                        'pertemuan2':False,'pertemuan3':False}
    st.rerun()
