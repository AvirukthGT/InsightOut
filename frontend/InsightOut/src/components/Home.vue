<template>
  <div class="home-page">
    <!-- Top bar for actions on larger screens -->
    <header class="topbar">
      <div class="topbar-title">
        <span class="topbar-eyebrow">Landing</span>
        <span class="topbar-heading">InsightOut overview</span>
      </div>
      <router-link to="/dashboard" class="btn btn-primary topbar-upload">
        Upload Dataset
      </router-link>
    </header>

    <main>
      <!-- ===================== HERO ===================== -->
      <section class="hero">
        <div class="hero-content">
          <p class="eyebrow">Data insights, instantly</p>
          <h1 class="hero-title">
            Upload data. Detect anomalies. See the future.
          </h1>
          <p class="hero-subtitle">
            Drag and drop any CSV or Excel file to instantly uncover descriptive statistics,
            outliers, and time‑series forecasts — without writing a single line of code.
          </p>
          <div class="hero-actions">
            <router-link to="/dashboard" class="btn btn-primary hero-primary">
              Upload CSV / Excel
            </router-link>
            <button class="btn btn-ghost">
              View Demo
            </button>
          </div>

          <div class="hero-meta">
            <span class="meta-pill">Supports CSV &amp; Excel</span>
            <span class="meta-dot"></span>
            <span class="meta-pill">Anomaly detection &amp; forecasting built‑in</span>
          </div>
        </div>

        <div class="hero-visual" aria-hidden="true">
          <div class="hero-card hero-card-main">
            <div class="hero-card-header">
              <span class="hero-card-title">Anomaly Overview</span>
              <span class="hero-card-badge">Live preview</span>
            </div>
            <div class="hero-chart">
              <div class="chart-bars">
                <div class="bar" style="height: 45%"></div>
                <div class="bar" style="height: 70%"></div>
                <div class="bar bar-anomaly" style="height: 95%"></div>
                <div class="bar" style="height: 60%"></div>
                <div class="bar" style="height: 40%"></div>
              </div>
              <div class="chart-footer">
                <span>Detected anomalies</span>
                <span class="chart-highlight">7 events</span>
              </div>
            </div>
          </div>

          <div class="hero-card hero-card-secondary">
            <div class="metric">
              <span class="metric-label">Forecast horizon</span>
              <span class="metric-value">30 days</span>
            </div>
            <div class="metric">
              <span class="metric-label">Explained variance</span>
              <span class="metric-value">92%</span>
            </div>
          </div>

          <div class="hero-bg-ring"></div>
        </div>
      </section>

      <!-- Anchor target for Docs (placeholder) -->
      <section id="docs" class="anchor-spacer" aria-hidden="true"></section>

      <!-- ===================== FEATURE CARDS ===================== -->
      <section id="features" class="section section-features">
        <header class="section-header">
          <h2>Designed for modern data teams</h2>
          <p>
            InsightOut turns raw tabular data into clear narratives, surfacing patterns,
            anomalies, and forecasts in a few clicks.
          </p>
        </header>

        <div class="features-grid">
          <article class="card feature-card">
            <div class="icon-circle">
              <span class="icon-dot"></span>
            </div>
            <h3>Automated EDA</h3>
            <p>
              Instant descriptive statistics, distributions, and correlations — automatically
              generated for every upload.
            </p>
          </article>

          <article class="card feature-card">
            <div class="icon-circle">
              <span class="icon-spark"></span>
            </div>
            <h3>Anomaly Detection</h3>
            <p>
              Detect outliers and shifts using robust algorithms that adapt to your data's shape
              and seasonality.
            </p>
          </article>

          <article class="card feature-card">
            <div class="icon-circle">
              <span class="icon-trend"></span>
            </div>
            <h3>Forecasting</h3>
            <p>
              Generate time‑series forecasts with confidence bands and scenario views in seconds.
            </p>
          </article>

          <article class="card feature-card">
            <div class="icon-circle">
              <span class="icon-grid"></span>
            </div>
            <h3>Interactive Dashboards</h3>
            <p>
              Explore metrics, anomalies, and segment filters in a lightweight, shareable
              analytics workspace.
            </p>
          </article>
        </div>
      </section>

      <!-- ===================== HOW IT WORKS ===================== -->
      <section id="how-it-works" class="section section-how">
        <header class="section-header">
          <h2>How InsightOut works</h2>
          <p>
            From raw data to clear decisions in four simple steps.
          </p>
        </header>

        <ol class="steps">
          <li class="step">
            <div class="step-badge">1</div>
            <h3>Upload dataset</h3>
            <p>Drag and drop your CSV or Excel file, or connect a data source.</p>
          </li>
          <li class="step">
            <div class="step-badge">2</div>
            <h3>Analyze automatically</h3>
            <p>InsightOut profiles your data, detects schema issues, and runs EDA.</p>
          </li>
          <li class="step">
            <div class="step-badge">3</div>
            <h3>Visualize anomalies</h3>
            <p>Outliers, changepoints, and anomalies are highlighted across charts.</p>
          </li>
          <li class="step">
            <div class="step-badge">4</div>
            <h3>Forecast trends</h3>
            <p>Generate forecasts and auto‑generated narrative insights to share.</p>
          </li>
        </ol>
      </section>

      <!-- ===================== CTA ===================== -->
      <section class="section section-cta">
        <div class="cta-card">
          <h2>Ready to see what's hiding in your data?</h2>
          <p>
            Upload a dataset and let InsightOut surface anomalies, patterns, and forecasts
            in under a minute.
          </p>
          <router-link to="/dashboard" class="btn btn-primary btn-large">
            Upload Dataset
          </router-link>
        </div>
      </section>
    </main>

    <!-- ===================== FOOTER ===================== -->
    <footer class="footer">
      <div class="footer-left">
        <span class="footer-brand">InsightOut</span>
        <span class="footer-dot">·</span>
        <span>© 2025</span>
      </div>
      <div class="footer-links">
        <a href="https://github.com" target="_blank" rel="noreferrer">GitHub</a>
        <a href="https://linkedin.com" target="_blank" rel="noreferrer">LinkedIn</a>
        <a href="mailto:contact@insightout.app">Contact</a>
      </div>
    </footer>
  </div>
