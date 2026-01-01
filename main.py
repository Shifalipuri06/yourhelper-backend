from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI(
    title="YourHelper Research Backend",
    description="FastAPI backend for research text and PDF analysis",
    version="1.0.0"
)

# ---------- MODELS ----------
class AnalyzeRequest(BaseModel):
    text: str


# ---------- ROUTES ----------
@app.get("/")
def home():
    return {"message": "YourHelper backend is running"}


@app.post("/analyze")
def analyze_text(request: AnalyzeRequest):
    text = request.text

    # Dummy analysis (you can replace later with real logic)
    return {
        "identified_research_gaps": [
            "Lack of standardized LC–MS workflows",
            "Limited cross-lab validation",
            "Insufficient benchmarking against qPCR"
        ],
        "why_it_matters": "These gaps limit reproducibility and clinical translation.",
        "future_direction": "Develop standardized, isotope-labeled LC–MS pipelines."
    }


@app.post("/analyze-pdf")
async def analyze_pdf(file: UploadFile = File(...)):
    filename = file.filename

    # Dummy PDF handling (real parsing can be added later)
    return {
        "filename": filename,
        "identified_research_gaps": [
            "PDF-based LC–MS miRNA studies lack harmonized extraction protocols",
            "Scarce use of stable-isotope internal standards"
        ],
        "future_direction": "Standardized LC–MS pipelines validated across labs"
    }
