<template>
  <div class="page">
    <!-- ===================== LEFT SIDEBAR ===================== -->
    <SidebarNav />

    <!-- ===================== MAIN CONTENT COLUMN ===================== -->
    <div class="main-column">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import SidebarNav from './components/SidebarNav.vue'
</script>

<style scoped>
.page {
  min-height: 100vh;
  background: #f8f9f6;
  color: #101214;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI",
    sans-serif;
  display: flex;
  flex-direction: row;
}

.main-column {
  flex: 1;
  display: flex;
  flex-direction: column;
}
</style>
