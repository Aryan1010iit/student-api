from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from CSV
df = pd.read_csv("marks.csv")
marks_dict = dict(zip(df["name"], df["marks"]))

@app.get("/names")
def get_names():
    return {"available_names": list(marks_dict.keys())}


@app.get("/api")
def get_marks(name: list[str] = []):
    result = [marks_dict.get(n, None) for n in name]
    return {"marks": result}
