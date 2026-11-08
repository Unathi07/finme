# API contract

Base path: `/api/v1`; JSON; ISO-8601 timestamps; amounts serialized as decimal strings to avoid binary floating-point loss; currency defaults to `ZAR`.

## Implemented

- `GET /health` → `200 {"status":"ok"}` (liveness only; no private data).

## Planned initial endpoints

- `POST /auth/register`, `POST /auth/login`, `GET /users/me` (Sprint 2).
- `GET/POST /transactions`, `GET/PATCH/DELETE /transactions/{id}` (Sprint 1, protected before release).
- `GET/POST /income`, `GET/PATCH/DELETE /income/{id}` (Sprint 1, protected before release).

Example planned transaction request: `{"amount":"125.50","currency":"ZAR","kind":"expense","category":"groceries","description":"Market","occurred_at":"2026-11-08T10:00:00+02:00"}`.

Errors use FastAPI validation format initially; the team should standardise an envelope `{ "error": { "code": "...", "message": "...", "details": [] } }` before broad client integration. Never leak stack traces or data owned by another user. Version incompatible API changes under a new version path.
