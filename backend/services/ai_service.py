import google.generativeai as genai
import os
import json
from PIL import Image
import io

# Configure the API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

async def analyze_crop_image(image_bytes: bytes, filename: str):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        
        prompt = """
        You are an expert agriculturalist and plant pathologist. Analyze this image of a crop.
        Return a JSON object with the following structure:
        {
            "status": "Healthy" | "Diseased" | "Damaged" | "Unknown",
            "confidence": float (0.0 to 1.0),
            "recommendations": [list of strings],
            "waste_to_value": [list of strings]
        }
        
        If the image is not a plant or crop, set status to "Unknown" and provide a helpful message in recommendations.
        For "waste_to_value", suggest ways to use the crop waste or damaged parts (e.g., composting, animal feed, biofuel).
        """
        
        response = model.generate_content([prompt, image])
        
        # Clean up the response to ensure valid JSON
        text = response.text.replace("```json", "").replace("```", "").strip()
        result = json.loads(text)
        
        # Add filename to result
        result["filename"] = filename
        return result
        
    except Exception as e:
        print(f"Error analyzing image: {e}")
        return {
            "filename": filename,
            "status": "Error",
            "confidence": 0.0,
            "recommendations": ["Error analyzing image. Please try again."],
            "waste_to_value": []
        }
