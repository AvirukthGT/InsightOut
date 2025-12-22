"""Quick test script to verify backend is accessible"""
import requests

try:
    response = requests.get("http://localhost:8000/health")
    print(f"✅ Backend is accessible!")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except requests.exceptions.ConnectionError:
    print("❌ Cannot connect to backend. Make sure it's running on http://localhost:8000")
except Exception as e:
    print(f"❌ Error: {e}")

