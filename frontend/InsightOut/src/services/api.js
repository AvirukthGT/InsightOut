const API_BASE_URL = 'http://localhost:8000'

export const api = {
  async uploadFile(file) {
    const formData = new FormData()
    formData.append('file', file)

    try {
      const response = await fetch(`${API_BASE_URL}/profile`, {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        const error = await response.json().catch(() => ({ 
          error: `HTTP error! status: ${response.status}` 
        }))
        throw new Error(error.error || `Server error: ${response.status}`)
      }

      return await response.json()
    } catch (error) {
      // Handle network errors (CORS, connection refused, etc.)
      if (error.name === 'TypeError' && error.message.includes('fetch')) {
        throw new Error('Failed to connect to backend. Make sure the server is running on http://localhost:8000')
      }
      throw error
    }
  },

  async healthCheck() {
    try {
      const response = await fetch(`${API_BASE_URL}/health`)
      if (!response.ok) {
        throw new Error('Backend health check failed')
      }
      return await response.json()
    } catch (error) {
      if (error.name === 'TypeError' && error.message.includes('fetch')) {
        throw new Error('Cannot reach backend server. Make sure it\'s running on http://localhost:8000')
      }
      throw error
    }
  },
}

