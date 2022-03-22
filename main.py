from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import users, courses, sections

app = FastAPI(
    title= "Fast API Initial Project",
    description="My first project",
    version="0.0.1",
    contact={
        "name": "Danish",
        "email": "danish21752@gmail.com"
    },
    license_info={
        "name": "MIT",
    },

)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)

