import pytest
from app import main
from httpx import ASGITransport, AsyncClient


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=main.app), base_url="http://test", follow_redirects=True
    ) as client:
        yield client
