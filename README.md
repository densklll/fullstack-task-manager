# Full-Stack Task Manager

[![CI](https://github.com/densklll/fullstack-task-manager/actions/workflows/ci.yml/badge.svg)](https://github.com/densklll/fullstack-task-manager/actions/workflows/ci.yml)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.14-009688)](https://www.django-rest-framework.org/)
[![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![Redux Toolkit](https://img.shields.io/badge/Redux%20Toolkit-1.8-764ABC?logo=redux&logoColor=white)](https://redux-toolkit.js.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/compose/)

Full-stack task management app: **Django REST** API with **JWT**, **Celery** + **Redis** for background work, **Swagger / Redoc** docs, and a **React** client with **Redux Toolkit**, **React Router**, and **Styled Components**. Packaged with **Docker Compose** and **GitHub Actions** CI.

---

## Highlights

- **Tasks** — CRUD with status filters
- **Async jobs** — Celery workers backed by Redis
- **Auth** — JWT via `djangorestframework-simplejwt`; protected routes on the frontend
- **API docs** — `/swagger/` and `/redoc/` (drf-yasg)
- **Frontend** — Axios instance with interceptors for access/refresh tokens; `ProtectedRoute` for private pages

## Stack

| Layer | Technology |
| -------- | ---------- |
| **API** | Django 4.2, Django REST Framework, Gunicorn |
| **Workers** | Celery 5, Redis |
| **Auth** | JWT (simplejwt) |
| **UI** | React 18, Redux Toolkit, Styled Components, React Router 6 |
| **Tooling** | CRACO, Create React App |
| **Ops** | Docker Compose, GitHub Actions |

## Repository layout

```
fullstack-task-manager/
├── backend/           # Django project, Celery, API
├── frontend/          # React SPA
├── docker-compose.yml
└── .github/workflows/ # CI (backend tests + frontend step)
```

## Quick start (Docker)

From the repository root:

```bash
git clone https://github.com/densklll/fullstack-task-manager.git
cd fullstack-task-manager
docker compose up --build
```

| Service | URL |
| -------- | --- |
| API | [http://localhost:8000](http://localhost:8000) |
| Frontend | [http://localhost:3000](http://localhost:3000) |
| Swagger | [http://localhost:8000/swagger/](http://localhost:8000/swagger/) |
| Redoc | [http://localhost:8000/redoc/](http://localhost:8000/redoc/) |

## Local development (without Docker)

**Backend**

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Frontend**

```bash
cd frontend
npm install
npm start
```

## Testing

```bash
# Backend
cd backend && python manage.py test

# Frontend (placeholder script in this repo)
cd frontend && npm test
```

## Contributing

Issues and pull requests are welcome.

- *2023-01-10* — Review react-router state after login (local dev)

- *2023-01-22* — Describe docker compose service links (CI runner)

- *2023-02-04* — Document redis broker string for celery (staging)

- *2023-02-14* — Review serializer deadline optional field (demo box)

- *2023-02-24* — Record CRACO alias for tests (demo box)

- *2023-03-11* — Clarify frontend env base URL (demo box)

- *2023-03-24* — Note redis broker string for celery (prod checklist)

- *2023-04-07* — Note Celery task idempotency key (prod checklist)

- *2023-04-22* — Adjust task status filter query params (CI runner)

- *2023-05-04* — Align migration checklist for celery beat (demo box)

- *2023-05-24* — Document Redux task normalization (demo box)

- *2023-06-12* — Record react-router state after login (local dev)

- *2023-06-28* — Record CRACO alias for tests (local dev)

- *2023-07-10* — Stub axios 401 refresh race (CI runner)

- *2023-07-20* — Capture gunicorn worker count on dev (demo box)
