

from pydantic import BaseModel


from typing import Optional, List

class User(BaseModel):
    name: str
    email: str
    password: str

class Blog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True


class showUser(BaseModel):
    name: str
    email: str
    blogs: list[Blog] = []


    class Config:
        orm_mode = True




class showBlog(BaseModel):
    title: str
    body: str
    creator: showUser
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str
    class Config:
        orm_mode = True