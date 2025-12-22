<template>
  <div class="dashboard">
    <header class="dashboard-header">
      <div class="header-content">
        <div class="header-text">
          <h1 class="dashboard-title">Dashboard</h1>
          <p class="dashboard-subtitle">Upload your data files to get started</p>
        </div>
        <div v-if="recentFiles.length > 0" class="stats-preview">
          <div class="stat-item">
            <span class="stat-value">{{ recentFiles.length }}</span>
            <span class="stat-label">Files</span>
          </div>
        </div>
      </div>
    </header>

    <main class="dashboard-main">
      <div class="upload-section">
        <div
          class="upload-zone"
          :class="{ 
            'upload-zone-dragover': isDragging, 
            'upload-zone-has-file': selectedFile,
            'upload-zone-pulse': !selectedFile && !isDragging
          }"
          @dragover.prevent="handleDragOver"
          @dragleave.prevent="handleDragLeave"
          @drop.prevent="handleDrop"
          @click="triggerFileInput"
        >
          <input
            ref="fileInput"
            type="file"
            accept=".csv,.xlsx,.xls"
            @change="handleFileSelect"
            class="file-input-hidden"
          />

          <div v-if="!selectedFile" class="upload-content">
            <div class="upload-icon-wrapper">
              <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="17 8 12 3 7 8"></polyline>
                <line x1="12" y1="3" x2="12" y2="15"></line>
              </svg>
            </div>
            <h2 class="upload-title">Drop your file here</h2>
            <p class="upload-subtitle">or click to browse</p>
            <div class="upload-formats">
              <span class="format-badge">CSV</span>
              <span class="format-badge">Excel</span>
            </div>
          </div>

          <div v-else class="file-preview">
            <div class="file-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
              </svg>
            </div>
            <div class="file-info">
              <h3 class="file-name">{{ selectedFile.name }}</h3>
              <p class="file-size">{{ formatFileSize(selectedFile.size) }}</p>
            </div>
            <button @click.stop="removeFile" class="remove-file-btn" aria-label="Remove file">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>
        </div>

        <transition name="fade-slide">
          <div v-if="selectedFile" class="upload-actions">
            <button @click="uploadFile" class="btn btn-primary btn-large" :disabled="isUploading">
              <span v-if="!isUploading">
                <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                </svg>
                Analyze Dataset
              </span>
              <span v-else class="uploading-text">
                <span class="spinner"></span>
                Processing...
              </span>
            </button>
            <button @click="removeFile" class="btn btn-ghost">Cancel</button>
          </div>
        </transition>

        <transition name="fade">
          <div v-if="uploadError" class="message message-error">
            <svg class="message-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="8" x2="12" y2="12"></line>
              <line x1="12" y1="16" x2="12.01" y2="16"></line>
            </svg>
            <span>{{ uploadError }}</span>
            <button @click="uploadError = null" class="message-close">×</button>
          </div>
        </transition>

        <transition name="fade">
          <div v-if="uploadSuccess" class="message message-success">
            <svg class="message-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
              <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            <span>{{ uploadSuccess }}</span>
            <button @click="uploadSuccess = null" class="message-close">×</button>
          </div>
        </transition>
      </div>

      <transition name="fade">
        <div v-if="recentFiles.length > 0" class="recent-section">
          <div class="section-header-row">
            <h2 class="section-title">Recent Files</h2>
            <button v-if="recentFiles.length > 0" @click="clearRecentFiles" class="clear-btn">
              Clear all
            </button>
          </div>
          <div class="recent-files">
            <transition-group name="list" tag="div">
              <div 
                v-for="file in recentFiles" 
                :key="file.id" 
                class="recent-file-card"
                @mouseenter="hoveredFile = file.id"
                @mouseleave="hoveredFile = null"
              >
                <div class="recent-file-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <polyline points="14 2 14 8 20 8"></polyline>
                  </svg>
                </div>
                <div class="recent-file-info">
                  <h3 class="recent-file-name">{{ file.name }}</h3>
                  <p class="recent-file-date">{{ formatDate(file.uploadedAt) }}</p>
                </div>
                <button @click="reanalyzeFile(file)" class="btn btn-ghost btn-small">
                  <svg class="btn-icon-small" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="23 4 23 10 17 10"></polyline>
                    <polyline points="1 20 1 14 7 14"></polyline>
                    <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
                  </svg>
                  Re-analyze
                </button>
              </div>
            </transition-group>
          </div>
        </div>
      </transition>

      <div v-if="recentFiles.length === 0 && !selectedFile" class="empty-state">
        <div class="empty-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
          </svg>
        </div>
        <p class="empty-text">No files uploaded yet</p>
        <p class="empty-subtext">Get started by uploading your first dataset</p>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { api } from '../services/api'

