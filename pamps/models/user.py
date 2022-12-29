from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
from pamps.security import HashedPassword

from pydantic import BaseModel

if TYPE_CHECKING:
    from pamps.models.post import Post


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=False)
    email: str = Field(unique=True, nullable=False)
    password: HashedPassword
    bio: Optional[str] = None

    posts: List["Post"] = Relationship(back_populates="user")

    # implents a request API who using a randon avatar
    avatar: Optional[str] = None


class UserResponse(BaseModel):
    """Serializer for User Response"""

    username: str
    avatar: Optional[str] = None
    bio: Optional[str] = None


class UserRequest(BaseModel):
    """Serializer for User request payload"""

    email: str
    username: str
    password: str
    avatar: Optional[str] = None
    bio: Optional[str] = None
