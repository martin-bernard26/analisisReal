<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Barisan Cauchy & Divergensi Sejati | Analisis Real</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --ink:      #0F1B2D;
    --ink-soft: #1E3048;
    --cream:    #F8F5EE;
    --cream-dk: #EDE9DF;
    --gold:     #C9A84C;
    --gold-lt:  #E2C97E;
    --blue:     #4A9ECA;
    --blue-dk:  #2D6E96;
    --red:      #B84C3A;
    --green:    #3A7D5A;
    --text:     #1A1A2E;
    --muted:    #6B7280;
    --border:   #D4C9B0;
    --shadow:   rgba(15,27,45,0.12);
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html { scroll-behavior: smooth; }

  body {
    font-family: 'Lora', Georgia, serif;
    background: var(--cream);
    color: var(--text);
    font-size: 16px;
    line-height: 1.75;
  }

  /* ── NAVIGATION ── */
  nav {
    position: sticky; top: 0; z-index: 100;
    background: var(--ink);
    border-bottom: 3px solid var(--gold);
    padding: 0 1.5rem;
    display: flex; align-items: center; gap: 1rem;
    height: 56px;
    box-shadow: 0 2px 12px var(--shadow);
  }
  nav .nav-brand {
    font-family: 'Cinzel', serif;
    color: var(--gold);
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    white-space: nowrap;
  }
  nav .nav-links {
    display: flex; gap: 0.25rem; margin-left: auto; list-style: none; flex-wrap: wrap;
  }
  nav .nav-links a {
    color: #CBD5E1;
    text-decoration: none;
    font-size: 0.75rem;
    padding: 0.3rem 0.6rem;
    border-radius: 4px;
    transition: all 0.2s;
    font-family: 'Lora', serif;
  }
  nav .nav-links a:hover { background: rgba(201,168,76,0.2); color: var(--gold-lt); }

  /* ── HERO ── */
  .hero {
    background: linear-gradient(135deg, var(--ink) 0%, var(--ink-soft) 60%, #1A3A5C 100%);
    color: white;
    padding: 4rem 2rem 3.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(74,158,202,0.15), transparent);
    pointer-events: none;
  }
  .hero-eyebrow {
    font-family: 'Cinzel', serif;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 1rem;
  }
  .hero h1 {
    font-family: 'Cinzel', serif;
    font-size: clamp(1.8rem, 4vw, 3rem);
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 0.5rem;
  }
  .hero h1 span { color: var(--gold-lt); }
  .hero-subtitle {
    color: #94A3B8;
    font-size: 0.95rem;
    margin-top: 1rem;
    font-style: italic;
  }
  .hero-meta {
    margin-top: 1.75rem;
    display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;
  }
  .hero-meta-item {
    text-align: center;
  }
  .hero-meta-item .val {
    display: block;
    font-family: 'Cinzel', serif;
    font-size: 1.4rem;
    color: var(--gold-lt);
    font-weight: 600;
  }
  .hero-meta-item .lbl {
    font-size: 0.7rem;
    color: #94A3B8;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }
  .hero-divider {
    width: 60px; height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 1.5rem auto 0;
  }
  .author-badge {
    margin-top: 1.5rem;
    display: inline-block;
    background: rgba(201,168,76,0.15);
    border: 1px solid rgba(201,168,76,0.4);
    border-radius: 999px;
    padding: 0.35rem 1.2rem;
    font-size: 0.78rem;
    color: var(--gold-lt);
    font-family: 'Lora', serif;
  }

  /* ── MAIN CONTAINER ── */
  .container {
    max-width: 900px;
    margin: 0 auto;
    padding: 2.5rem 1.5rem 4rem;
  }

  /* ── SECTION ── */
  .section {
    margin-bottom: 3rem;
  }
  .section-header {
    display: flex; align-items: center; gap: 1rem;
    margin-bottom: 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 2px solid var(--border);
  }
  .section-num {
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    font-weight: 700;
    color: var(--gold);
    background: var(--ink);
    border-radius: 4px;
    padding: 0.25rem 0.5rem;
    letter-spacing: 0.1em;
  }
  .section-title {
    font-family: 'Cinzel', serif;
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--ink);
  }

  /* ── DEFINITION BOX ── */
  .defbox {
    background: white;
    border-left: 4px solid var(--blue);
    border-radius: 0 8px 8px 0;
    padding: 1.25rem 1.5rem;
    margin: 1.25rem 0;
    box-shadow: 0 2px 8px var(--shadow);
    position: relative;
  }
  .defbox::before {
    content: attr(data-label);
    font-family: 'Cinzel', serif;
    font-size: 0.65rem;
    font-weight: 700;
    color: var(--blue-dk);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    display: block;
    margin-bottom: 0.5rem;
  }
  .defbox.theorem { border-color: var(--gold); }
  .defbox.theorem::before { color: #8B6914; }
  .defbox.example { border-color: var(--green); }
  .defbox.example::before { color: var(--green); }
  .defbox.warning { border-color: var(--red); }
  .defbox.warning::before { color: var(--red); }
  .defbox.proof { border-color: var(--muted); background: #FAFAF8; }
  .defbox.proof::before { color: var(--muted); }

  /* ── PROSE ── */
  .prose p { margin-bottom: 1rem; }
  .prose p:last-child { margin-bottom: 0; }
  .hl-gold { color: #8B6914; font-weight: 600; }
  .hl-blue { color: var(--blue-dk); font-weight: 600; }
  .hl-red  { color: var(--red); font-weight: 600; }
  .hl-grn  { color: var(--green); font-weight: 600; }

  /* ── ACCORDION ── */
  .accordion { margin: 1rem 0; }
  .acc-item {
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-bottom: 0.5rem;
    overflow: hidden;
    transition: box-shadow 0.2s;
  }
  .acc-item:hover { box-shadow: 0 2px 8px var(--shadow); }
  .acc-toggle {
    width: 100%; background: var(--cream-dk);
    border: none; cursor: pointer;
    padding: 0.9rem 1.25rem;
    display: flex; align-items: center; gap: 0.75rem;
    text-align: left;
    font-family: 'Lora', serif;
    font-size: 0.92rem;
    font-weight: 600;
    color: var(--ink);
    transition: background 0.2s;
  }
  .acc-toggle:hover { background: #E2DDD3; }
  .acc-toggle .acc-icon {
    width: 22px; height: 22px; border-radius: 50%;
    background: var(--ink); color: var(--gold);
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85rem; flex-shrink: 0;
    transition: transform 0.3s;
  }
  .acc-toggle[aria-expanded="true"] .acc-icon { transform: rotate(45deg); }
  .acc-body {
    display: none;
    padding: 1.25rem 1.5rem;
    background: white;
    border-top: 1px solid var(--border);
    animation: fadeIn 0.25s ease;
  }
  .acc-body.open { display: block; }
  @keyframes fadeIn { from { opacity:0; transform:translateY(-4px); } to { opacity:1; transform:none; } }

  /* ── INTERACTIVE VISUALIZER ── */
  .viz-card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 20px var(--shadow);
    overflow: hidden;
    margin: 1.5rem 0;
  }
  .viz-header {
    background: var(--ink);
    color: white;
    padding: 0.9rem 1.5rem;
    display: flex; align-items: center; gap: 0.75rem;
  }
  .viz-dot { width:10px; height:10px; border-radius:50%; }
  .viz-title {
    font-family: 'Cinzel', serif;
    font-size: 0.82rem;
    color: var(--gold-lt);
    letter-spacing: 0.08em;
    margin-left: 0.25rem;
  }
  .viz-body { padding: 1.5rem; }
  .viz-controls {
    display: flex; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 1rem;
    align-items: center;
  }
  .viz-controls label {
    font-size: 0.82rem; color: var(--muted); font-family: 'JetBrains Mono', monospace;
  }
  .viz-controls select, .viz-controls input[type=range] {
    font-size: 0.82rem;
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.25rem 0.5rem;
    background: var(--cream);
    cursor: pointer;
  }
  .btn {
    font-family: 'Lora', serif;
    font-size: 0.82rem;
    padding: 0.4rem 1rem;
    border-radius: 6px;
    border: none; cursor: pointer;
    transition: all 0.2s;
    font-weight: 600;
  }
  .btn-primary {
    background: var(--ink); color: var(--gold);
    border: 1px solid var(--gold);
  }
  .btn-primary:hover { background: var(--ink-soft); }
  .btn-secondary {
    background: white; color: var(--ink);
    border: 1px solid var(--border);
  }
  .btn-secondary:hover { background: var(--cream-dk); }

  canvas {
    width: 100%; border-radius: 8px;
    border: 1px solid var(--border);
    display: block;
  }
  .viz-info {
    margin-top: 0.75rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: var(--muted);
    background: var(--cream);
    border-radius: 6px;
    padding: 0.6rem 0.9rem;
    line-height: 1.6;
  }
  .viz-info span { color: var(--ink); font-weight: 500; }

  /* ── COMPARISON TABLE ── */
  .compare-table {
    width: 100%; border-collapse: collapse;
    margin: 1.25rem 0;
    font-size: 0.9rem;
    box-shadow: 0 2px 12px var(--shadow);
    border-radius: 10px;
    overflow: hidden;
  }
  .compare-table th {
    background: var(--ink);
    color: var(--gold-lt);
    font-family: 'Cinzel', serif;
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    padding: 0.9rem 1.25rem;
    text-align: left;
  }
  .compare-table td {
    padding: 0.8rem 1.25rem;
    border-bottom: 1px solid var(--border);
    background: white;
    vertical-align: top;
  }
  .compare-table tr:last-child td { border-bottom: none; }
  .compare-table tr:hover td { background: var(--cream); }
  .compare-table .col-cauchy td:first-child { border-left: 3px solid var(--blue); }
  .compare-table .col-div td:first-child { border-left: 3px solid var(--red); }

  /* ── QUIZ ── */
  .quiz-card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 16px var(--shadow);
    padding: 1.75rem;
    margin: 1.5rem 0;
  }
  .quiz-q {
    font-weight: 600;
    margin-bottom: 1.1rem;
    color: var(--ink);
    font-size: 0.95rem;
  }
  .quiz-opts { display: flex; flex-direction: column; gap: 0.5rem; }
  .quiz-opt {
    display: flex; align-items: center; gap: 0.75rem;
    padding: 0.65rem 1rem;
    border: 2px solid var(--border);
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.18s;
    font-size: 0.88rem;
    background: white;
  }
  .quiz-opt:hover { border-color: var(--blue); background: #EFF7FC; }
  .quiz-opt.correct { border-color: var(--green); background: #EFF8F4; }
  .quiz-opt.wrong { border-color: var(--red); background: #FEF0EE; }
  .quiz-opt-mark {
    width: 22px; height: 22px;
    border-radius: 50%;
    border: 2px solid var(--border);
    flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.7rem; font-weight: 700;
  }
  .quiz-opt.correct .quiz-opt-mark { background: var(--green); border-color: var(--green); color: white; }
  .quiz-opt.wrong .quiz-opt-mark { background: var(--red); border-color: var(--red); color: white; }
  .quiz-feedback {
    margin-top: 0.9rem;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    font-size: 0.85rem;
    display: none;
  }
  .quiz-feedback.show { display: block; }
  .quiz-feedback.ok { background: #EFF8F4; color: #1A5C3A; border-left: 3px solid var(--green); }
  .quiz-feedback.no { background: #FEF0EE; color: #7A2E22; border-left: 3px solid var(--red); }

  /* ── STEP-BY-STEP PROOF ── */
  .proof-steps { counter-reset: step; }
  .proof-step {
    display: flex; gap: 1rem;
    margin-bottom: 1rem;
    padding: 0.9rem 1rem;
    background: white;
    border-radius: 8px;
    border: 1px solid var(--border);
    opacity: 0;
    transform: translateY(8px);
    transition: all 0.35s ease;
  }
  .proof-step.visible { opacity: 1; transform: none; }
  .proof-step-num {
    counter-increment: step;
    font-family: 'Cinzel', serif;
    font-size: 0.7rem;
    font-weight: 700;
    color: white;
    background: var(--gold);
    border-radius: 4px;
    width: 28px; height: 28px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
    margin-top: 0.1rem;
  }
  .proof-step-content { font-size: 0.9rem; }

  /* ── PROGRESS BAR ── */
  .progress-wrap {
    background: var(--ink);
    color: white;
    padding: 1rem 1.5rem;
    display: flex; align-items: center; gap: 1rem;
    border-radius: 10px;
    margin-bottom: 2rem;
    font-size: 0.82rem;
  }
  .progress-bar-outer {
    flex: 1; background: rgba(255,255,255,0.15);
    border-radius: 999px; height: 8px; overflow: hidden;
  }
  .progress-bar-inner {
    height: 100%; background: linear-gradient(90deg, var(--gold), var(--gold-lt));
    border-radius: 999px;
    transition: width 0.4s ease;
    width: 0%;
  }
  .progress-label { color: var(--gold-lt); font-family: 'Cinzel', serif; font-size: 0.75rem; white-space: nowrap; }

  /* ── CODE BLOCK ── */
  .code-block {
    background: var(--ink);
    color: #E2E8F0;
    border-radius: 8px;
    padding: 1rem 1.25rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    line-height: 1.7;
    overflow-x: auto;
    margin: 0.75rem 0;
  }
  .code-block .kw { color: var(--gold-lt); }
  .code-block .cm { color: #64748B; font-style: italic; }
  .code-block .nm { color: #7DD3FC; }
  .code-block .op { color: #F472B6; }

  /* ── FOOTER ── */
  footer {
    background: var(--ink);
    color: #94A3B8;
    text-align: center;
    padding: 2rem;
    font-size: 0.8rem;
    margin-top: 2rem;
    border-top: 3px solid var(--gold);
  }
  footer strong { color: var(--gold-lt); }

  @media (max-width: 600px) {
    .hero { padding: 2.5rem 1rem 2rem; }
    .container { padding: 1.5rem 1rem 3rem; }
    .viz-controls { flex-direction: column; align-items: flex-start; }
  }
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <span class="nav-brand">⟨ ANALISIS REAL ⟩</span>
  <ul class="nav-links">
    <li><a href="#cauchy">Barisan Cauchy</a></li>
    <li><a href="#sifat">Sifat</a></li>
    <li><a href="#divergensi">Divergensi Sejati</a></li>
    <li><a href="#perbandingan">Perbandingan</a></li>
    <li><a href="#latihan">Latihan</a></li>
  </ul>
</nav>

<!-- HERO -->
<header class="hero">
  <div class="hero-eyebrow">Analisis Real · IKIP Siliwangi</div>
  <h1>Barisan Cauchy &<br><span>Divergensi Sejati</span></h1>
  <p class="hero-subtitle">Konvergensi tanpa batas, dan pelarian menuju tak hingga</p>
  <div class="hero-meta">
    <div class="hero-meta-item">
      <span class="val">ℝ</span>
      <span class="lbl">Bilangan Real</span>
    </div>
    <div class="hero-meta-item">
      <span class="val">ε–N</span>
      <span class="lbl">Metode Formal</span>
    </div>
    <div class="hero-meta-item">
      <span class="val">∞</span>
      <span class="lbl">Divergensi Sejati</span>
    </div>
  </div>
  <div class="hero-divider"></div>
  <div class="author-badge">Martin Bernard, M.Pd. · Pendidikan Matematika IKIP Siliwangi</div>
</header>

<div class="container">

  <!-- PROGRESS -->
  <div class="progress-wrap">
    <span class="progress-label">PROGRES MODUL</span>
    <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
    <span id="progressPct" style="color:var(--gold-lt);font-family:'Cinzel',serif;font-size:0.75rem;">0%</span>
  </div>

  <!-- ════════════════════ BAGIAN 1: BARISAN CAUCHY ════════════════════ -->
  <section class="section" id="cauchy">
    <div class="section-header">
      <span class="section-num">§ 1</span>
      <h2 class="section-title">Barisan Cauchy</h2>
    </div>

    <div class="prose">
      <p>
        Dalam analisis real, kita sering ingin menentukan apakah suatu barisan konvergen tanpa harus mengetahui nilai limitnya terlebih dahulu. 
        <span class="hl-blue">Barisan Cauchy</span> memberikan karakterisasi yang elegan untuk tujuan tersebut — konvergensi dideteksi melalui <em>perilaku internal</em> elemen-elemen barisan itu sendiri.
      </p>
      <p>
        Konsep ini dikembangkan oleh matematikawan Prancis <span class="hl-gold">Augustin-Louis Cauchy (1789–1857)</span> sebagai fondasi rigor dalam analisis modern. Ide utamanya: elemen-elemen barisan yang "semakin rapat satu sama lain" menjamin keberadaan nilai limit.
      </p>
    </div>

    <div class="defbox" data-label="Definisi 1.1 — Barisan Cauchy">
      <p>
        Suatu barisan \((x_n)\) dalam \(\mathbb{R}\) disebut <strong>barisan Cauchy</strong> jika untuk setiap \(\varepsilon > 0\), terdapat \(N \in \mathbb{N}\) sedemikian sehingga:
      </p>
      <br>
      <p style="text-align:center; font-size:1.05rem;">
        \[ \forall\, m, n \geq N \implies |x_m - x_n| < \varepsilon \]
      </p>
      <br>
      <p style="font-size:0.88rem; color:var(--muted); margin-top:0.5rem;">
        <em>Artinya: elemen-elemen yang "jauh" dalam barisan (indeks besar) saling berdekatan satu sama lain dengan jarak yang dapat dibuat sekecil mungkin.</em>
      </p>
    </div>

    <div class="prose">
      <p>
        Perhatikan bahwa definisi ini berbeda secara halus dari definisi konvergensi biasa. Pada konvergensi biasa, kita memerlukan <em>nilai limit \(L\)</em> yang diketahui: \(|x_n - L| < \varepsilon\). 
        Pada barisan Cauchy, kita hanya membandingkan <em>sesama anggota barisan</em>: \(|x_m - x_n| < \varepsilon\).
      </p>
    </div>

    <!-- VISUALIZER 1 -->
    <div class="viz-card">
      <div class="viz-header">
        <div class="viz-dot" style="background:#EF4444"></div>
        <div class="viz-dot" style="background:#F59E0B; margin-left:4px"></div>
        <div class="viz-dot" style="background:#10B981; margin-left:4px"></div>
        <span class="viz-title">VISUALISASI INTERAKTIF — PERILAKU BARISAN</span>
      </div>
      <div class="viz-body">
        <div class="viz-controls">
          <label>Pilih barisan:</label>
          <select id="seqSelect" onchange="drawSeq()">
            <option value="cauchy1">xₙ = 1/n (Cauchy)</option>
            <option value="cauchy2">xₙ = (n+1)/n (Cauchy)</option>
            <option value="cauchy3">xₙ = (-1)ⁿ/n (Cauchy)</option>
            <option value="div1">xₙ = (-1)ⁿ (Divergen Osilasi)</option>
            <option value="div2">xₙ = n (Divergen → +∞)</option>
            <option value="div3">xₙ = (-1)ⁿ · n (Divergen Sejati)</option>
          </select>
          <label>N hingga:</label>
          <input type="range" id="nRange" min="5" max="40" value="20" oninput="updateN(this.value)">
          <span id="nVal" style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;">N=20</span>
          <button class="btn btn-primary" onclick="drawSeq()">Perbarui</button>
        </div>
        <canvas id="seqCanvas" height="220"></canvas>
        <div class="viz-info" id="seqInfo">
          Pilih barisan dan tekan <strong>Perbarui</strong> untuk melihat perilaku elemen.
        </div>
      </div>
    </div>

    <!-- VISUALIZER 2: JARAK |xm - xn| -->
    <div class="viz-card">
      <div class="viz-header">
        <div class="viz-dot" style="background:#EF4444"></div>
        <div class="viz-dot" style="background:#F59E0B; margin-left:4px"></div>
        <div class="viz-dot" style="background:#10B981; margin-left:4px"></div>
        <span class="viz-title">VISUALISASI — JARAK |x_m − x_n| TERHADAP ε</span>
      </div>
      <div class="viz-body">
        <div class="viz-controls">
          <label>Barisan:</label>
          <select id="distSelect" onchange="drawDist()">
            <option value="cauchy1">xₙ = 1/n</option>
            <option value="div1">xₙ = (-1)ⁿ</option>
            <option value="div3">xₙ = (-1)ⁿ·n</option>
          </select>
          <label>ε =</label>
          <input type="range" id="epsRange" min="1" max="20" value="5" oninput="updateEps(this.value)">
          <span id="epsVal" style="font-family:'JetBrains Mono',monospace;font-size:0.8rem;">ε = 0.5</span>
          <button class="btn btn-primary" onclick="drawDist()">Tampilkan</button>
        </div>
        <canvas id="distCanvas" height="200"></canvas>
        <div class="viz-info" id="distInfo">
          Garis <span style="color:#4A9ECA">biru</span> = batas ε. Titik <span style="color:#10B981">hijau</span> = jarak ≤ ε (syarat Cauchy terpenuhi). Titik <span style="color:#EF4444">merah</span> = jarak > ε (syarat belum terpenuhi untuk N tersebut).
        </div>
      </div>
    </div>

    <!-- CONTOH -->
    <div class="accordion">
      <div class="acc-item">
        <button class="acc-toggle" onclick="toggleAcc(this)" aria-expanded="false">
          <span class="acc-icon">+</span>
          Contoh 1.1 — Membuktikan \(x_n = 1/n\) adalah Barisan Cauchy
        </button>
        <div class="acc-body">
          <div class="defbox example" data-label="Contoh 1.1">
            <p><strong>Klaim:</strong> Barisan \(x_n = \dfrac{1}{n}\) adalah barisan Cauchy di \(\mathbb{R}\).</p>
            <p style="margin-top:0.75rem"><strong>Bukti:</strong></p>
            <p>Ambil sembarang \(\varepsilon > 0\). Kita perlu mencari \(N \in \mathbb{N}\) sehingga \(m, n \geq N \Rightarrow |x_m - x_n| < \varepsilon\).</p>
            <p>Perhatikan:</p>
            \[ |x_m - x_n| = \left|\frac{1}{m} - \frac{1}{n}\right| \leq \frac{1}{m} + \frac{1}{n} \leq \frac{1}{N} + \frac{1}{N} = \frac{2}{N} \]
            <p>Pilih \(N > \dfrac{2}{\varepsilon}\), maka untuk semua \(m, n \geq N\):</p>
            \[ |x_m - x_n| \leq \frac{2}{N} < \varepsilon \quad \square \]
          </div>
        </div>
      </div>

      <div class="acc-item">
        <button class="acc-toggle" onclick="toggleAcc(this)" aria-expanded="false">
          <span class="acc-icon">+</span>
          Contoh 1.2 — \(x_n = (-1)^n\) bukan Barisan Cauchy
        </button>
        <div class="acc-body">
          <div class="defbox warning" data-label="Contoh 1.2 — Bukan Barisan Cauchy">
            <p><strong>Klaim:</strong> Barisan \(x_n = (-1)^n\) BUKAN barisan Cauchy.</p>
            <p style="margin-top:0.75rem"><strong>Bukti Negasi:</strong></p>
            <p>Kita harus menunjukkan: \(\exists\, \varepsilon_0 > 0\), \(\forall\, N \in \mathbb{N}\), \(\exists\, m, n \geq N\) sehingga \(|x_m - x_n| \geq \varepsilon_0\).</p>
            <p>Pilih \(\varepsilon_0 = 1\). Untuk sembarang \(N\), ambil \(m = 2N\) (genap) dan \(n = 2N+1\) (ganjil):</p>
            \[ |x_m - x_n| = |(-1)^{2N} - (-1)^{2N+1}| = |1 - (-1)| = 2 \geq \varepsilon_0 = 1 \quad \square \]
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ════════════════════ BAGIAN 2: SIFAT-SIFAT ════════════════════ -->
  <section class="section" id="sifat">
    <div class="section-header">
      <span class="section-num">§ 2</span>
      <h2 class="section-title">Sifat-Sifat Barisan Cauchy</h2>
    </div>

    <div class="defbox theorem" data-label="Teorema 2.1 — Barisan Cauchy Terbatas">
      <p>Setiap barisan Cauchy adalah <strong>barisan terbatas</strong>.</p>
    </div>

    <div class="accordion">
      <div class="acc-item">
        <button class="acc-toggle" onclick="toggleAcc(this)" aria-expanded="false">
          <span class="acc-icon">+</span>
          Bukti Teorema 2.1
        </button>
        <div class="acc-body">
          <div class="defbox proof" data-label="Bukti">
            <p>Misalkan \((x_n)\) adalah barisan Cauchy. Pilih \(\varepsilon = 1\). Maka terdapat \(N \in \mathbb{N}\) sehingga \(m, n \geq N \Rightarrow |x_m - x_n| < 1\).</p>
            <p style="margin-top:0.5rem">Khususnya, untuk semua \(n \geq N\):</p>
            \[ |x_n| = |x_n - x_N + x_N| \leq |x_n - x_N| + |x_N| < 1 + |x_N| \]
            <p>Definisikan \(M = \max\{|x_1|, |x_2|, \ldots, |x_{N-1}|, 1 + |x_N|\}\). Maka \(|x_n| \leq M\) untuk semua \(n \in \mathbb{N}\). \(\square\)</p>
          </div>
        </div>
      </div>
    </div>

    <div class="defbox theorem" data-label="Teorema 2.2 — Kelengkapan ℝ (Cauchy Criterion)">
      <p>Di dalam \(\mathbb{R}\), suatu barisan konvergen <strong>jika dan hanya jika</strong> barisan tersebut adalah barisan Cauchy.</p>
      \[ (x_n) \text{ konvergen di } \mathbb{R} \iff (x_n) \text{ adalah barisan Cauchy} \]
    </div>

    <div class="prose">
      <p>
        Teorema ini dikenal sebagai <span class="hl-gold">Kriteria Kelengkapan</span> dan merupakan salah satu hasil terpenting dalam analisis real. Ia menyatakan bahwa \(\mathbb{R}\) adalah ruang metrik yang <em>lengkap</em> (complete), artinya setiap barisan Cauchy di \(\mathbb{R}\) pasti konvergen di \(\mathbb{R}\).
      </p>
      <p>
        Sebagai perbandingan, \(\mathbb{Q}\) (bilangan rasional) <span class="hl-red">bukan</span> ruang lengkap — barisan Cauchy di \(\mathbb{Q}\) bisa berkonvergen ke bilangan irasional (misal: pendekatan decimal \(\sqrt{2}\)).
      </p>
    </div>

    <div class="accordion">
      <div class="acc-item">
        <button class="acc-toggle" onclick="toggleAcc(this)" aria-expanded="false">
          <span class="acc-icon">+</span>
          Teorema 2.3 — Subbarisan Barisan Cauchy
        </button>
        <div class="acc-body">
          <div class="defbox theorem" data-label="Teorema 2.3">
            <p>Jika \((x_n)\) adalah barisan Cauchy dan \((x_{n_k})\) adalah subbarisannya yang konvergen ke \(L\), maka \((x_n)\) juga konvergen ke \(L\).</p>
          </div>
          <div class="defbox proof" data-label="Sketsa Bukti">
            <p>Karena \((x_n)\) Cauchy, ambil \(\varepsilon > 0\), terdapat \(N_1\) sehingga \(m,n \geq N_1 \Rightarrow |x_m - x_n| < \varepsilon/2\).</p>
            <p>Karena \(x_{n_k} \to L\), terdapat \(K\) sehingga \(k \geq K \Rightarrow |x_{n_k} - L| < \varepsilon/2\).</p>
            <p>Pilih \(k\) cukup besar sehingga \(n_k \geq N_1\). Maka untuk \(n \geq N_1\):</p>
            \[ |x_n - L| \leq |x_n - x_{n_k}| + |x_{n_k} - L| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon \quad \square \]
          </div>
        </div>
      </div>

      <div class="acc-item">
        <button class="acc-toggle" onclick="toggleAcc(this)" aria-expanded="false">
          <span class="acc-icon">+</span>
          Langkah-langkah Membuktikan Barisan Cauchy
        </button>
        <div class="acc-body">
          <div class="proof-steps" id="proofSteps">
            <div class="proof-step">
              <div class="proof-step-num">1</div>
              <div class="proof-step-content">
                <strong>Nyatakan tujuan:</strong> Akan ditunjukkan bahwa untuk setiap \(\varepsilon > 0\), terdapat \(N \in \mathbb{N}\) sehingga \(m, n \geq N \Rightarrow |x_m - x_n| < \varepsilon\).
              </div>
            </div>
            <div class="proof-step">
              <div class="proof-step-num">2</div>
              <div class="proof-step-content">
                <strong>Perkirakan \(|x_m - x_n|\):</strong> Hitung atau batas-ataskan selisih \(|x_m - x_n|\) dalam bentuk yang bergantung pada \(m\) dan \(n\).
              </div>
            </div>
            <div class="proof-step">
              <div class="proof-step-num">3</div>
              <div class="proof-step-content">
                <strong>Gunakan \(m, n \geq N\):</strong> Substitusikan kondisi \(m \geq N\) dan \(n \geq N\) untuk menyederhanakan batas atas tersebut menjadi fungsi \(N\) saja.
              </div>
            </div>
            <div class="proof-step">
              <div class="proof-step-num">4</div>
              <div class="proof-step-content">
                <strong>Pilih \(N\) yang tepat:</strong> Tentukan nilai \(N\) (biasanya dari \(\lfloor f(1/\varepsilon) \rfloor + 1\)) sehingga batas atas kurang dari \(\varepsilon\).
              </div>
            </div>
            <div class="proof-step">
              <div class="proof-step-num">5</div>
              <div class="proof-step-content">
                <strong>Tulis bukti formal:</strong> Susun argumen lengkap dan akhiri dengan \(\square\) (QED).
              </div>
            </div>
          </div>
          <button class="btn btn-primary" style="margin-top:0.75rem" onclick="showProofSteps()">Tampilkan Langkah ▶</button>
        </div>
      </div>
    </div>
  </section>

  <!-- ════════════════════ BAGIAN 3: DIVERGENSI SEJATI ════════════════════ -->
  <section class="section" id="divergensi">
    <div class="section-header">
      <span class="section-num">§ 3</span>
      <h2 class="section-title">Barisan Divergensi Sejati</h2>
    </div>

    <div class="prose">
      <p>
        Tidak semua barisan yang divergen (tidak konvergen) berperilaku sama. Ada barisan yang "<em>melarikan diri</em>" ke tak hingga secara teratur — inilah yang disebut <span class="hl-red">divergensi sejati</span> (proper divergence). Berbeda dengan divergensi osilasi, divergensi sejati menuju \(+\infty\) atau \(-\infty\) secara monoton-asimtotik.
      </p>
    </div>

    <div class="defbox" data-label="Definisi 3.1 — Divergensi ke +∞">
      <p>Barisan \((x_n)\) dikatakan <strong>divergen ke \(+\infty\)</strong>, ditulis \(\lim_{n\to\infty} x_n = +\infty\), jika untuk setiap \(M > 0\), terdapat \(N \in \mathbb{N}\) sedemikian sehingga:</p>
      <br>
      \[ \forall\, n \geq N \implies x_n > M \]
    </div>

    <div class="defbox" data-label="Definisi 3.2 — Divergensi ke −∞">
      <p>Barisan \((x_n)\) dikatakan <strong>divergen ke \(-\infty\)</strong>, ditulis \(\lim_{n\to\infty} x_n = -\infty\), jika untuk setiap \(M < 0\), terdapat \(N \in \mathbb{N}\) sedemikian sehingga:</p>
      <br>
      \[ \forall\, n \geq N \implies x_n < M \]
    </div>

    <div class="prose">
      <p>
        Catatan terminologi: dalam konteks <span class="hl-gold">Bartle & Sherbert</span> (Introduction to Real Analysis), divergensi sejati merujuk pada barisan yang "properly diverges" — yaitu memiliki limit tak hingga yang well-defined dan bertanda konsisten. Ini berbeda dari divergensi karena osilasi (\((-1)^n\)) yang tidak punya limit-tak-hingga pun.
      </p>
    </div>

    <div class="accordion">
      <div class="acc-item">
        <button class="acc-toggle" onclick="toggleAcc(this)" aria-expanded="false">
          <span class="acc-icon">+</span>
          Contoh 3.1 — \(x_n = n\) divergen ke \(+\infty\)
        </button>
        <div class="acc-body">
          <div class="defbox example" data-label="Contoh 3.1">
            <p><strong>Klaim:</strong> \(\lim_{n\to\infty} n = +\infty\)</p>
            <p style="margin-top:0.75rem"><strong>Bukti:</strong></p>
            <p>Ambil sembarang \(M > 0\). Pilih \(N = \lceil M \rceil + 1\). Maka untuk semua \(n \geq N\):</p>
            \[ x_n = n \geq N > M \quad \square \]
          </div>
        </div>
      </div>

      <div class="acc-item">
        <button class="acc-toggle" onclick="toggleAcc(this)" aria-expanded="false">
          <span class="acc-icon">+</span>
          Contoh 3.2 — \(x_n = \sqrt{n}\) divergen ke \(+\infty\)
        </button>
        <div class="acc-body">
          <div class="defbox example" data-label="Contoh 3.2">
            <p><strong>Klaim:</strong> \(\lim_{n\to\infty} \sqrt{n} = +\infty\)</p>
            <p style="margin-top:0.75rem"><strong>Bukti:</strong></p>
            <p>Ambil sembarang \(M > 0\). Pilih \(N = \lceil M^2 \rceil + 1\). Maka untuk \(n \geq N\):</p>
            \[ \sqrt{n} \geq \sqrt{N} > \sqrt{M^2} = M \quad \square \]
          </div>
        </div>
      </div>

      <div class="acc-item">
        <button class="acc-toggle" onclick="toggleAcc(this)" aria-expanded="false">
          <span class="acc-icon">+</span>
          Contoh 3.3 — \(x_n = (-1)^n \cdot n\) bukan divergensi sejati
        </button>
        <div class="acc-body">
          <div class="defbox warning" data-label="Contoh 3.3 — Bukan Divergensi Sejati">
            <p>Barisan \(x_n = (-1)^n \cdot n\) divergen, <em>tetapi bukan divergensi sejati</em>.</p>
            <p style="margin-top:0.5rem">Barisan ini beroscilasi: nilai-nilainya berganti-ganti antara positif besar (\(n, 3n, \ldots\)) dan negatif besar (\(-2n, -4n, \ldots\)).</p>
            <p>Ia tidak mendekati \(+\infty\) (karena ada istilah negatif yang sangat kecil) maupun \(-\infty\) (karena ada istilah positif yang sangat besar).</p>
            <p>Barisan ini adalah contoh <strong>divergensi osilasi tidak terbatas</strong>, bukan divergensi sejati.</p>
          </div>
        </div>
      </div>
    </div>

    <div class="defbox theorem" data-label="Teorema 3.1 — Kriteria Divergensi Sejati">
      <p>Barisan monoton naik \((x_n)\) yang tidak terbatas di atas adalah divergen sejati ke \(+\infty\):</p>
      \[ (x_n) \text{ monoton naik dan tak terbatas} \implies \lim_{n\to\infty} x_n = +\infty \]
      <p style="margin-top:0.5rem">Demikian pula, barisan monoton turun yang tidak terbatas di bawah divergen sejati ke \(-\infty\).</p>
    </div>

    <div class="defbox theorem" data-label="Teorema 3.2 — Aljabar Divergensi Sejati">
      <p>Jika \(\lim x_n = +\infty\) dan \((y_n)\) terbatas di bawah (terdapat \(m\) s.t. \(y_n \geq m\)), maka:</p>
      \[ \lim_{n\to\infty}(x_n + y_n) = +\infty \]
      <p style="margin-top:0.5rem">Jika \(\lim x_n = +\infty\) dan \(c > 0\), maka \(\lim c \cdot x_n = +\infty\).</p>
    </div>
  </section>

  <!-- ════════════════════ BAGIAN 4: PERBANDINGAN ════════════════════ -->
  <section class="section" id="perbandingan">
    <div class="section-header">
      <span class="section-num">§ 4</span>
      <h2 class="section-title">Tabel Perbandingan Komprehensif</h2>
    </div>

    <table class="compare-table">
      <thead>
        <tr>
          <th>Aspek</th>
          <th style="color:#7DD3FC">Barisan Cauchy</th>
          <th style="color:#FCA5A5">Divergensi Sejati</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Definisi formal</strong></td>
          <td>\(\forall\varepsilon>0, \exists N: m,n\geq N\Rightarrow|x_m-x_n|<\varepsilon\)</td>
          <td>\(\forall M>0, \exists N: n\geq N\Rightarrow x_n>M\)</td>
        </tr>
        <tr>
          <td><strong>Perilaku elemen</strong></td>
          <td>Semakin rapat satu sama lain</td>
          <td>Semakin jauh menuju ±∞</td>
        </tr>
        <tr>
          <td><strong>Keterbatasan</strong></td>
          <td>Selalu <span class="hl-grn">terbatas</span></td>
          <td>Selalu <span class="hl-red">tidak terbatas</span></td>
        </tr>
        <tr>
          <td><strong>Hubungan dengan konvergensi</strong></td>
          <td>Ekuivalen dengan konvergensi di ℝ</td>
          <td>Divergen — tidak ada limit di ℝ</td>
        </tr>
        <tr>
          <td><strong>Kelengkapan ruang</strong></td>
          <td>Terkait dengan kelengkapan ℝ</td>
          <td>Tidak tergantung kelengkapan</td>
        </tr>
        <tr>
          <td><strong>Contoh khas</strong></td>
          <td>\(1/n,\; n/(n+1),\; (-1)^n/n\)</td>
          <td>\(n,\; n^2,\; \sqrt{n},\; 2^n\)</td>
        </tr>
        <tr>
          <td><strong>Bukan contohnya</strong></td>
          <td>\((-1)^n\) (osilasi), \(n\) (tak terbatas)</td>
          <td>\((-1)^n \cdot n\) (osilasi tak terbatas)</td>
        </tr>
        <tr>
          <td><strong>Subbarisan</strong></td>
          <td>Setiap subbarisan juga Cauchy</td>
          <td>Subbarisan juga divergen ke ±∞</td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- ════════════════════ BAGIAN 5: LATIHAN ════════════════════ -->
  <section class="section" id="latihan">
    <div class="section-header">
      <span class="section-num">§ 5</span>
      <h2 class="section-title">Latihan & Kuis Interaktif</h2>
    </div>

    <!-- QUIZ 1 -->
    <div class="quiz-card">
      <div class="quiz-q">1. Barisan \(x_n = \dfrac{n}{n+1}\) adalah...</div>
      <div class="quiz-opts">
        <div class="quiz-opt" onclick="answerQ(this, 1, true)">
          <div class="quiz-opt-mark">A</div>
          Barisan Cauchy yang konvergen ke 1
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 1, false)">
          <div class="quiz-opt-mark">B</div>
          Barisan Cauchy yang divergen ke +∞
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 1, false)">
          <div class="quiz-opt-mark">C</div>
          Bukan barisan Cauchy karena nilainya mendekati 1
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 1, false)">
          <div class="quiz-opt-mark">D</div>
          Divergen sejati ke +∞
        </div>
      </div>
      <div class="quiz-feedback" id="fb1">
        ✓ Benar! \(x_n = n/(n+1) \to 1\). Karena konvergen di ℝ, maka ia adalah barisan Cauchy (Kriteria Kelengkapan). \(|x_m - x_n| = |m/(m+1) - n/(n+1)| = |m-n|/((m+1)(n+1)) \leq 1/N \to 0\).
      </div>
    </div>

    <!-- QUIZ 2 -->
    <div class="quiz-card">
      <div class="quiz-q">2. Manakah pernyataan yang BENAR tentang barisan Cauchy?</div>
      <div class="quiz-opts">
        <div class="quiz-opt" onclick="answerQ(this, 2, false)">
          <div class="quiz-opt-mark">A</div>
          Setiap barisan terbatas adalah barisan Cauchy
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 2, true)">
          <div class="quiz-opt-mark">B</div>
          Setiap barisan Cauchy adalah barisan terbatas
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 2, false)">
          <div class="quiz-opt-mark">C</div>
          Barisan Cauchy selalu monoton
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 2, false)">
          <div class="quiz-opt-mark">D</div>
          Barisan \((-1)^n\) adalah barisan Cauchy
        </div>
      </div>
      <div class="quiz-feedback" id="fb2">
        ✓ Benar! Teorema 2.1 menyatakan setiap barisan Cauchy terbatas. Opsi A salah (\((-1)^n\) terbatas tapi bukan Cauchy). Opsi C salah (Cauchy tidak harus monoton, contoh: \((-1)^n/n\)). Opsi D salah (terbukti di Contoh 1.2).
      </div>
    </div>

    <!-- QUIZ 3 -->
    <div class="quiz-card">
      <div class="quiz-q">3. Barisan \(x_n = (-1)^n \cdot n\) termasuk kategori...</div>
      <div class="quiz-opts">
        <div class="quiz-opt" onclick="answerQ(this, 3, false)">
          <div class="quiz-opt-mark">A</div>
          Barisan Cauchy
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 3, false)">
          <div class="quiz-opt-mark">B</div>
          Divergen sejati ke +∞
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 3, false)">
          <div class="quiz-opt-mark">C</div>
          Divergen sejati ke −∞
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 3, true)">
          <div class="quiz-opt-mark">D</div>
          Divergen osilasi tidak terbatas (bukan divergensi sejati)
        </div>
      </div>
      <div class="quiz-feedback" id="fb3">
        ✓ Benar! \((-1)^n \cdot n\) berganti-ganti antara \(+n\) dan \(-n\). Ia tidak mendekati \(+\infty\) (karena ada suku sangat negatif) maupun \(-\infty\). Ini adalah divergensi osilasi, bukan divergensi sejati.
      </div>
    </div>

    <!-- QUIZ 4 -->
    <div class="quiz-card">
      <div class="quiz-q">4. Untuk membuktikan \(x_n = n^2\) divergen sejati ke \(+\infty\), kita memilih \(N\) sebesar...</div>
      <div class="quiz-opts">
        <div class="quiz-opt" onclick="answerQ(this, 4, false)">
          <div class="quiz-opt-mark">A</div>
          \(N = M\)
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 4, true)">
          <div class="quiz-opt-mark">B</div>
          \(N = \lceil\sqrt{M}\rceil + 1\)
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 4, false)">
          <div class="quiz-opt-mark">C</div>
          \(N = M^2\)
        </div>
        <div class="quiz-opt" onclick="answerQ(this, 4, false)">
          <div class="quiz-opt-mark">D</div>
          \(N = 2/M\)
        </div>
      </div>
      <div class="quiz-feedback" id="fb4">
        ✓ Benar! Kita ingin \(n^2 > M\), yaitu \(n > \sqrt{M}\). Jadi pilih \(N = \lceil\sqrt{M}\rceil + 1\). Maka untuk \(n \geq N\): \(x_n = n^2 \geq N^2 > M\). \(\square\)
      </div>
    </div>

    <!-- SOAL ESAI -->
    <div class="defbox" data-label="Soal Esai — Analisis Mendalam" style="margin-top:1.5rem">
      <p><strong>Soal 5 (Esai):</strong> Misalkan \((x_n)\) adalah barisan Cauchy dan \((y_n)\) adalah barisan Cauchy. Buktikan bahwa \((x_n + y_n)\) juga merupakan barisan Cauchy!</p>
      <p style="margin-top:0.75rem; font-size:0.87rem; color:var(--muted)"><em>Petunjuk: Gunakan ketaksamaan segitiga dan pilih N = max(N₁, N₂) dari masing-masing ε/2.</em></p>
    </div>
  </section>

