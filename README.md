# Daily Quote API 🌟

A simple yet fun API that returns a random motivational or funny quote every day.  
Built with **Python + FastAPI** 🚀  

---

## Features ✨
- Returns a random **daily quote** 📝  
- Provides the **current date** 📅  
- Lightweight, no database required 🪶  
- Built with FastAPI (fast & modern) ⚡  

---

## Installation ⚙️

1. Clone the repo:
```bash
git clone https://github.com/your-username/daily-quote-api.git
cd daily-quote-api
```

2. Install dependencies:
```bash
pip install fastapi uvicorn
```

3. Run the server:
```bash
uvicorn main:app --reload
```

---

## Usage 📌

- Open your browser or use curl/Postman:  
```
http://127.0.0.1:8000/quote
```

- Example Response:
```json
{
  "date": "2025-09-01",
  "quote": "Code, eat, sleep, repeat. 😎",
  "author": "Daily Quote API"
}
```

- API Docs (Swagger UI):
```
http://127.0.0.1:8000/docs
```

---

## Endpoints 🔗

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Welcome message |
| GET    | `/quote` | Get your daily quote |

---

## License 📜
This project is licensed under the MIT License.  
