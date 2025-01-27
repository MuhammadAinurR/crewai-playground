<div align="center">

# 🤖 AI-Powered Technical Recruitment System

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.crewai.com/)
[![Groq](https://img.shields.io/badge/Groq-4BAAEE?style=for-the-badge)](https://groq.com/)

**Transform Your Technical Recruitment Process with AI-Powered Assessments**

[Features](#features) •
[Installation](#installation) •
[Usage](#usage) •
[Documentation](#documentation) •
[Contributing](#contributing)

</div>

---

## 🌟 Overview

An intelligent system that revolutionizes technical recruitment by:
- 🎯 Analyzing job descriptions to create structured assessment criteria
- 🤔 Generating in-depth technical questions
- 📊 Providing objective candidate evaluations
- 🚀 Streamlining the entire recruitment process

## ✨ Features

### 1️⃣ Smart Job Analysis
```python
POST /api/v1/recruitment/analyze-job
{
    "title": "Senior Backend Engineer",
    "requirements": ["Python", "FastAPI", "Redis"],
    "responsibilities": ["API Design", "Team Leadership"]
}
```

### 2️⃣ Intelligent Question Generation
```python
POST /api/v1/recruitment/generate-questions
# Generates role-specific technical questions based on CV and criteria
```

### 3️⃣ Automated Response Evaluation
```python
POST /api/v1/recruitment/evaluate-response
# Provides detailed scoring and feedback on candidate responses
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- FastAPI
- CrewAI
- Groq API Key

### Installation

```bash
# Clone the repository
git clone https://github.com/MuhammadAinurR/crewai-playground

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

### 2. API Endpoints

#### Analyze Job Description
```bash
curl -X POST "http://localhost:8000/api/v1/recruitment/analyze-job" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Senior Backend Engineer",
           "description": "..."
         }'
```

#### Generate Questions
```bash
curl -X POST "http://localhost:8000/api/v1/recruitment/generate-questions" \
     -F "cv_file=@path/to/cv.pdf" \
     -F "criteria=@path/to/criteria.json"
```

#### Evaluate Responses
```bash
curl -X POST "http://localhost:8000/api/v1/recruitment/evaluate-response" \
     -F "question_id=technical_questions[0]" \
     -F "response=candidate answer" \
     -F "criteria=@path/to/criteria.json"
```

## 📊 Example Response

```json
{
    "technical_accuracy": {
        "score": 85,
        "comments": "Strong understanding of concepts..."
    },
    "understanding_depth": {
        "score": 80,
        "comments": "Good fundamental knowledge..."
    },
    "practical_experience": {
        "score": 90,
        "comments": "Excellent hands-on experience..."
    }
}
```

## 🛠️ Tech Stack

- **FastAPI** - High-performance web framework
- **CrewAI** - AI agent orchestration
- **Groq** - Ultra-fast LLM inference
- **PyPDF2** - PDF processing
- **Pydantic** - Data validation

## 🔜 Roadmap

- [ ] Voice Interview Integration
- [ ] Enhanced Analytics Dashboard
- [ ] Custom Assessment Workflows
- [ ] Multi-language Support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- CrewAI Team for the amazing framework
- Groq for ultra-fast LLM inference
- FastAPI for the robust web framework

---

<div align="center">

### Made with ❤️ for Better Technical Recruitment

[Report Bug](https://github.com/yourusername/repo/issues) • [Request Feature](https://github.com/yourusername/repo/issues)

</div>