const fileInput = ref(null)
const selectedFile = ref(null)
const isDragging = ref(false)
const isUploading = ref(false)
const recentFiles = ref([])
const hoveredFile = ref(null)
const uploadError = ref(null)
const uploadSuccess = ref(null)
const analysisResult = ref(null)

const triggerFileInput = () => {
  fileInput.value?.click()
}

const handleFileSelect = (event) => {
  const file = event.target.files[0]
  if (file && isValidFileType(file)) {
    selectedFile.value = file
  } else {
    alert('Please select a valid CSV or Excel file (.csv, .xlsx, .xls)')
  }
}

const handleDragOver = (event) => {
  isDragging.value = true
  event.preventDefault()
}

const handleDragLeave = () => {
  isDragging.value = false
}

const handleDrop = (event) => {
  isDragging.value = false
  const file = event.dataTransfer.files[0]
  if (file && isValidFileType(file)) {
    selectedFile.value = file
  } else {
    alert('Please drop a valid CSV or Excel file (.csv, .xlsx, .xls)')
  }
}

const isValidFileType = (file) => {
  const validTypes = [
    'text/csv',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
  ]
  const validExtensions = ['.csv', '.xlsx', '.xls']
  const extension = '.' + file.name.split('.').pop().toLowerCase()
  
  return validTypes.includes(file.type) || validExtensions.includes(extension)
}

const formatFileSize = (bytes) => {
  if (bytes === 0) return '0 Bytes'
  const k = 1024
  const sizes = ['Bytes', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i]
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  })
}

const removeFile = () => {
  selectedFile.value = null
  uploadError.value = null
  uploadSuccess.value = null
  analysisResult.value = null
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}

const uploadFile = async () => {
  if (!selectedFile.value) return

  isUploading.value = true
  uploadError.value = null
  uploadSuccess.value = null
  analysisResult.value = null

  try {
    // Call backend API
    const result = await api.uploadFile(selectedFile.value)
    
    // Store analysis result
    analysisResult.value = result
    
    // Add to recent files
    recentFiles.value.unshift({
      id: Date.now(),
      name: selectedFile.value.name,
      size: selectedFile.value.size,
      uploadedAt: new Date().toISOString(),
      analysisResult: result
    })

    uploadSuccess.value = `File analyzed successfully! Found ${result.rows} rows and ${result.cols} columns.`

    // Reset file selection after a short delay
    setTimeout(() => {
      selectedFile.value = null
      if (fileInput.value) {
        fileInput.value.value = ''
      }
    }, 1500)
  } catch (error) {
    uploadError.value = error.message || 'Failed to upload and analyze file. Please try again.'
    console.error('Upload error:', error)
  } finally {
    isUploading.value = false
  }
}

const reanalyzeFile = (file) => {
  // In a real app, this would trigger re-analysis
  console.log('Re-analyzing file:', file.name)
}

const clearRecentFiles = () => {
  recentFiles.value = []
}
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
  background: #f8f9f6;
  display: flex;
  flex-direction: column;
}

.dashboard-header {
  padding: 2rem 3rem;
  background: #ffffff;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  transition: all 0.3s ease;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
}

.header-text {
  flex: 1;
}

