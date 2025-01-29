<div align="center">

# 🤖 AI-Powered Technical Recruitment System

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.crewai.com/)
[![Groq](https://img.shields.io/badge/Groq-4BAAEE?style=for-the-badge)](https://groq.com/)

**Transform Your Technical Recruitment Process with AI-Powered Analysis & Dynamic Interviews**

[Features](#features) •
[Installation](#installation) •
[Usage](#usage) •
[Documentation](#documentation) •
[Contributing](#contributing)

</div>

---

## 🌟 Overview

An intelligent system that revolutionizes technical recruitment by:
- 📄 Analyzing CVs with detailed feedback and recommendations
- 🎯 Creating dynamic, depth-first technical interviews
- 🤔 Adapting questions based on candidate responses
- 📊 Progressive technical depth assessment
- 🚀 Google-style interview experience

## ✨ Features

### 1️⃣ Smart CV Analysis
```python
# CV Analysis
POST /api/v1/analyze-cv
# Upload a CV in PDF format for comprehensive analysis

# Job Recommendations
POST /api/v1/recommend-jobs
# Get personalized job recommendations based on CV analysis
```

Example Job Recommendations Response:
```json
{
    "recommendations": [
        {
            "title": "Senior Full Stack Developer",
            "match_score": 0.92,
            "key_matches": [
                "JavaScript/TypeScript",
                "React",
                "Node.js",
                "Full Stack Experience"
            ],
            "description": "Role description and requirements",
            "required_skills": [
                "JavaScript",
                "React",
                "Node.js"
            ],
            "recommended_skills": [
                "AWS",
                "System Design"
            ]
        }
    ],
    "summary": "Based on your strong full-stack development background..."
}
```

Example Response:
```json
{
    "summary": "Brief CV overview highlighting key qualifications",
    "strengths": [
        "Strong technical skills in full-stack development",
        "Impressive project portfolio",
        "Multiple technical certifications",
        "Demonstrated adaptability"
    ],
    "improvements": [
        "Summary optimization suggestions",
        "Project description refinements",
        "Experience detail recommendations"
    ],
    "skills_analysis": {
        "technical": [
            "Full-stack development skills",
            "AI and machine learning expertise",
            "Data analysis capabilities"
        ],
        "soft": [
            "Adaptability",
            "Collaboration",
            "Communication"
        ]
    },
    "recommendations": [
        "Actionable CV improvements",
        "Career development suggestions",
        "Skills enhancement recommendations"
    ]
}
```

### 2️⃣ Smart Job Analysis
```python
POST /api/v1/recruitment/analyze-job
{
    "title": "Senior Backend Engineer",
    "description": "Looking for an expert in distributed systems",
    "requirements": ["Python", "Redis", "Distributed Systems"],
    "responsibilities": ["System Design", "Performance Optimization"]
}
```

### 3️⃣ Dynamic Interview Generation
```python
POST /api/v1/recruitment/generate-questions
# Generates conversation flows that adapt based on responses
{
    "conversation_flows": [
        {
            "initial_topic": "Redis Implementation",
            "base_question": "How have you used Redis?",
            "follow_up_questions": [
                {
                    "trigger": "caching",
                    "deeper_questions": [
                        "Memory limits handling?",
                        "Scaling strategies?",
                        "High availability setup?"
                    ]
                }
            ]
        }
    ]
}
```

### 4️⃣ Progressive Depth Evaluation
```python
POST /api/v1/recruitment/evaluate-response
# Evaluates technical depth and suggests deeper follow-ups
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- FastAPI
- CrewAI
- Groq API Key
- PyPDF2

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/repo

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your Groq API key to .env
```

## 💻 Usage Guide

### 1. Start the Server
```bash
uvicorn src.main:app --reload
```

### 2. API Flow

#### Step 1: Analyze CV
```bash
curl -X POST "http://localhost:8000/api/v1/analyze-cv" \
     -H "Content-Type: multipart/form-data" \
     -F "cv_file=@path/to/cv.pdf"
```

#### Step 2: Create Assessment Criteria
```bash
curl -X POST "http://localhost:8000/api/v1/recruitment/analyze-job" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Senior Backend Engineer",
           "description": "..."
         }'
```

#### Step 3: Generate Dynamic Interview
```bash
curl -X POST "http://localhost:8000/api/v1/recruitment/generate-questions" \
     -F "cv_file=@path/to/cv.pdf" \
     -F "criteria=@path/to/criteria.json"
```

#### Step 4: Evaluate and Progress
```bash
curl -X POST "http://localhost:8000/api/v1/recruitment/evaluate-response" \
     -F "question_id=conversation_flows[0].base_question" \
     -F "response=candidate answer" \
     -F "criteria=@path/to/criteria.json"
```

## 📊 Example Conversation Flow

```json
{
    "initial_topic": "Redis Implementation",
    "base_question": "Explain your Redis experience",
    "follow_up_questions": [
        {
            "trigger": "caching",
            "question": "What about memory limits?",
            "deeper_questions": [
                "How do you handle eviction?",
                "What's your scaling strategy?",
                "High availability approach?"
            ]
        }
    ]
}
```

## 🛠️ Tech Stack

- **FastAPI** - High-performance web framework
- **CrewAI** - AI agent orchestration
- **Groq** - Ultra-fast LLM inference
- **PyPDF2** - PDF processing for CV analysis
- **Pydantic** - Data validation

## 🔜 Roadmap

- [ ] Enhanced CV Analysis Features
- [ ] Real-time Voice Interview Integration
- [ ] Interview Memory System
- [ ] Multi-topic Conversation Flows
- [ ] Technical Depth Analytics
- [ ] Custom Interview Patterns

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- CrewAI Team for the amazing framework
- Groq for ultra-fast LLM inference
- FastAPI for the robust web framework
- Google's technical interview style for inspiration

---

<div align="center">

### Made with ❤️ for Smarter Technical Interviews

[Report Bug](https://github.com/yourusername/repo/issues) • [Request Feature](https://github.com/yourusername/repo/issues)

</div>