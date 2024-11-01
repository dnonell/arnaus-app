from uuid import uuid4

from pydantic import BaseModel, Field


class Session(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
