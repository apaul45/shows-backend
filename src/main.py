from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from motor.motor_asyncio import AsyncIOMotorClient

import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()
mongo_connection = os.getenv("MONGO_CONNECTION")


db = AsyncIOMotorClient(mongo_connection).torqatadb
app.add_middleware(DBSessionMiddleware, db_url=os.getenv("POSTGRES_CONNECTION"))


@app.get("/")
def root():
    return {"msg": "Welcome to my backend"}


from shows import routes as shows
from user import routes as user

app.include_router(shows.router)
app.include_router(user.router)
