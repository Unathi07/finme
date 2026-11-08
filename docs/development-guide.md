# Development guide (Windows / PyCharm)

## Requirements

Python 3.12, Node.js 22 LTS and npm, Git. Docker Desktop with Compose is optional.

## Clone and configure

In PyCharm choose **Get from VCS**, paste `https://github.com/Unathi07/finme.git`, and choose a folder. Open the project root. Copy `.env.example` to `.env` (do not commit it).

## Database

With Docker: from the project root run `docker compose up -d db`. Without Docker, install PostgreSQL 17 and create a local `finme` database/user; set `DATABASE_URL` in `.env`.

## Backend

PyCharm: Settings → Project → Python Interpreter → add a local virtual environment using Python 3.12 under `backend/.venv`. In a terminal: `cd backend`; `py -3.12 -m venv .venv`; `.venv\Scripts\Activate.ps1`; `python -m pip install -e .[dev]`; `alembic upgrade head`; `uvicorn app.main:app --reload`. Visit `http://localhost:8000/health` and `/docs`.

## Frontend

Second terminal: `cd frontend`; `npm ci`; `npm run dev`; open `http://localhost:5173`. Configure `VITE_API_BASE_URL` in root `.env` as needed.

## Checks

Backend: `pytest`, `ruff check .`, `ruff format --check .`. Frontend: `npm run typecheck`, `npm test -- --run`, `npm run build`.

## Troubleshooting

- PowerShell blocks activation: use `backend/.venv/Scripts/python.exe -m pip ...` directly, or enable activation for the current terminal according to your organisation's policy.
- Port 5432 in use: stop the other local PostgreSQL service or change the published port and `DATABASE_URL`.
- API unreachable: confirm backend runs on 8000 and frontend uses the correct `VITE_API_BASE_URL`.
- Migration errors: confirm database is healthy and URL uses `postgresql+psycopg`.
