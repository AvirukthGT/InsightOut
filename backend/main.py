from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import BytesIO

app = FastAPI(title="InsightOut API")

# Allow your Vue frontend to call this backend (dev mode)
# IMPORTANT: CORS middleware must be added BEFORE routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods including OPTIONS for preflight
    allow_headers=["*"],  # Allow all headers
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "InsightOut API", "docs": "/docs", "health": "/health"}

@app.get("/health")
def health():
    return {"status": "ok", "service": "InsightOut API"}

@app.post("/profile")
async def profile(file: UploadFile = File(...)):
    filename = (file.filename or "").lower()
    content = await file.read()

    # Read file into pandas
    if filename.endswith(".csv"):
        df = pd.read_csv(BytesIO(content))
    elif filename.endswith(".xlsx") or filename.endswith(".xls"):
        df = pd.read_excel(BytesIO(content))
    else:
        return {"error": "Unsupported file type. Upload .csv or .xlsx"}

    # Basic profiling
    result = {
        "filename": file.filename,
        "rows": int(df.shape[0]),
        "cols": int(df.shape[1]),
        "columns": [
            {
                "name": col,
                "dtype": str(df[col].dtype),
                "missing": int(df[col].isna().sum()),
            }
            for col in df.columns
        ],
        "preview": df.head(20).to_dict(orient="records"),
    }
    return result