</div>

<!-- FOOTER -->
<footer>
  <p><strong>Barisan Cauchy & Divergensi Sejati</strong> — Modul Interaktif Analisis Real</p>
  <p style="margin-top:0.35rem">Disusun oleh <strong>Martin Bernard, M.Pd.</strong> | Program Studi Pendidikan Matematika | IKIP Siliwangi, Cimahi</p>
  <p style="margin-top:0.35rem; font-size:0.72rem; color:#64748B">Referensi: Bartle & Sherbert, <em>Introduction to Real Analysis</em>, 4th ed. · Abbott, <em>Understanding Analysis</em></p>
</footer>

<script>
// ─── MATHJAX CONFIG ───
window.MathJax = {
  tex: { inlineMath: [['\\(','\\)'],['$','$']], displayMath: [['\\[','\\]']] },
  startup: { ready() { MathJax.startup.defaultReady(); } }
};

// ─── ACCORDION ───
function toggleAcc(btn) {
  const body = btn.nextElementSibling;
  const open = body.classList.contains('open');
  body.classList.toggle('open', !open);
  btn.setAttribute('aria-expanded', String(!open));
  updateProgress();
}

// ─── QUIZ ───
const answered = {};
function answerQ(el, qId, correct) {
  if (answered[qId]) return;
  answered[qId] = true;
  const opts = el.parentElement.querySelectorAll('.quiz-opt');
  opts.forEach(o => {
    o.style.pointerEvents = 'none';
    const isCorrect = o.onclick.toString().includes('true');
    if (isCorrect) { o.classList.add('correct'); o.querySelector('.quiz-opt-mark').textContent = '✓'; }
    else if (o === el && !correct) { o.classList.add('wrong'); o.querySelector('.quiz-opt-mark').textContent = '✗'; }
  });
  const fb = document.getElementById('fb' + qId);
  if (fb) { fb.classList.add('show', correct ? 'ok' : 'no'); }
  updateProgress();
  if (typeof MathJax !== 'undefined') MathJax.typesetPromise([fb]);
}

