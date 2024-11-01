from unittest import mock

import pytest
from app import exceptions, main, models
from fastapi.testclient import TestClient

client = TestClient(main.app)

pytestmark = pytest.mark.asyncio


@mock.patch("app.service.health_check")
async def test_health(health_check_mock):
    health_check_mock.return_value = True

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@mock.patch("app.service.get_session")
async def test_get_session(get_session_mock):
    session = models.Session()
    get_session_mock.return_value = session

    response = client.get(f"/sessions/{session.id}")
    assert response.status_code == 200
    assert response.json() == session.model_dump()


@mock.patch("app.service.get_session")
async def test_get_session_returns_session_not_found(get_session_mock):
    session = models.Session()
    get_session_mock.side_effect = [exceptions.SessionNotFound]

    response = client.get(f"/sessions/{session.id}")
    assert response.status_code == 404


@mock.patch("app.service.create_session")
async def test_create_session(create_session_mock):
    create_session_mock.return_value = models.Session(id="session-id")

    response = client.post("/sessions")
    assert response.status_code == 201
