# Auto-Grader-Web-App (FastAPI + React)
## Project Overview
This project implements an Auto Grader system for grading Python code submissions for a single programming problem: Knight Attack. 

Students can:
Read the problem description
Write or upload Python code
Submit the solution and automatically receive a test report
See PASS/FAIL results per test case and execution time

This project includes both:
Backend: FastAPI + automatic test runner
Frontend: React + Monaco Editor

### Project Context (Cloud Computing Class Project)
This project was developed as part of a Cloud Computing course, with the goal of learning how to design and build a complete end-to-end web application.
```
Designing a full frontend + backend architecture
Building a functional web application from scratch
Implementing a backend grading engine using Python and FastAPI
Creating a modern React frontend with an interactive code editor
Connecting the two sides through REST APIs
Preparing the system for deployment on cloud platforms such as Render and Vercel
```

## Tech Stack
### Frontend
```
React (Vite)
@monaco-editor/react
Axios
JavaScript
CSS3
```

### Backend
```
FastAPI
Uvicorn
Pydantic
python-multipart (file uploads)
CORS middleware
```

### Grading Engine
```
pytest
subprocess (isolated execution)
importlib (load student submission)
File I/O (save student code)
```

### Development Tools
```
Node.js + npm
Python virtual environment (.venv)
VS Code / Swagger UI (/docs)
Git / GitHub
```

```
auto-grader/
│
├── backend/
│   ├── main.py
│   ├── grader/
│   │   ├── run_tests.py
│   │   ├── test_knight_attack.py
│   │   ├── student_submission.py (runtime)
│   │   └── templates/
│   │       └── student_template.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/Editor.jsx
│   │   └── api.js
│   └── package.json
│
└── README.md
```
