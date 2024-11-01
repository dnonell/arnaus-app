from app import exceptions, models, repository


async def health_check() -> bool:
    return repository.health_check()


async def create_session() -> models.Session:
    session = models.Session()

    repository.set_value(name=session.id, value=session.model_dump_json())

    return session


async def get_session(session_id: str) -> models.Session:
    value = repository.get_value(name=session_id)

    if not value:
        raise exceptions.SessionNotFound

    return models.Session.model_validate_json(value)
