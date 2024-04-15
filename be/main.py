from fastapi import FastAPI
from datetime import datetime
from os import environ

app = FastAPI()


@app.get("/test")
async def root():
    return {"time": str(datetime.now()), "env": environ}
