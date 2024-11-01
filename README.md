# Face Encoding 

Arnau's docker compose example app

## Requirements

- GNU Make
- Docker
- Python 3

## Service endpoints

The exercise exposes the follwing endpoints:

- GET   /health: checks the service healthiness
- POST  /sessions: creates a new session to start uploading images
- GET   /sessions/{session_id}: gets the session summary for the given session_id
- GET   /docs: provides OpenAPI documentation for the previous endpoints

## Running the service

The application can be executed in development and production modes.

```
make run-prod
make run-dev
```

## Testing

Tests are divided in unit and integration. Both can be executed independently or all at once using the `make tests` rule.

```
make tests-unit
make tests-integration
make tests
```

## Local environment

Running the service locally is also possible for debugging.

```
make venv
make run-local
make clean
```

### Linting

Tools such as `black`, `isort`, `flake8` and `mypy` are used to ensure the code is properly formatted and performs a minimim level of readability and quality.

```
make format
make lint
```
