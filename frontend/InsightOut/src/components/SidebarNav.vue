<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <span class="logo-text">InsightOut</span>
    </div>

    <nav class="sidebar-nav">
      <router-link to="/dashboard" class="nav-item" :class="{ 'nav-item-active': route.name === 'dashboard' }">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
          <polyline points="9 22 9 12 15 12 15 22"></polyline>
        </svg>
        <span>Dashboard</span>
      </router-link>

      <router-link to="/" class="nav-item" :class="{ 'nav-item-active': route.name === 'home' }">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="3" y="7" width="18" height="14" rx="2" ry="2"></rect>
          <line x1="8" y1="5" x2="16" y2="5"></line>
          <line x1="8" y1="9" x2="16" y2="9"></line>
          <line x1="8" y1="13" x2="14" y2="13"></line>
        </svg>
        <span>Tasks</span>
        <span class="nav-badge">2</span>
      </router-link>

      <router-link to="/" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
        </svg>
        <span>Activity</span>
      </router-link>

      <router-link to="/" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
          <circle cx="9" cy="7" r="4"></circle>
          <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
          <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
        </svg>
        <span>Features</span>
      </router-link>

      <router-link to="/" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="3"></circle>
          <path d="M12 1v6m0 6v6m11-7h-6m-6 0H1"></path>
        </svg>
        <span>Settings</span>
      </router-link>
    </nav>

    <div class="sidebar-section">
      <span class="section-label">Projects</span>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polyline>
        </svg>
        <span>Data Analysis</span>
        <span class="nav-badge">7</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
          <polyline points="17 6 23 6 23 12"></polyline>
        </svg>
        <span>Forecasting</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M12 6v6l4 2"></path>
        </svg>
        <span>Anomaly Detection</span>
      </a>
      <a href="#" class="nav-item">
        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
          <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
        </svg>
        <span>Reports</span>
      </a>
    </div>

    <div class="sidebar-section">
      <div class="section-header">
        <span class="section-label">Members</span>
        <button class="add-member-btn" aria-label="Add member">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
        </button>
      </div>
      <div class="member-item">
        <div class="member-avatar">
          <div class="avatar-initial">SP</div>
          <span class="online-dot"></span>
        </div>
        <div class="member-info">
          <span class="member-name">Sandra Perry</span>
          <span class="member-role">Product Manager</span>
        </div>
      </div>
      <div class="member-item">
        <div class="member-avatar">
          <div class="avatar-initial">AC</div>
          <span class="online-dot"></span>
        </div>
        <div class="member-info">
          <span class="member-name">Antony Cardenas</span>
          <span class="member-role">Data Analyst</span>
        </div>
      </div>
      <div class="member-item">
        <div class="member-avatar">
          <div class="avatar-initial">JC</div>
          <span class="online-dot"></span>
        </div>
        <div class="member-info">
          <span class="member-name">Jamal Connolly</span>
          <span class="member-role">ML Engineer</span>
        </div>
      </div>
      <div class="member-item">
        <div class="member-avatar">
          <div class="avatar-initial">CC</div>
          <span class="online-dot"></span>
        </div>
        <div class="member-info">
          <span class="member-name">Cara Carr</span>
          <span class="member-role">Data Scientist</span>
        </div>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
.sidebar {
  width: 260px;
  padding: 1.5rem 1rem;
  background: #ffffff;
  border-right: 1px solid rgba(0, 0, 0, 0.06);
  display: flex;
  flex-direction: column;
  gap: 2rem;
  position: sticky;
  top: 0;
  align-self: flex-start;
  min-height: 100vh;
  overflow-y: auto;
}

.sidebar-header {
  padding-bottom: 0.5rem;
}

.logo-text {
  font-size: 1.25rem;
  font-weight: 700;
  color: #111827;
  letter-spacing: -0.02em;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 0.75rem;
  border-radius: 0.5rem;
  color: #4b5563;
  text-decoration: none;
  font-size: 0.9rem;
  transition: background-color 0.15s ease, color 0.15s ease;
  position: relative;
}

.nav-item:hover {
  background: rgba(0, 0, 0, 0.04);
  color: #111827;
}

.nav-item-active {
  background: rgba(0, 0, 0, 0.06);
  color: #111827;
  font-weight: 500;
}

.nav-icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  stroke-width: 2;
}

.nav-item span:not(.nav-badge) {
  flex: 1;
}

.nav-badge {
  background: rgba(0, 0, 0, 0.08);
  color: #4b5563;
  font-size: 0.75rem;
  font-weight: 500;
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
  min-width: 20px;
  text-align: center;
}

.sidebar-section {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.25rem;
}

.section-label {
  font-size: 0.75rem;
  font-weight: 500;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0 0.75rem;
}

.add-member-btn {
  width: 18px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: none;
  color: #9ca3af;
  cursor: pointer;
  padding: 0;
  border-radius: 4px;
  transition: color 0.15s ease, background-color 0.15s ease;
}

.add-member-btn:hover {
  color: #4b5563;
  background: rgba(0, 0, 0, 0.04);
}

.add-member-btn svg {
  width: 14px;
  height: 14px;
}

.member-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 0.75rem;
  border-radius: 0.5rem;
  transition: background-color 0.15s ease;
}

.member-item:hover {
  background: rgba(0, 0, 0, 0.04);
}

.member-avatar {
  position: relative;
  flex-shrink: 0;
}

.avatar-initial {
  width: 32px;
  height: 32px;
  border-radius: 999px;
  background: linear-gradient(135deg, #e5e7eb, #d1d5db);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 600;
  color: #4b5563;
}

.online-dot {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: #22c55e;
  border: 2px solid #ffffff;
}

.member-info {
  display: flex;
  flex-direction: column;
  gap: 0.1rem;
  flex: 1;
  min-width: 0;
}

.member-name {
  font-size: 0.875rem;
  font-weight: 500;
  color: #111827;
  line-height: 1.2;
}

.member-role {
  font-size: 0.75rem;
  color: #6b7280;
  line-height: 1.2;
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
    border-bottom: 1px solid rgba(0, 0, 0, 0.06);
    gap: 1rem;
    overflow-x: auto;
  }

  .sidebar-header {
    padding-bottom: 0;
  }

  .sidebar-nav {
    flex-direction: row;
    gap: 0.5rem;
  }

  .sidebar-section {
    display: none;
  }

  .nav-item {
    white-space: nowrap;
  }
}

@media (max-width: 768px) {
  .sidebar-nav {
    gap: 0.25rem;
  }

  .nav-item span:not(.nav-badge) {
    display: none;
  }

  .nav-item {
    padding: 0.5rem;
    justify-content: center;
  }

  .nav-badge {
    position: absolute;
    top: 0;
    right: 0;
    transform: translate(25%, -25%);
  }
}
</style>
