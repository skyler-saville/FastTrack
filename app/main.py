# main.py
from fastapi import Depends, FastAPI
from typing import Union

from .dependencies import get_query_token, get_token_header
# TODO import routers from routers/__init__.py

from .routers import userRouter, choresRouter, rewardsRouter, punishmentRouter

# global dependency "get_query_token"
# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()
app.include_router(userRouter)
# require special header token
app.include_router(choresRouter)
app.include_router(rewardsRouter)
app.include_router(punishmentRouter)
@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
