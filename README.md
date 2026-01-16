<<<<<<< HEAD
# Project-CropSense
=======
# CropSense

**Scan Crops. Improve Yield. Reduce Waste.**

CropSense is a hackathon MVP web app designed to analyze crop health from images, providing farming recommendations and waste-to-value suggestions.

## Tech Stack

- **Frontend**: Next.js (App Router), Tailwind CSS, Axios
- **Backend**: FastAPI, Uvicorn
- **Deployment**: Vercel (Frontend), Render (Backend)

## 🚀 deployment-ready

### 1. Local Run Steps

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# Backend will run at http://localhost:8000
```

**Frontend:**
```bash
cd frontend
# Create .env.local file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
npm install
npm run dev
# Frontend will run at http://localhost:3000
```

### 2. Deploy Backend on Render

1. Create a new **Web Service** on Render connected to this repo.
2. Set **Root Directory** to `backend`.
3. Set **Build Command** to `pip install -r requirements.txt`.
4. Set **Start Command** to `uvicorn main:app --host 0.0.0.0 --port $PORT`.
5. Deploy. Copy the service URL (e.g., `https://cropsense-api.onrender.com`).

### 3. Deploy Frontend on Vercel

1. Import this repo into Vercel.
2. Set **Root Directory** to `frontend`.
3. Add Environment Variable:
   - `NEXT_PUBLIC_API_URL`: Your Render Backend URL (e.g., `https://cropsense-api.onrender.com`)
4. Deploy.

## Demo Instructions

For the hackathon demo, rename your image files to trigger specific results (Mock AI):

- `*healthy*` (e.g., `tomato_healthy.jpg`) -> **Healthy**
- `*blight*`, `*disease*`, `*mildew*` -> **Diseased**
- `*rotten*`, `*damaged*`, `*cut*` -> **Damaged**
- Any other name -> **Unknown conditon**

## Requirements

- Python 3.8+
- Node.js 18+
>>>>>>> 690fc24 (Initital Commit)
