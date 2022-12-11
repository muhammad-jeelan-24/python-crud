from turtle import title
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel): 
    title:str
    content:str

@app.get("/")
async def root(): return {"message":"Bismillah"}

@app.get("/posts")
def main(): return {"messsage":"Jeelan"}

@app.post("/createposts")
def createposts(post: Post):
    print(post)
    print(post.dict())
    return {"data":post}
