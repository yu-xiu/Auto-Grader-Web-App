from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import subprocess
import uuid
from grader.run_tests import run_all_tests

app = FastAPI()

# Allow frontend local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeInput(BaseModel):
    code: str

@app.post("/grade")
async def grade_code(code: CodeInput):
    """
    Accepts raw code string from frontend.
    Saves to student_submission.py
    Executes the test runner
    Returns JSON results
    """

    submission_path = "grader/student_submission.py"

    with open(submission_path, "w") as f:
        f.write(code.code)

    try:
        results = run_all_tests()
        return {"status": "success", "results": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/upload")
async def upload_file(file: UploadFile):
    """
    Student uploads a .py file
    """
    if not file.filename.endswith(".py"):
        return {"error": "Only .py files are accepted"}

    submission_path = "grader/student_submission.py"
    content = await file.read()

    with open(submission_path, "wb") as f:
        f.write(content)

    try:
        results = run_all_tests()
        return {"status": "success", "results": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}
