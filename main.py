from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load CSV
df = pd.read_csv("marks.csv")
marks_dict = dict(zip(df["name"], df["marks"]))

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    result = [marks_dict.get(n, None) for n in name]
    return {"marks": result}

@app.get("/names")
def get_names():
    return {"available_names": list(marks_dict.keys())}
