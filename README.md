# Finme AI

An AI-assisted personal finance platform for South African users. Finme AI uses deterministic Python calculations for money and keeps AI behind authorised, validated backend tools. ZAR is the default currency.

## MVP principles

- No bank connections, payments, or transfers in the MVP.
- Use `Decimal` and database `NUMERIC` for authoritative financial amounts.
- Financial endpoints must require authentication and enforce user ownership before deployment.
- Use fictional development data only; never commit secrets.

## Stack

React, TypeScript, Vite, Tailwind CSS, React Router; Python, FastAPI, Pydantic, SQLAlchemy, Alembic; PostgreSQL; Pytest and Vitest; Docker Compose and GitHub Actions.

## Quick start (Windows / PyCharm)

Requirements: Python 3.12, Node.js 22 LTS with npm, Git, and optionally Docker Desktop with Compose. Copy `.env.example` to `.env`. Start PostgreSQL with `docker compose up -d db` (or use a local PostgreSQL instance), then follow [docs/development-guide.md](docs/development-guide.md). Backend: `cd backend; py -3.12 -m venv .venv; .venv\Scripts\Activate.ps1; python -m pip install -e .[dev]; alembic upgrade head; uvicorn app.main:app --reload`. Frontend in a second terminal: `cd frontend; npm ci; npm run dev`.

## Test and quality checks

Backend: `cd backend; pytest; ruff check .; ruff format --check .`. Frontend: `cd frontend; npm ci; npm run typecheck; npm test -- --run; npm run build`.

## Architecture

See [architecture](docs/architecture.md), [database design](docs/database-design.md), and [API contract](docs/api-contract.md). The starter exposes `GET /health` and a responsive UI shell with Dashboard, Transactions, Income, and AI Assistant routes. Financial feature endpoints will be added as vertical slices.

## Team workflow

Use short-lived branches from `main`, link each PR to an issue, run checks, and get a peer review before merging. See [CONTRIBUTING.md](CONTRIBUTING.md). Both developers rotate through backend, frontend, tests, and AI work. Planned ownership is recorded in issues; only Unathi07 is assigned until Developer B shares their username.

## Roadmap

Eight two-week planning sprints are outlined in [docs/roadmap.md](docs/roadmap.md). Dates are intentionally not fixed until capacity and dependencies are agreed.

