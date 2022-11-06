#!/usr/bin/env python3

import uvicorn
from typing import Union
from fastapi import FastAPI

from dab import mydb

# Init fastapi
app = FastAPI()
# Init db
mdb = mydb()
mdb.createDB()

# http://127.0.0.1:8000/docs

@app.get("/")
def read_root():
    return {"Hello": "World"}

# http://127.0.0.1:8000/travel/beforestarts/2020-05-14T06:04:00
@app.get("/travel/beforestarts/{before_starts}")
async def read_item(before_starts: str):
    return mdb.queryBeforeStart(before_starts)

# http://127.0.0.1:8000/travel/withstops/AAA%20LLL
@app.get("/travel/withstops/{with_stops}")
async def read_item(with_stops: str):
    return mdb.queryWithStops(with_stops)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)