# Contributing

## Daily flow

1. Pull the latest `main`.
2. Create a focused branch: `feature/transactions`, `fix/transaction-validation`, or `docs/api-contract`.
3. Work one vertical slice and commit with a conventional prefix (`feat:`, `fix:`, `test:`, `docs:`, `chore:`).
4. Open a PR that references its issue (`Closes #N`), explain testing and migrations, and add UI screenshots when relevant.
5. Ask the other developer to review. Address feedback, wait for CI, then merge to `main`.

## Standards

- Python: type hints, Pydantic request validation, SQLAlchemy 2.x, Ruff, Pytest.
- TypeScript: strict mode, small accessible components, Vitest and React Testing Library.
- Money: `Decimal` in Python and `NUMERIC` in PostgreSQL; never use floats for authoritative amounts.
- Keep routes thin; put business rules in services and persistence in repositories.
- Never commit `.env`, credentials, real financial data, or API keys. Use fictional data.
- AI may explain validated tool results; it must not invent computed totals or execute arbitrary SQL.

## Definition of Done

Acceptance criteria pass; relevant tests and checks pass; API/UI are integrated; errors and access boundaries are considered; docs and migrations are updated; PR receives peer review and CI passes.
