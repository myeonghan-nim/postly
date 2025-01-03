from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class Post(BaseModel):
    title: str
    content: str
    created_at: datetime


class PostCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=128, title="Title", description="The title of the post")
    content: str = Field(..., min_length=1, max_length=2048, title="Content", description="The content of the post")
    created_at: datetime = Field(default_factory=datetime.now, title="Created At", description="The date and time the post was created")

    @field_validator("title")
    def check_title(cls, title):
        if title.lower() == "bad":
            raise ValueError("title cannot be 'bad'")
        return title


class PostResponse(BaseModel):
    id: int
