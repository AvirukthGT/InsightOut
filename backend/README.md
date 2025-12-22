# InsightOut Backend

## Setup

1. Make sure you're in the backend directory
2. Activate your virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. Install dependencies (if not already installed):
   ```bash
   pip install fastapi uvicorn pandas openpyxl python-multipart
   ```

## Running the Server

From the backend directory, run:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Important:** 
- Make sure you're in the `backend` directory when running this command
- Make sure your virtual environment is activated
- Use `--host 0.0.0.0` to allow connections from other origins
- The server should start and show: `Uvicorn running on http://0.0.0.0:8000`
- You can test it by visiting: `http://localhost:8000/health` in your browser

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /health` - Health check endpoint
- `POST /profile` - Upload and analyze CSV/Excel file
  - Accepts: multipart/form-data with `file` field
  - Returns: File profiling data (rows, cols, columns info, preview)

## CORS

The backend is configured to allow requests from `http://localhost:5173` (Vite dev server).

