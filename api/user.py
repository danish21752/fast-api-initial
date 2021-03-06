from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from api.utils.courses import get_user_courses
from api.utils.users import get_users, get_user_by_email, get_user, create_user
from db.db_setup import get_db, async_get_db
from pydantic_schemas.courses import Course
from pydantic_schemas.users import UserCreate, User

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=404, detail="User Already Registered")
    return create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=User, status_code=200)
async def read_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_user


@router.get("/users/{user_id}/course", response_model=List[Course])
async def read_user_courses(user_id: int, db: Session = Depends(get_db)):
    courses = get_user_courses(user_id=user_id, db=db)
    return courses


# @router.get("/users/{id}")
# async def get_user(
#         id: int = Path(
#           ...,
#           description="The ID of the user you want to retrieve",
#           lt=2),
#         q: str = Query(None, max_length=5)
# ):
#     return { "user": users[id], "query": "q" }
# done
