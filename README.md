# Enterprise AI Recruitment & Sourcing Platform 💼🤖

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)

**Autonomous Candidate Resume Parsing, Skill Matching & AI Technical Interview Synthesizer**

---

## 🌟 Key Features

- **Automated Resume Parsing**: Extracts candidate skills, work history, and educational credentials into structured Pydantic v2 JSON.
- **Skill Match Score Algorithm**: Computes weighted match score against job requirement benchmarks (Python, FastAPI, React, PyTorch).
- **AI Interview Question Synthesizer**: Generates tailored technical screening questions based on candidate profile gaps.
- **Recruitment Pipeline Dashboard**: Interactive candidate status Kanban board and evaluation scoring.

---

## 📂 Monorepo Structure

```text
AI-Recruitment-Platform/
├── apps/
│   ├── api/                     # Python 3.12 FastAPI Backend
│   │   ├── app/domain/recruitment_sourcing/
│   │   │   ├── models.py        # Candidate & Job ORM Tables
│   │   │   ├── schemas.py       # Pydantic v2 Resume & Match Schemas
│   │   │   ├── service.py       # Resume Parser & Match Scoring Engine
│   │   │   └── router.py        # REST API Endpoints
│   │   └── main.py
│   └── web/                     # React 18 Frontend App
├── docker-compose.yml
└── README.md
```

---

## 🚀 Quick Start
```bash
# Backend
cd apps/api && pip install -r requirements.txt && python main.py

# Frontend
cd apps/web && npm install && npm run dev
```