// ─── PROGRESS ───
function updateProgress() {
  const totalSections = 5;
  const openAccs = document.querySelectorAll('.acc-body.open').length;
  const answeredCount = Object.keys(answered).length;
  const pct = Math.min(100, Math.round((openAccs * 8 + answeredCount * 12)));
  document.getElementById('progressBar').style.width = pct + '%';
  document.getElementById('progressPct').textContent = pct + '%';
}

// ─── PROOF STEPS ───
function showProofSteps() {
  const steps = document.querySelectorAll('#proofSteps .proof-step');
  steps.forEach((s, i) => setTimeout(() => s.classList.add('visible'), i * 180));
}

// ─── SEQUENCE DATA ───
const sequences = {
  cauchy1: { fn: n => 1/n, label: 'xₙ = 1/n', isCauchy: true, desc: 'Konvergen ke 0. Barisan Cauchy.' },
  cauchy2: { fn: n => (n+1)/n, label: 'xₙ = (n+1)/n', isCauchy: true, desc: 'Konvergen ke 1. Barisan Cauchy.' },
  cauchy3: { fn: n => Math.pow(-1,n)/n, label: 'xₙ = (−1)ⁿ/n', isCauchy: true, desc: 'Konvergen ke 0 (dengan osilasi peredam). Barisan Cauchy.' },
  div1:    { fn: n => Math.pow(-1,n), label: 'xₙ = (−1)ⁿ', isCauchy: false, desc: 'Osilasi antara ±1. Bukan Cauchy. Bukan divergensi sejati.' },
  div2:    { fn: n => n, label: 'xₙ = n', isCauchy: false, desc: 'Divergen sejati ke +∞. Tidak terbatas.' },
  div3:    { fn: n => Math.pow(-1,n)*n, label: 'xₙ = (−1)ⁿ·n', isCauchy: false, desc: 'Divergen osilasi tidak terbatas. Bukan Cauchy, bukan divergensi sejati.' },
};

