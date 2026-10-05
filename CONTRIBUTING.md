# Contributing to CampusHub

CampusHub is intentionally beginner-friendly. Pick one focused issue, create a branch, make the smallest useful change, and open a PR.

## Local workflow
1. Fork/clone the repository.
2. Create a virtual environment and install `requirements.txt`.
3. Copy `.env.example` to `.env` and set a secret key.
4. Run `python run.py`.
5. Run `pytest -q` before opening a PR.

## Branches
Use names such as `feature/task-filters`, `fix/login-validation`, or `docs/setup-guide`.

## Avoiding merge conflicts
Routes are separated by module, frontend JavaScript is separated by page, and models are centralized. Avoid unrelated formatting changes. If two people need the same template, split reusable UI into `templates/partials/` before adding more logic. Keep PRs focused on one issue.

## Code style
Prefer clear Python and small functions. Validate at the API boundary. Keep private queries scoped to `current_user.id`. Do not commit `.env`, SQLite databases, generated files, or credentials.
