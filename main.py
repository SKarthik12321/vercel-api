from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks data
with open("marks.json") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    return {"marks": [marks_data.get(n, 0) for n in name]}