# Repository Guidelines

## Project Structure & Module Organization

This repository is currently empty. As implementation is added, keep production code under `src/`, tests under `tests/`, and non-code resources under `assets/`. Group files by feature or domain rather than by file type when the project grows. Keep generated output in `build/`, `dist/`, or another ignored directory; do not commit generated artifacts.

Example layout:

```text
src/<feature>/
tests/<feature>/
assets/
```

Document any intentional departure from this layout in the root `README.md`.

## Build, Test, and Development Commands

No build tool, package manager, or test runner is configured yet. When adding one, expose a small, predictable command set and document it in `README.md`. Prefer conventional entry points such as:

- `make setup` — install or prepare development dependencies.
- `make test` — run the complete automated test suite.
- `make lint` — check formatting and static-analysis rules.
- `make run` — start the project locally.

Commands should be reproducible from the repository root and return a nonzero status on failure.

## Coding Style & Naming Conventions

Use the standard formatter and linter for the chosen language, checked into project configuration where possible. Do not mix formatting-only changes with functional changes. Use descriptive names: `snake_case` for files in Python projects, `kebab-case` for web assets, and the language's established conventions for symbols and types. Prefer small modules with explicit responsibilities and comments that explain intent, not obvious mechanics.

## Testing Guidelines

Add tests with every behavior change and bug fix. Mirror source organization beneath `tests/`; name tests after the behavior they verify (for example, `test_rejects_expired_token`). Keep tests deterministic and avoid relying on network access, wall-clock timing, or developer-specific state. Once a framework is selected, record coverage expectations and the exact test command here.

## Commit & Pull Request Guidelines

There is no Git history from which to infer an existing convention. Use concise, imperative commit subjects, optionally following Conventional Commits (for example, `feat: add session validation` or `fix: handle empty input`). Keep each commit focused.

Pull requests should explain the motivation and implementation, list verification performed, and link relevant issues. Include screenshots or recordings for visible UI changes and call out configuration changes, migrations, or follow-up work.

## Security & Configuration

Never commit credentials, tokens, or local environment files. Provide sanitized examples such as `.env.example`, and document every required variable without including real secret values.
