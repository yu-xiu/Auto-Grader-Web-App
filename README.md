# Auto-Grader-Web-App (FastAPI + React)
## Project Overview
This project implements an Auto Grader system for grading Python code submissions for a single programming problem: Knight Attack. 

Website link:
https://auto-grader-web-app.vercel.app/

Students can:
Read the problem description
Write or upload Python code
Submit the solution and automatically receive a test report
See PASS/FAIL results per test case and execution time

This project includes both:
Backend: FastAPI + automatic test runner
Frontend: React + Monaco Editor


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

### Deployment
```
Vercel - Frontend
Render - Backend 
```
## Architecture Diagram
<img src="./assets/auto-grader-architecture-flowchart.png" width="200" />

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
