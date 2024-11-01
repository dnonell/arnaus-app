import json
from unittest import mock

import pytest
from app import exceptions, service

pytestmark = pytest.mark.asyncio


@mock.patch("app.repository.health_check")
async def test_health_check(health_check_mock):
    health_check_mock.return_value = True

    healt_check = await service.health_check()

    health_check_mock.assert_called_once()
    assert healt_check is True


@mock.patch("app.repository.set_value")
async def test_create_session(respository_set_mock):
    respository_set_mock.return_value = True

    session = await service.create_session()

    respository_set_mock.assert_called_once()
    assert session


@mock.patch("app.repository.get_value")
async def test_get_session(respository_get_mock):
    session_id = "test-id"
    respository_get_mock.return_value = json.dumps({"id": session_id})

    session = await service.get_session(session_id=session_id)

    assert session
    respository_get_mock.assert_called_once()


@mock.patch("app.repository.get_value")
async def test_get_session_returns_session_not_found(respository_get_mock):
    session_id = "test-id"
    respository_get_mock.return_value = None

    with pytest.raises(exceptions.SessionNotFound):
        _ = await service.get_session(session_id=session_id)

    respository_get_mock.assert_called_once()
