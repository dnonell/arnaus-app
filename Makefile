COMPONENT ?= arnaus-app
COMPOSE_FILE ?= compose.yaml
DC=docker compose -p ${COMPONENT} -f ${COMPOSE_FILE}

.PHONY: run-dev
run-dev:
	${DC} up app-dev

.PHONY: run-prod
run-prod:
	${DC} up app

.PHONY: run-local
run-local:
	${DC} up -d cache face-encoding
	venv/bin/fastapi dev app/main.py --port 8080 --reload
	${DC} down --remove-orphans

.PHONY: venv
venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
	venv/bin/pip install -r dev-requirements.txt

.PHONY: clean
clean: down
	find . -name '__pycache__' | xargs rm -rf
	find . -type f -name "*.pyc" -delete
	rm -rf venv

.PHONY: down
down:
	${DC} down --remove-orphans

.PHONY: build
build:
	${DC} build --no-cache app
	${DC} build --no-cache app-dev

.PHONY: lint-local
lint:
	venv/bin/black --check app/ tests/
	venv/bin/isort --check-only app/ tests/
	venv/bin/flake8 app/ tests/
	venv/bin/mypy app/ tests/

.PHONY: format
format:
	venv/bin/black app/ tests/
	venv/bin/isort app/ tests/

.PHONY: tests-unit-local
tests-unit:
	venv/bin/pytest --cache-clear tests/unit

.PHONY: tests-integration-local
tests-integration:
	${DC} up -d cache face-encoding
	venv/bin/pytest --cache-clear tests/integration
	${DC} down --remove-orphans

.PHONY: tests
tests: tests-unit tests-integration
