import httpx
import pytest
from app import models

pytestmark = pytest.mark.anyio


async def _create_test_session(client: httpx.AsyncClient) -> dict:
    response = await client.post("/sessions")
    assert response.status_code == 201
    return response.json()


async def test_health(client: httpx.AsyncClient):
    response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


async def test_get_session(client: httpx.AsyncClient):
    session = await _create_test_session(client)

    response = await client.get(f"/sessions/{session['id']}")

    assert response.status_code == 200
    assert response.json() == session


async def test_get_session_returns_session_not_found(client: httpx.AsyncClient):
    session = models.Session()  # session not persisted

    response = await client.get(f"/sessions/{session.id}")

    assert response.status_code == 404


async def test_create_session(client: httpx.AsyncClient):
    response = await client.post("/sessions")

    assert response.status_code == 201