// ─── DRAW SEQUENCE ───
function updateN(v) { document.getElementById('nVal').textContent = 'N=' + v; }
function updateEps(v) { document.getElementById('epsVal').textContent = 'ε = ' + (v/10).toFixed(1); }

function drawSeq() {
  const key = document.getElementById('seqSelect').value;
  const N = parseInt(document.getElementById('nRange').value);
  const seq = sequences[key];
  const canvas = document.getElementById('seqCanvas');
  const ctx = canvas.getContext('2d');
  const W = canvas.offsetWidth || 750, H = 220;
  canvas.width = W; canvas.height = H;
  ctx.clearRect(0, 0, W, H);

  const vals = [];
  for (let n = 1; n <= N; n++) vals.push({ n, v: seq.fn(n) });

  let minV = Math.min(...vals.map(p=>p.v));
  let maxV = Math.max(...vals.map(p=>p.v));
  const pad = 36;
  const range = (maxV - minV) || 1;
  const toY = v => pad + (1 - (v - minV) / range) * (H - 2*pad);
  const toX = n => pad + ((n-1) / (N-1 || 1)) * (W - 2*pad);

  // Grid
  ctx.strokeStyle = '#E5E7EB'; ctx.lineWidth = 1;
  for (let i = 0; i <= 4; i++) {
    const y = pad + i * (H - 2*pad) / 4;
    ctx.beginPath(); ctx.moveTo(pad, y); ctx.lineTo(W - pad, y); ctx.stroke();
    const v = maxV - i * range / 4;
    ctx.fillStyle = '#9CA3AF'; ctx.font = '10px JetBrains Mono,monospace';
    ctx.fillText(v.toFixed(2), 2, y + 4);
  }

  // Line
  ctx.beginPath(); ctx.strokeStyle = seq.isCauchy ? '#4A9ECA' : '#EF4444'; ctx.lineWidth = 1.5;
  vals.forEach((p, i) => {
    const x = toX(p.n), y = toY(p.v);
    if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
  });
  ctx.stroke();

  // Dots
  vals.forEach(p => {
    const x = toX(p.n), y = toY(p.v);
    ctx.beginPath();
    ctx.arc(x, y, 3.5, 0, Math.PI*2);
    ctx.fillStyle = seq.isCauchy ? '#2D6E96' : '#B84C3A';
    ctx.fill();
  });

  // Label
  ctx.fillStyle = seq.isCauchy ? '#2D6E96' : '#B84C3A';
  ctx.font = 'bold 11px Lora,serif';
  ctx.fillText(seq.label, pad, pad - 10);

  document.getElementById('seqInfo').innerHTML =
    `<span>${seq.label}</span> — ${seq.desc} &nbsp;|&nbsp; Tipe: <span>${seq.isCauchy ? '✓ Barisan Cauchy' : '✗ Bukan Barisan Cauchy'}</span>`;
}

