from typing import Dict

from app import exceptions, models, service
from fastapi import FastAPI, HTTPException, status

app = FastAPI(
    title="Arnau's App",
    version="0.0.1",
)


@app.get(
    "/health",
    response_model=Dict,
    responses={
        200: {
            "description": "Application healthiness",
            "content": {"application/json": {"example": {"status": "healthy"}}},
        }
    },
)
async def health_check():
    _ = await service.health_check()
    return {"status": "healthy"}


@app.get(
    "/sessions/{id}",
    summary="Get Session metadada by id",
    response_model=models.Session,
    responses={
        200: {
            "description": "Session requested by ID",
            "content": {"application/json": {"example": {"id": "afcbddd2a8f74aefa2edf1cbc9f662cc", "selfies": []}}},
        },
        404: {
            "description": "Session not found",
            "content": {"application/json": {"example": {"detail": "Session not found"}}},
        },
    },
)
async def get_session(id: str) -> models.Session:
    try:
        return await service.get_session(session_id=id)
    except exceptions.SessionNotFound as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))


@app.post(
    "/sessions/",
    status_code=status.HTTP_201_CREATED,
    summary="Create new session",
    response_model=models.Session,
    responses={
        201: {
            "description": "Session created",
            "content": {"application/json": {"example": {"id": "afcbddd2a8f74aefa2edf1cbc9f662cc", "selfies": []}}},
        },
    },
)
async def create_session() -> models.Session:
    return await service.create_session()
