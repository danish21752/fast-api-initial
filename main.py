from fastapi import FastAPI

from api import user, courses, sections
from db.db_setup import engine
from db.models import users, course

users.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

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

app.include_router(user.router)
app.include_router(courses.router)
app.include_router(sections.router)

