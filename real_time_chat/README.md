# AGENTS.md - Real-Time Chat Django Project

## Project Overview

Django 6.0.3 real-time chat application using Django Channels and Daphne (ASGI).
Python 3.13, managed with `uv`. SQLite database.

## Project Structure

```
real_time_chat/
├── main.py                  # Entry point placeholder
├── pyproject.toml           # Project config (uv)
├── uv.lock                  # Dependency lock file
└── chat_project/            # Django project root
    ├── manage.py
    ├── chat_project/        # Django settings module
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    └── chat_app/            # Main application
        ├── models.py
        ├── views.py
        ├── urls.py
        ├── consumers.py     # WebSocket consumers
        ├── routing.py       # WebSocket URL routing
        ├── templates/
        └── tests.py
```

## Build / Run Commands

All Django commands must be run from the `chat_project/` directory.

```bash
# Install dependencies
uv sync

# Run development server (Daphne ASGI)
uv run python chat_project/manage.py runserver

# Database migrations
uv run python chat_project/manage.py makemigrations
uv run python chat_project/manage.py migrate

# Django shell
uv run python chat_project/manage.py shell

# Create superuser
uv run python chat_project/manage.py createsuperuser
```

## Testing

The project uses Django's built-in test framework (`django.test.TestCase`).

```bash
# Run all tests
uv run python chat_project/manage.py test

# Run tests for a specific app
uv run python chat_project/manage.py test chat_app

# Run a single test class
uv run python chat_project/manage.py test chat_app.tests.TestClassName

# Run a single test method
uv run python chat_project/manage.py test chat_app.tests.TestClassName.test_method_name
```

Tests live in `chat_project/chat_app/tests.py`.

## Code Style Guidelines

### General

- Python 3.13+ syntax is expected.
- No linter or formatter configuration exists yet — follow Django conventions.
- Follow PEP 8 with the existing codebase style as the authoritative reference.

### Imports

- Use `from pathlib import Path` style (named imports from standard library).
- Django/third-party imports come after stdlib, separated by a blank line.
- Use relative imports within the app: `from .models import ChatRoom`, `from . import views`.
- Group imports: stdlib → third-party → local, with blank lines between groups.

### Formatting

- Double quotes for strings (`"string"`), matching Django's default style.
- 4-space indentation (standard Python).
- Two blank lines between top-level definitions (classes, functions).
- One blank line between methods inside a class.
- Trailing commas in multi-line data structures are acceptable.

### Naming Conventions

- **Classes**: `CamelCase` (e.g., `ChatConsumer`, `ChatRoom`, `ChatAppConfig`).
- **Functions/methods**: `snake_case` (e.g., `chat_room`, `chat_message`).
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `BASE_DIR`, `ASGI_APPLICATION`).
- **URL names**: `snake_case` strings (e.g., `"index"`, `"chat_room"`).
- **Template paths**: `app_name/template.html` (e.g., `"chat_app/index.html"`).
- **Django apps**: `snake_case` directory names (e.g., `chat_app`).

### Types

- No type hints are currently used in this codebase.
- If adding type hints, follow standard Python typing conventions and keep them consistent with existing code.

### Django-Specific Patterns

- Models: define in `models.py`, register in `admin.py`.
- Views: function-based views are used; keep them thin — delegate business logic elsewhere if complex.
- URLs: define `urlpatterns` list in each app's `urls.py`, include in project `urls.py`.
- WebSocket consumers: extend `AsyncWebsocketConsumer` from `channels.generic.websocket`.
- WebSocket routing: define `websocket_urlpatterns` in `routing.py`, wire up in `asgi.py`.
- Channel layers: currently using `InMemoryChannelLayer` (dev only — swap for Redis in production).

### Error Handling

- Use Django's built-in error handling for HTTP views (404 via `get_object_or_404`, etc.).
- In WebSocket consumers, handle `json.JSONDecodeError` when parsing incoming messages.
- Avoid bare `except:` clauses; catch specific exceptions.

### Templates

- Located in `chat_app/templates/chat_app/` following Django's app-level template convention.
- Use Django template language (`{% %}`, `{{ }}`).

### Migration Files

- Never edit migration files manually after they are applied.
- Use `makemigrations` to generate and `migrate` to apply.

## Key Dependencies

- `django>=6.0.3` — web framework
- `channels>=4.3.2` — WebSocket support
- `daphne>=4.2.1` — ASGI server
