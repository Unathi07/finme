# Database design

## Initial foundation

The starter configures PostgreSQL, SQLAlchemy 2.x, and Alembic. Feature tables are introduced by migrations with their vertical slice.

## Planned entities

- `users`: id, unique email, password hash, timestamps.
- `transactions`: id, user_id, amount `NUMERIC(14,2)`, currency, kind, category, description, occurred_at, timestamps.
- `income`: id, user_id, amount `NUMERIC(14,2)`, currency, source, received_at, timestamps.
- `budgets`: id, user_id, category, month, limit `NUMERIC(14,2)`.
- `savings_goals`: id, user_id, name, target/current `NUMERIC(14,2)`, target date.
- `debts`: id, user_id, name, principal/balance/rate stored with explicit precision, due date.

Every financial row has a foreign key to its owner and indexes supporting user-scoped queries. Use `Decimal` in Python and `NUMERIC` in PostgreSQL. Enforce non-negative/domain constraints where valid, unique user/month/category budgets, and transactional consistency. Never accept `user_id` as authority from an untrusted client. These are planned models, not all implemented yet.