</template>

<script setup>
// Landing page component
</script>

<style scoped>
.home-page {
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* ===================== TOP BAR ===================== */

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.1rem 5vw 0.4rem;
}

.topbar-title {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.topbar-eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.65rem;
  color: #9ca3af;
}

.topbar-heading {
  font-size: 0.95rem;
  font-weight: 500;
  color: #111827;
}

.topbar-upload {
  display: inline-flex;
  text-decoration: none;
}

/* ===================== BUTTONS ===================== */

.btn {
  border-radius: 999px;
  border: none;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.55rem 1.25rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  transition:
    background-color 0.18s ease,
    color 0.18s ease,
    box-shadow 0.18s ease,
    transform 0.08s ease;
  white-space: nowrap;
  text-decoration: none;
}

.btn-primary {
  background: linear-gradient(135deg, #4f46e5, #22c55e);
  color: #f9fafb;
  box-shadow: 0 14px 30px rgba(15, 23, 42, 0.18);
}

.btn-primary:hover {
  box-shadow: 0 18px 36px rgba(15, 23, 42, 0.22);
  transform: translateY(-1px);
}

.btn-ghost {
  background: transparent;
  color: #111827;
  border: 1px solid rgba(148, 163, 184, 0.5);
}

.btn-ghost:hover {
  background: rgba(148, 163, 184, 0.08);
}

.btn-large {
  padding: 0.8rem 1.8rem;
  font-size: 0.95rem;
}

/* ===================== HERO ===================== */

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr);
  gap: 3rem;
  padding: 2.4rem 5vw 3rem;
  align-items: center;
}

.hero-content {
  max-width: 560px;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.7rem;
  color: #6b7280;
  margin-bottom: 0.75rem;
}

.hero-title {
  font-size: clamp(2.2rem, 3vw, 2.7rem);
  line-height: 1.1;
  margin: 0 0 1rem;
  letter-spacing: -0.04em;
}

.hero-subtitle {
  font-size: 0.98rem;
  line-height: 1.6;
  color: #4b5563;
  margin-bottom: 1.6rem;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-bottom: 1.25rem;
}

