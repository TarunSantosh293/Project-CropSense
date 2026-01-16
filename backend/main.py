from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from services.ai_service import analyze_crop_image
from database import supabase

load_dotenv()

app = FastAPI(title="CropSense API")

# CORS Setup
origins = ["*"]  # Allow all for hackathon simplicity

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisResult(BaseModel):
    filename: str
    status: str
    confidence: float
    recommendations: list[str]
    waste_to_value: list[str]

@app.get("/")
def read_root():
    return {"message": "CropSense API running"}

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_image(file: UploadFile = File(...)):
    filename = file.filename.lower()
    
    # Real AI Analysis
    content = await file.read()
    analysis = await analyze_crop_image(content, filename)
    
    status = analysis.get("status", "Unknown")
    confidence = analysis.get("confidence", 0.0)
    recommendations = analysis.get("recommendations", [])
    waste_to_value = analysis.get("waste_to_value", [])

    # Save to Supabase
    if supabase:
        try:
            supabase.table("analyses").insert({
                "filename": filename,
                "status": status,
                "confidence": confidence,
                "recommendations": recommendations,
                "waste_to_value": waste_to_value
            }).execute()
        except Exception as e:
            print(f"Error saving to Supabase: {e}")

    return AnalysisResult(
        filename=file.filename,
        status=status,
        confidence=confidence,
        recommendations=recommendations,
        waste_to_value=waste_to_value
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
