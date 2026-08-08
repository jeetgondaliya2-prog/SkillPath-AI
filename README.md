from pathlib import Path

readme = r'''<div align="center">

# 🎯 SkillPath AI

### AI-Powered Career Guidance, Skill Gap Analysis & Personalized Learning Platform

<p>
  <b>Discover your career path. Understand your skill gaps. Learn what matters next.</b>
</p>

<p>
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-workflow">Workflow</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-api-documentation">API</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-future-scope">Future Scope</a>
</p>

<br>

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Mistral](https://img.shields.io/badge/Mistral-AI-000000?style=for-the-badge)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063?style=for-the-badge)
![REST API](https://img.shields.io/badge/API-REST-005571?style=for-the-badge)

</div>

---

## 🧭 Quick Navigation

- [🌟 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [💡 Solution](#-solution)
- [✨ Features](#-features)
- [🔄 Workflow](#-workflow)
- [🏗️ Architecture](#️-architecture)
- [📁 Project Structure](#-project-structure)
- [🧩 File-by-File Explanation](#-file-by-file-explanation)
- [🛠️ Technology Stack](#️-technology-stack)
- [🔌 API Documentation](#-api-documentation)
- [🎨 Frontend Design](#-frontend-design)
- [🤖 AI Layer](#-ai-layer)
- [📊 Example](#-example)
- [⚙️ Installation](#️-installation)
- [▶️ Running the Project](#️-running-the-project)
- [🧪 Testing](#-testing)
- [🔐 Security](#-security)
- [🚀 Future Scope](#-future-scope)
- [👨‍💻 Author](#-author)

---

# 🌟 Overview

**SkillPath AI** is an AI-powered career guidance platform built for students, freshers and early-career developers.

The platform takes a user's current profile and transforms it into an actionable career plan.

Instead of simply saying:

> "Learn Python, DSA and SQL."

SkillPath AI tries to answer:

> **"Based on your current skills and target role, what are you missing, how ready are you, what should you learn first, and which resources can help you learn it?"**

The application combines:

- 👤 Student profile analysis
- 🧠 Skill matching
- 🎯 Career recommendation
- 📊 Career readiness scoring
- ❌ Missing-skill detection
- 🗺️ AI-generated roadmap
- 📚 Personalized learning resources
- 📄 Resume analysis

---

# 🎯 Problem Statement

Students frequently face four major problems:

### 1. Career uncertainty

A student may know several technologies but still not know which career role fits those skills.

### 2. Invisible skill gaps

Students often learn technologies without comparing them against the actual requirements of their target role.

### 3. Generic roadmaps

Most learning roadmaps are one-size-fits-all and do not start from the student's current level.

### 4. Scattered learning resources

Even after identifying a missing skill, students still have to search multiple platforms to decide what to learn next.

### Our Goal

Build one platform that connects:

```text
Current Skills
      ↓
Career Goal
      ↓
Skill Gap
      ↓
Readiness
      ↓
Personalized Roadmap
      ↓
Learning Resources
