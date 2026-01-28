import uuid
from sqlmodel import SQLModel, Field, Relationship,Column

class User(SQLModel, table=True):
    __tablename__ = "users"
    uid: uuid.UUID = Field(sa_column=Column(
        nullable=False, primary_key=True, default=uuid.uuid4
    ))
    username: str
    email: str
    password_hash: str
