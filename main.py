from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv

app = FastAPI()

# Enable CORS for Railway deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def read_students(class_list: Optional[List[str]] = Query(None, alias="class")):
    students = []
    # Use a relative path so it finds the file on the server
    with open('q-fastapi_.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"studentid": int(row['studentid']), "class": row['class']})
    
    if not class_list:
        return {"students": students}
        
    filtered = [s for s in students if s["class"] in class_list]
    return {"students": filtered}