.dashboard-title {
  font-size: 1.875rem;
  font-weight: 700;
  color: #111827;
  margin: 0 0 0.35rem;
  letter-spacing: -0.03em;
  background: linear-gradient(135deg, #111827 0%, #4b5563 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.dashboard-subtitle {
  font-size: 0.95rem;
  color: #6b7280;
  margin: 0;
  font-weight: 400;
}

.stats-preview {
  display: flex;
  gap: 1.5rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.2rem;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #4f46e5;
  line-height: 1;
}

.stat-label {
  font-size: 0.75rem;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.dashboard-main {
  flex: 1;
  padding: 3rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.upload-section {
  margin-bottom: 3rem;
}

.upload-zone {
  background: #ffffff;
  border: 2px dashed rgba(79, 70, 229, 0.2);
  border-radius: 1.25rem;
  padding: 4.5rem 2rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.upload-zone::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(79, 70, 229, 0.05), transparent);
  transition: left 0.5s ease;
}

.upload-zone:hover::before {
  left: 100%;
}

.upload-zone:hover {
  border-color: rgba(79, 70, 229, 0.4);
  background: rgba(79, 70, 229, 0.02);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(79, 70, 229, 0.12);
}

.upload-zone-pulse {
  animation: subtle-pulse 3s ease-in-out infinite;
}

@keyframes subtle-pulse {
  0%, 100% {
    border-color: rgba(79, 70, 229, 0.2);
  }
  50% {
    border-color: rgba(79, 70, 229, 0.35);
  }
}

.upload-zone-dragover {
  border-color: #4f46e5;
  background: rgba(79, 70, 229, 0.08);
  transform: scale(1.02);
  box-shadow: 0 12px 32px rgba(79, 70, 229, 0.2);
}

.upload-zone-dragover::before {
  display: none;
}

.upload-zone-has-file {
  border-style: solid;
  border-color: rgba(79, 70, 229, 0.3);
  background: rgba(79, 70, 229, 0.03);
  padding: 2rem;
  cursor: default;
}

.file-input-hidden {
  position: absolute;
  width: 0;
  height: 0;
  opacity: 0;
  pointer-events: none;
}

.upload-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  position: relative;
  z-index: 1;
}

.upload-icon-wrapper {
  width: 80px;
  height: 80px;
  border-radius: 1rem;
  background: linear-gradient(135deg, rgba(79, 70, 229, 0.1), rgba(34, 197, 94, 0.1));
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.5rem;
  transition: transform 0.3s ease;
}

.upload-zone:hover .upload-icon-wrapper {
  transform: scale(1.05) rotate(5deg);
}

.upload-icon {
  width: 40px;
  height: 40px;
  color: #4f46e5;
  transition: all 0.3s ease;
}

.upload-zone:hover .upload-icon {
  color: #6366f1;
  transform: translateY(-4px);
}

.upload-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #111827;
  margin: 0;
  letter-spacing: -0.02em;
}

.upload-subtitle {
  font-size: 1rem;
  color: #6b7280;
  margin: 0;
  font-weight: 400;
}

.upload-formats {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.75rem;
  justify-content: center;
}

.format-badge {
  padding: 0.35rem 0.85rem;
  border-radius: 0.5rem;
  background: rgba(79, 70, 229, 0.1);
  color: #4f46e5;
  font-size: 0.8rem;
  font-weight: 500;
  transition: all 0.2s ease;
}

.upload-zone:hover .format-badge {
  background: rgba(79, 70, 229, 0.15);
  transform: translateY(-1px);
}

.file-preview {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  text-align: left;
  position: relative;
  z-index: 1;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.file-icon {
  width: 56px;
  height: 56px;
  border-radius: 0.75rem;
  background: linear-gradient(135deg, rgba(79, 70, 229, 0.15), rgba(34, 197, 94, 0.15));
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: #4f46e5;
  transition: transform 0.2s ease;
}

.file-icon:hover {
  transform: scale(1.05);
}

.file-icon svg {
  width: 28px;
  height: 28px;
}

.file-info {
  flex: 1;
  min-width: 0;
}

.file-name {
  font-size: 1.05rem;
  font-weight: 600;
  color: #111827;
  margin: 0 0 0.3rem;
  word-break: break-word;
}

.file-size {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
}

.remove-file-btn {
  width: 40px;
  height: 40px;
  border-radius: 0.5rem;
  border: none;
  background: rgba(0, 0, 0, 0.04);
  color: #6b7280;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.remove-file-btn:hover {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  transform: rotate(90deg);
}

.remove-file-btn svg {
  width: 18px;
  height: 18px;
}

.upload-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  margin-top: 1.5rem;
}

.btn {
  border-radius: 0.625rem;
  border: none;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.75rem 1.5rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  white-space: nowrap;
  position: relative;
  overflow: hidden;
}

.btn::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  transform: translate(-50%, -50%);
  transition: width 0.6s, height 0.6s;
}

.btn:active::before {
  width: 300px;
  height: 300px;
}

.btn-primary {
  background: linear-gradient(135deg, #4f46e5, #22c55e);
  color: #ffffff;
  box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35);
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(79, 70, 229, 0.45);
}

.btn-primary:active:not(:disabled) {
  transform: translateY(0);
}

.btn-primary:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.btn-ghost {
  background: transparent;
  color: #4b5563;
  border: 1.5px solid rgba(0, 0, 0, 0.1);
}

