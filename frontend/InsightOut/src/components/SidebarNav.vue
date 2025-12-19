<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="logo-mark">IO</div>
      <span class="logo-text">InsightOut</span>
    </div>

    <nav class="sidebar-nav">
      <span class="sidebar-label">Navigation</span>
      <a href="#top" class="sidebar-link sidebar-link-active">Overview</a>
      <a href="#features" class="sidebar-link">Features</a>
      <a href="#how-it-works" class="sidebar-link">How it works</a>
      <a href="#docs" class="sidebar-link">Docs</a>
    </nav>

    <div class="sidebar-footer">
      <a
        href="https://github.com"
        target="_blank"
        rel="noreferrer"
        class="sidebar-link secondary"
      >
        GitHub
      </a>
      <button class="btn btn-primary sidebar-upload">
        Upload Dataset
      </button>
    </div>
  </aside>
</template>

<script setup>
// Presentational sidebar navigation for the landing layout.
</script>

<style scoped>
.sidebar {
  width: 240px;
  padding: 1.5rem 1.4rem;
  border-right: 1px solid rgba(15, 23, 42, 0.06);
  background: #f9faf7;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  position: sticky;
  top: 0;
  align-self: flex-start;
  min-height: 100vh;
}

.sidebar-header {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.logo-mark {
  width: 28px;
  height: 28px;
  border-radius: 999px;
  background: radial-gradient(circle at 30% 0%, #e5f2ff, #d0e5ff);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #1e293b;
  font-weight: 600;
  box-shadow: 0 3px 8px rgba(15, 23, 42, 0.15);
}

.logo-text {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  font-size: 0.84rem;
}

.sidebar-label {
  text-transform: uppercase;
  letter-spacing: 0.16em;
  font-size: 0.65rem;
  color: #9ca3af;
  margin-bottom: 0.4rem;
}

.sidebar-link {
  padding: 0.45rem 0.7rem;
  border-radius: 0.6rem;
  color: #4b5563;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.3rem;
  transition:
    background-color 0.16s ease,
    color 0.16s ease;
}

.sidebar-link:hover {
  background: rgba(148, 163, 184, 0.18);
  color: #111827;
}

.sidebar-link-active {
  background: #111827;
  color: #f9fafb;
}

.sidebar-link.secondary {
  margin-top: auto;
  padding-inline: 0;
  background: transparent;
}

.sidebar-footer {
  margin-top: auto;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.sidebar-upload {
  width: 100%;
}

@media (max-width: 1024px) {
  .sidebar {
    position: static;
    width: 100%;
    min-height: auto;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 4vw;
    border-right: none;
    border-bottom: 1px solid rgba(15, 23, 42, 0.06);
  }

  .sidebar-nav {
    flex-direction: row;
    align-items: center;
    gap: 0.75rem;
  }

  .sidebar-label {
    display: none;
  }

  .sidebar-link {
    padding-inline: 0.4rem;
    padding-block: 0.3rem;
  }

  .sidebar-footer {
    margin-top: 0;
    flex-direction: row;
    align-items: center;
  }

  .sidebar-upload {
    width: auto;
  }
}

@media (max-width: 480px) {
  .sidebar-nav {
    display: none;
  }
}
</style>