.hero-primary {
  padding-inline: 1.7rem;
}

.hero-meta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8rem;
  color: #6b7280;
}

.meta-pill {
  padding: 0.25rem 0.7rem;
  border-radius: 999px;
  background: rgba(148, 163, 184, 0.18);
}

.meta-dot {
  width: 4px;
  height: 4px;
  border-radius: 999px;
  background: #9ca3af;
}

/* Hero visual */

.hero-visual {
  position: relative;
  min-height: 260px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-card {
  border-radius: 1.25rem;
  background: #fdfdfb;
  border: 1px solid rgba(15, 23, 42, 0.05);
  box-shadow:
    0 18px 45px rgba(15, 23, 42, 0.18),
    0 0 0 1px rgba(255, 255, 255, 0.4) inset;
}

.hero-card-main {
  width: 320px;
  padding: 1.25rem 1.2rem 1.1rem;
  position: relative;
  z-index: 2;
}

.hero-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.hero-card-title {
  font-size: 0.85rem;
  font-weight: 600;
}

.hero-card-badge {
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  padding: 0.2rem 0.55rem;
  border-radius: 999px;
  background: #eef2ff;
  color: #4f46e5;
}

.hero-chart {
  background: #f2f4f1;
  border-radius: 0.9rem;
  padding: 0.75rem 0.9rem 0.7rem;
}

.chart-bars {
  display: flex;
  align-items: flex-end;
  gap: 0.35rem;
  height: 90px;
  margin-bottom: 0.55rem;
}

.bar {
  flex: 1;
  border-radius: 999px;
  background: linear-gradient(180deg, #d4d4d8, #a1a1aa);
  opacity: 0.85;
}

.bar-anomaly {
  background: linear-gradient(180deg, #f97316, #ea580c);
  box-shadow: 0 0 0 4px rgba(248, 153, 56, 0.16);
}

.chart-footer {
  display: flex;
  justify-content: space-between;
  font-size: 0.72rem;
  color: #4b5563;
}

.chart-highlight {
  font-weight: 600;
  color: #111827;
}

.hero-card-secondary {
  position: absolute;
  right: 5%;
  bottom: -8%;
  padding: 0.8rem 0.9rem;
  width: 180px;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
  background: #fdfdfb;
}

.metric {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.metric-label {
  font-size: 0.71rem;
  color: #6b7280;
}

.metric-value {
  font-size: 0.86rem;
  font-weight: 600;
}

.hero-bg-ring {
  position: absolute;
  inset: 8%;
  border-radius: 999px;
  background: radial-gradient(circle at 20% 0%, rgba(79, 70, 229, 0.16), transparent),
    radial-gradient(circle at 80% 100%, rgba(34, 197, 94, 0.13), transparent);
  opacity: 0.65;
  filter: blur(6px);
  z-index: 0;
}

/* ===================== SECTIONS ===================== */

.section {
  padding: 3rem 5vw;
}

.section-header {
  max-width: 620px;
  margin-bottom: 2rem;
}

.section-header h2 {
  font-size: 1.4rem;
  margin-bottom: 0.4rem;
  letter-spacing: -0.03em;
}

.section-header p {
  font-size: 0.95rem;
  color: #4b5563;
}

/* ===================== FEATURES ===================== */

.section-features {
  padding-top: 1rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1.25rem;
}

.card {
  background: #fdfdfb;
  border-radius: 1rem;
  border: 1px solid rgba(15, 23, 42, 0.04);
  box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08);
}

.feature-card {
  padding: 1.2rem 1.2rem 1.3rem;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}

.feature-card h3 {
  font-size: 0.98rem;
}

.feature-card p {
  font-size: 0.86rem;
  color: #4b5563;
  line-height: 1.5;
}

.icon-circle {
  width: 34px;
  height: 34px;
  border-radius: 999px;
  background: #eef2ff;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.15rem;
}

.icon-dot,
.icon-spark,
.icon-trend,
.icon-grid {
  width: 14px;
  height: 14px;
  border-radius: 6px;
  background: linear-gradient(135deg, #4f46e5, #22c55e);
  position: relative;
}

.icon-spark::after {
  content: "";
  position: absolute;
  inset: 3px;
  border-radius: 999px;
  border: 1.5px solid rgba(248, 250, 252, 0.9);
  transform: rotate(-15deg);
}

.icon-trend::before {
  content: "";
  position: absolute;
  left: 2px;
  right: 2px;
  bottom: 3px;
  height: 1.5px;
  background: rgba(248, 250, 252, 0.9);
}

.icon-trend::after {
  content: "";
  position: absolute;
  width: 4px;
  height: 4px;
  border-top: 1.5px solid rgba(248, 250, 252, 0.9);
  border-right: 1.5px solid rgba(248, 250, 252, 0.9);
  right: 2px;
  top: 3px;
  transform: rotate(45deg);
}

.icon-grid::before,
.icon-grid::after {
  content: "";
  position: absolute;
  inset: 3px;
  border-radius: 3px;
  border: 1.5px solid rgba(248, 250, 252, 0.9);
}

/* ===================== HOW IT WORKS ===================== */

.section-how {
  padding-top: 1.5rem;
}

.steps {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1.2rem;
}

.step {
  background: #fdfdfb;
  border-radius: 1rem;
  padding: 1.15rem 1.1rem 1.2rem;
  border: 1px dashed rgba(148, 163, 184, 0.45);
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.step-badge {
  width: 26px;
  height: 26px;
  border-radius: 999px;
  background: #111827;
  color: #f9fafb;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  margin-bottom: 0.2rem;
}

.step h3 {
  font-size: 0.95rem;
}

.step p {
  font-size: 0.85rem;
  color: #4b5563;
  line-height: 1.5;
}

/* ===================== CTA ===================== */

.section-cta {
  padding-top: 1rem;
  padding-bottom: 3.5rem;
}

.cta-card {
  margin: 0 auto;
  max-width: 640px;
  text-align: center;
  padding: 2.1rem 2rem 2.25rem;
  border-radius: 1.5rem;
  background: radial-gradient(circle at 0% 0%, #eef2ff, transparent 60%),
    radial-gradient(circle at 100% 100%, #dcfce7, transparent 60%), #fdfdfb;
  box-shadow:
    0 20px 45px rgba(15, 23, 42, 0.18),
    0 0 0 1px rgba(255, 255, 255, 0.7) inset;
}

.cta-card h2 {
  font-size: 1.4rem;
  margin-bottom: 0.4rem;
  letter-spacing: -0.03em;
}

.cta-card p {
  font-size: 0.95rem;
  color: #4b5563;
  margin-bottom: 1.4rem;
}

/* ===================== FOOTER ===================== */

.footer {
  margin-top: auto;
  padding: 1.4rem 5vw 1.8rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.8rem;
  color: #6b7280;
  border-top: 1px solid rgba(15, 23, 42, 0.05);
}

.footer-left {
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

.footer-brand {
  font-weight: 500;
}

.footer-links {
  display: flex;
  gap: 1rem;
}

.footer-links a {
  color: inherit;
  text-decoration: none;
}

.footer-links a:hover {
  color: #111827;
}

.footer-dot {
  opacity: 0.6;
}

/* ===================== MISC ===================== */

.anchor-spacer {
  height: 1px;
}

/* ===================== RESPONSIVE ===================== */

@media (max-width: 1024px) {
  .hero {
    grid-template-columns: minmax(0, 1.1fr);
    padding-top: 2.5rem;
  }

  .hero-visual {
    order: -1;
    margin-bottom: 1.25rem;
  }

  .features-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .steps {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 2.25rem 4vw 2.4rem;
  }

  .section {
    padding-inline: 4vw;
  }

  .features-grid {
    grid-template-columns: minmax(0, 1fr);
  }

  .steps {
    grid-template-columns: minmax(0, 1fr);
  }

  .cta-card {
    padding-inline: 1.5rem;
  }

  .footer {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.6rem;
  }
}

@media (max-width: 480px) {
  .hero-actions {
    flex-direction: column;
    align-items: stretch;
  }

  .hero-primary,
  .btn-ghost {
    width: 100%;
    justify-content: center;
  }
}
</style>