.btn-ghost:hover {
  background: rgba(0, 0, 0, 0.05);
  border-color: rgba(0, 0, 0, 0.15);
  transform: translateY(-1px);
}

.btn-large {
  padding: 0.875rem 2rem;
  font-size: 1rem;
  font-weight: 600;
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
}

.btn-icon {
  width: 18px;
  height: 18px;
}

.btn-icon-small {
  width: 14px;
  height: 14px;
}

.uploading-text {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: #ffffff;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.recent-section {
  margin-top: 3rem;
  animation: fadeIn 0.4s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.section-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
}

.section-title {
  font-size: 1.375rem;
  font-weight: 600;
  color: #111827;
  margin: 0;
  letter-spacing: -0.02em;
}

.clear-btn {
  background: transparent;
  border: none;
  color: #6b7280;
  font-size: 0.875rem;
  cursor: pointer;
  padding: 0.4rem 0.8rem;
  border-radius: 0.5rem;
  transition: all 0.2s ease;
}

.clear-btn:hover {
  background: rgba(0, 0, 0, 0.04);
  color: #111827;
}

.recent-files {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.recent-file-card {
  background: #ffffff;
  border: 1.5px solid rgba(0, 0, 0, 0.06);
  border-radius: 0.875rem;
  padding: 1.25rem 1.5rem;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.recent-file-card:hover {
  border-color: rgba(79, 70, 229, 0.3);
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.1);
  transform: translateX(4px);
}

.recent-file-icon {
  width: 44px;
  height: 44px;
  border-radius: 0.625rem;
  background: linear-gradient(135deg, rgba(79, 70, 229, 0.12), rgba(34, 197, 94, 0.12));
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: #4f46e5;
  transition: transform 0.2s ease;
}

.recent-file-card:hover .recent-file-icon {
  transform: scale(1.1) rotate(5deg);
}

.recent-file-icon svg {
  width: 22px;
  height: 22px;
}

.recent-file-info {
  flex: 1;
  min-width: 0;
}

.recent-file-name {
  font-size: 0.95rem;
  font-weight: 500;
  color: #111827;
  margin: 0 0 0.25rem;
  word-break: break-word;
}

.recent-file-date {
  font-size: 0.8rem;
  color: #6b7280;
  margin: 0;
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #9ca3af;
}

.empty-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto 1.5rem;
  opacity: 0.4;
}

.empty-icon svg {
  width: 100%;
  height: 100%;
}

.empty-text {
  font-size: 1.125rem;
  font-weight: 500;
  color: #6b7280;
  margin: 0 0 0.5rem;
}

.empty-subtext {
  font-size: 0.9rem;
  color: #9ca3af;
  margin: 0;
}

/* Transitions */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.list-enter-active {
  transition: all 0.3s ease;
}

.list-leave-active {
  transition: all 0.25s ease;
}

.list-enter-from {
  opacity: 0;
  transform: translateX(-20px);
}

.list-leave-to {
  opacity: 0;
  transform: translateX(20px);
}

.list-move {
  transition: transform 0.3s ease;
}

/* Message styles */
.message {
  margin-top: 1rem;
  padding: 1rem 1.25rem;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.9rem;
  animation: slideDown 0.3s ease;
  position: relative;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.message-error {
  background: rgba(239, 68, 68, 0.1);
  border: 1.5px solid rgba(239, 68, 68, 0.3);
  color: #dc2626;
}

.message-success {
  background: rgba(34, 197, 94, 0.1);
  border: 1.5px solid rgba(34, 197, 94, 0.3);
  color: #16a34a;
}

.message-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.message-close {
  margin-left: auto;
  background: transparent;
  border: none;
  color: inherit;
  font-size: 1.5rem;
  line-height: 1;
  cursor: pointer;
  padding: 0;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.25rem;
  transition: background-color 0.2s ease;
  opacity: 0.7;
}

.message-close:hover {
  opacity: 1;
  background: rgba(0, 0, 0, 0.05);
}

@media (max-width: 768px) {
  .dashboard-header {
    padding: 1.5rem 1.5rem;
  }

  .header-content {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .dashboard-main {
    padding: 1.5rem;
  }

  .upload-zone {
    padding: 3rem 1.5rem;
  }

  .upload-zone-has-file {
    padding: 1.5rem;
  }

  .upload-actions {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }

  .section-header-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.75rem;
  }
}
</style>
