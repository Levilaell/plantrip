# ✈️ PlanTrip - Intelligent Travel Planning SaaS

**PlanTrip** is a SaaS platform that generates personalized and realistic travel itineraries based on destination, dates, budget, and user preferences. Using LangChain, integration with multiple APIs (Google Places, Skyscanner, Eventbrite, etc.), and a scalable microservices architecture, it delivers complete and dynamic travel plans ready for use.

---

## 📌 Features

- Daily itineraries with attractions, restaurants, and events
- Transport and accommodation suggestions with booking links
- Weather forecast and local events integration
- Responsive web interface (React PWA)
- Export options: PDF, ICS, Markdown, JSON
- Visual editor with drag & drop functionality
- Activity feedback and rating system

---

## 🧱 Architecture Overview

```
project_root/
├── api-gateway/            # Routing & JWT Auth (Nginx)
├── frontend/               # React PWA Application
├── backend-core/           # Django + DRF + Celery
├── microservices/          # Flights, Hotels, Events, Weather, etc.
├── langchain-pipeline/     # LangChain Orchestration
├── cache/                  # Redis for volatile data
└── docs/                   # Documentation
```

> Modern architecture using microservices, React PWA, Django REST backend, and LangChain async pipelines.

---

## ⚙️ Tech Stack

- **Frontend:** React, Bootstrap, Chart.js, react-query, react-beautiful-dnd
- **Backend:** Django REST Framework, Celery, Redis
- **Microservices:** Flask / FastAPI
- **AI Pipeline:** LangChain + OpenAI GPT-4, Pinecone/Weaviate
- **APIs Integrated:** Google Places, Eventbrite, Skyscanner, Booking, OpenWeather
- **DevOps:** Docker, Kubernetes, Nginx API Gateway

---

## 🚀 Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-user/plantrip.git
cd plantrip
```

### 2. Backend (Django)

```bash
cd backend-core
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

### 3. Frontend (React)

```bash
cd ../frontend
npm install
npm start
```

### 4. Redis & Microservices

```bash
# Dev mode with Docker
docker-compose up -d
```

---

## 🧪 Testing

- Backend: `pytest`
- Frontend: `Jest`, `React Testing Library`
- E2E: `Cypress`

---

## 📄 Itinerary Example

> A real output structure delivered to the end user:

- Executive summary of the trip
- Day-by-day cards with time slots (breakfast, morning, etc.)
- Tips, weather, ticket links, maps
- Accommodation and transport details
- Exportable formats: PDF, ICS, .md and JSON

🔗 [View sample in docs](docs/sample_itinerary.md)

---

## 🔐 .env Variables (example)

```env
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...
AMADEUS_API_KEY=...
BOOKING_API_KEY=...
DATABASE_URL=postgres://...
REDIS_URL=redis://localhost:6379
JWT_SECRET=your-secret
```

---

## 📤 Export Capabilities

- `/export-pdf/` → Styled PDF
- `/export-ics/` → Calendar file
- `/export-md/` → Structured Markdown
- `/export-json/` → API/automation ready JSON

---

## 📈 Observability & Security

- Sentry for error logging
- Prometheus + Grafana for metrics
- Health checks in all services
- Input validation, HTTPS, and restricted CORS

---

## 👥 Contributing

Feel free to open issues or submit pull requests. The project is actively evolving! 🚧

---

## 🧠 Roadmap

- [x] MVP with itinerary generation
- [x] Scalable Docker microservices
- [x] Multi-format exports
- [ ] Multilingual support
- [ ] Multiple itinerary sessions
- [ ] Admin panel with analytics

---

## 📝 License

MIT License

---

## ✉️ Contact

Levi Lael • [linkedin.com/in/levilael](https://www.linkedin.com/in/levi-lael-939b4a1b9/)