from unittest import mock

import pytest
from app import repository
from redis import Redis


@pytest.fixture(scope="session")
def redis():
    with mock.patch("app.repository.Redis") as redis_mock:
        mock_connection = mock.MagicMock(spec=Redis)
        redis_mock.from_url = mock.MagicMock(return_value=mock_connection)
        yield redis_mock


def test_health_check(redis):
    repository.health_check()
    connection = redis.from_url.return_value
    connection.ping.assert_called_once()


def test_get_value(redis):
    _ = repository.get_value(name="some-name")
    connection = redis.from_url.return_value
    connection.get.assert_called_once()


def test_set_value(redis):
    _ = repository.set_value(name="some-name", value="some-value")
    connection = redis.from_url.return_value
    connection.set.assert_called_once()
