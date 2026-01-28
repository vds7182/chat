import uuid
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid.uuid4
        )
    )
    username: str = Field(sa_column=Column(String(50), nullable=False))
    email: str = Field(sa_column=Column(String(100), nullable=False, unique=True))
    password_hash: str = Field(sa_column=Column(String(128), nullable=False))

