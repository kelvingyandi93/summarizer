from typing import Union
from sum import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI() # bikin server

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Link(BaseModel): #var untuk dilempar
    name: str
    size: float

@app.post("/links") # membuat end point dengan method post dan url path/items
async def create_item(link: Link): # format pastAPI (payload/req body)
    result = predict(link.name, link.size)
    return {"result" : result} # return jadi response


