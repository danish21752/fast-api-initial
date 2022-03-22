from typing import Optional, List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()


users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"

@router.get("/users/{id}")
async def get_user(id: int):
    return { "user": users[id] }


# @router.get("/users/{id}")
# async def get_user(
#         id: int = Path(..., description="The ID of the user you want to retrieve", lt=2),
#         q: str = Query(None, max_length=5)
# ):
#     return { "user": users[id], "query": "q" }
