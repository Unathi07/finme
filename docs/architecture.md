# Architecture

## Responsibilities and flow

React/TypeScript owns presentation, routing, and client-side interaction. FastAPI owns validation, authentication, authorisation, business rules, and API contracts. Services perform deterministic calculations; repositories encapsulate SQLAlchemy access. PostgreSQL is the source of truth. Alembic versions schema changes.

Browser → versioned `/api/v1` route → Pydantic validation → service → repository/SQLAlchemy → PostgreSQL. Responses return through the same route. Never trust client-supplied user ownership.

## AI boundary

The future assistant will call a small allowlist of backend tools scoped to the authenticated user. Tools retrieve only authorised records and return typed results. Deterministic Python services compute balances, budgets, forecasts, and comparisons. The model can summarise those results, but cannot issue arbitrary SQL or authoritatively calculate money. Validate tool arguments and outputs; require user approval for consequential actions. LangGraph is deferred until workflows require durable multi-step state.

## Security

No financial route is production-ready until authentication, per-user ownership checks, input validation, safe error handling, and security tests are in place. Secrets come from environment configuration. Treat descriptions and uploads as untrusted. No bank access, payments, or transfers in MVP.