// ─── DRAW DISTANCE ───
function drawDist() {
  const key = document.getElementById('distSelect').value;
  const eps = parseInt(document.getElementById('epsRange').value) / 10;
  document.getElementById('epsVal').textContent = 'ε = ' + eps.toFixed(1);
  const seq = sequences[key];
  const canvas = document.getElementById('distCanvas');
  const ctx = canvas.getContext('2d');
  const W = canvas.offsetWidth || 750, H = 200;
  canvas.width = W; canvas.height = H;
  ctx.clearRect(0, 0, W, H);

  const N = 20;
  const m = Math.floor(N / 2);
  const dists = [];
  for (let n = 1; n <= N; n++) {
    dists.push({ n, d: Math.abs(seq.fn(m) - seq.fn(n)) });
  }

  const pad = 36;
  const maxD = Math.min(Math.max(...dists.map(p=>p.d)), 5);
  const toY = v => pad + (1 - Math.min(v, maxD) / maxD) * (H - 2*pad);
  const toX = n => pad + ((n-1) / (N-1)) * (W - 2*pad);

  // Grid
  ctx.strokeStyle = '#E5E7EB'; ctx.lineWidth = 1;
  [0, 0.25, 0.5, 0.75, 1].forEach(f => {
    const y = pad + f * (H - 2*pad);
    ctx.beginPath(); ctx.moveTo(pad, y); ctx.lineTo(W-pad, y); ctx.stroke();
    ctx.fillStyle = '#9CA3AF'; ctx.font = '10px JetBrains Mono,monospace';
    ctx.fillText((maxD*(1-f)).toFixed(2), 2, y+4);
  });

  // ε line
  const epsY = toY(eps);
  ctx.beginPath(); ctx.setLineDash([5,4]);
  ctx.strokeStyle = '#4A9ECA'; ctx.lineWidth = 1.5;
  ctx.moveTo(pad, epsY); ctx.lineTo(W-pad, epsY); ctx.stroke();
  ctx.setLineDash([]);
  ctx.fillStyle = '#4A9ECA'; ctx.font = 'bold 10px JetBrains Mono,monospace';
  ctx.fillText('ε=' + eps.toFixed(1), W - pad + 2, epsY + 4);

  // Points
  dists.forEach(p => {
    const x = toX(p.n), y = toY(p.d);
    const ok = p.d <= eps;
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, Math.PI*2);
    ctx.fillStyle = ok ? '#10B981' : '#EF4444';
    ctx.fill();
    ctx.strokeStyle = 'white'; ctx.lineWidth = 1.5;
    ctx.stroke();
  });

  const okCount = dists.filter(p => p.d <= eps).length;
  document.getElementById('distInfo').innerHTML =
    `m tetap = ${m}, n bervariasi 1..${N}. <span>${okCount} dari ${N}</span> titik memenuhi |x_m − x_n| ≤ ε=${eps.toFixed(1)}.`;
}

// ─── INIT ───
window.addEventListener('load', () => {
  drawSeq();
  drawDist();
  // Animate proof steps into view on scroll
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.2 });
  document.querySelectorAll('.proof-step').forEach(s => observer.observe(s));
  updateProgress();
});
window.addEventListener('resize', () => { drawSeq(); drawDist(); });
</script>
</body>
</html>
