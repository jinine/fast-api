import enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserType(str, enum.Enum):
    seeker = 'seeker',
    employer = 'employer'


class Industry(str, enum.Enum):
    tech = 'tech',
    HR = 'HR',
    finance = 'finance',


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    password: str
    userType: UserType
    industry: Industry


users = []


@app.get("/")
async def root():
    return {"message": "Fast-Api Test Routing"}


@app.post('/user/')
async def create_user(_user: User):
    users.append(_user)
    return _user


@app.get('/user/')
async def user():
    return {"users": users}
