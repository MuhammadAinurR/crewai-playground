<div align="center">

# 🤖 AI-Powered Technical Interview Assistant

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.crewai.com/)
[![Groq](https://img.shields.io/badge/Groq-4BAAEE?style=for-the-badge)](https://groq.com/)

> 🎯 Transform your technical interviews into dynamic, intelligent conversations powered by AI

[Live Demo](#) • [Quick Start](#-quick-start) • [Documentation](#-documentation)

</div>

---

## ✨ What Makes This Special?

- 🧠 **Dynamic Question Flow**: Questions adapt based on candidate responses
- 🎯 **Real-time Evaluation**: Instant feedback on technical accuracy and depth
- 🔄 **Intelligent Follow-ups**: Automatically triggers relevant follow-up questions
- 📊 **Comprehensive Assessment**: Evaluates technical skills, understanding depth, and practical experience

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/repo.git

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Add your Groq API key to .env

# Start the server
uvicorn src.main:app --reload
```

## 💡 How It Works

### 1. Create Assessment Criteria
```bash
curl -X POST "http://localhost:8000/api/v1/recruitment/analyze-job" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Senior Backend Engineer",
           "requirements": ["Python", "FastAPI", "Concurrency"],
           "responsibilities": ["Design scalable systems"]
         }'
```

### 2. Generate Dynamic Questions
```bash
curl -X POST "http://localhost:8000/api/v1/recruitment/generate-questions" \
     -F "cv_file=@candidate_cv.pdf" \
     -F "criteria=@criteria.json"
```

### 3. Evaluate & Get Follow-ups
```bash
curl -X POST "http://localhost:8000/api/v1/recruitment/evaluate-response" \
     -F "question_id=Python Development" \
     -F "response=candidate answer" \
     -F "criteria=@criteria.json" \
     -F "conversation_flows=@flows.json"
```

## 🎯 Complete Interview Flow Guide

### 1. Base Question
**Request:**
```bash
POST /api/v1/recruitment/evaluate-response
Form-data:
- question_id: Python Development
- response: "In my previous role, I optimized a Python application that was processing large amounts of data. I implemented multiprocessing using Python's concurrent.futures module to parallelize the data processing tasks. For database operations, I implemented connection pooling using SQLAlchemy and added appropriate indexes. We also used Redis for caching frequently accessed data. This resulted in a 70% reduction in processing time."
- criteria: {your_criteria_json}
- conversation_flows: {your_flows_json}
- current_question_level: base
```

**Response:**
```json
{
    "technical_accuracy": {
        "score": 90,
        "comments": "Strong understanding of Python development concepts, including multiprocessing, connection pooling, and caching..."
    },
    "next_question": {
        "type": "follow_up",
        "question": "How do you handle concurrency in your applications?",
        "deeper_questions": [
            "What concurrency models do you use?",
            "How do you handle synchronization and locking?",
            "What libraries do you use for concurrent programming?"
        ]
    }
}
```

### 2. Follow-up Question
**Request:**
```bash
POST /api/v1/recruitment/evaluate-response
Form-data:
- question_id: Python Development
- response: "In my Python applications, I handle concurrency using multiple approaches. For I/O-bound tasks, I use asyncio with async/await patterns. For CPU-bound tasks, I use the multiprocessing module. I also implement thread pooling using concurrent.futures.ThreadPoolExecutor. For synchronization, I use threading.Lock() to prevent race conditions."
- criteria: {same_criteria_json}
- conversation_flows: {same_flows_json}
- current_question_level: follow_up
```

**Response:**
```json
{
    "technical_accuracy": {
        "score": 85,
        "comments": "Demonstrates strong understanding of concurrency concepts..."
    },
    "next_question": {
        "type": "deeper",
        "question": "What concurrency models do you use?",
        "deeper_questions": [
            "How do you handle synchronization and locking?",
            "What libraries do you use for concurrent programming?"
        ]
    }
}
```

### 3. Deeper Question
**Request:**
```bash
POST /api/v1/recruitment/evaluate-response
Form-data:
- question_id: Python Development
- response: "I use three main concurrency models: 1) Thread-based concurrency using threading and concurrent.futures for I/O-bound tasks, 2) Process-based parallelism using multiprocessing for CPU-intensive tasks to bypass GIL limitations, 3) Asynchronous programming with asyncio for event-driven applications. Each has its trade-offs: threads are good for I/O but limited by GIL, processes have more overhead but better for CPU work, and asyncio is efficient but requires async-compatible libraries."
- criteria: {same_criteria_json}
- conversation_flows: {same_flows_json}
- current_question_level: deeper
```

**Response:**
```json
{
    "technical_accuracy": {
        "score": 90,
        "comments": "Excellent understanding of different concurrency models and their trade-offs..."
    },
    "next_question": {
        "type": "continue",
        "question": "Continue with current question",
        "deeper_questions": []
    }
}
```

### 🔄 Flow Progression
1. System starts with base questions about Python development
2. Based on mentions of concurrency, triggers follow-up questions
3. High scores (>85) trigger deeper technical questions
4. Process continues until topic is exhausted or exit conditions are met
5. Moves to next topic (e.g., FastAPI, Concurrency) when current topic is complete

### 📝 Key Points
- Keep same `criteria` and `conversation_flows` throughout the session
- Watch `current_question_level` progression: base → follow_up → deeper
- Pay attention to trigger words in responses
- Check `next_question` field for subsequent questions
- Monitor scores to gauge candidate performance

## 🎯 Example Flow

1. **Base Question**:
   > "Can you explain your experience with Python development?"

2. **Follow-up** (based on response):
   > "How do you handle concurrency in your applications?"

3. **Deeper Questions** (based on expertise):
   > "What concurrency models do you use?"
   > "How do you handle synchronization?"

## 📊 Sample Evaluation

```json
{
    "technical_accuracy": {
        "score": 90,
        "comments": "Strong understanding of concurrency models..."
    },
    "understanding_depth": {
        "score": 85,
        "comments": "Good grasp of practical applications..."
    },
    "next_question": {
        "type": "deeper",
        "question": "What concurrency models do you use?"
    }
}
```

## 🛠️ Tech Stack

- **FastAPI**: High-performance web framework
- **CrewAI**: AI agent orchestration
- **Groq**: Ultra-fast LLM inference
- **PyPDF2**: CV analysis
- **Pydantic**: Data validation

## 📚 Documentation

Full documentation available at [docs/README.md](docs/README.md)

## 📝 Contributing

Contributions welcome! Check out our [Contributing Guide](CONTRIBUTING.md)

## 📝 License

MIT License - see [LICENSE](LICENSE)

---

<div align="center">

### Made with ❤️ for Better Technical Interviews

[Report Bug](https://github.com/yourusername/repo/issues) • [Request Feature](https://github.com/yourusername/repo/issues)

</div>