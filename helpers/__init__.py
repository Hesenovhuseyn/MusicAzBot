__version__ = "0.7.0"

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from MusicAzBot.config import Config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


def start() -> scoped_session:
    engine = create_engine(MONGODB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()



MONGODB_CLI = MongoClient(Config.MONGODB_URI)
db = MONGODB_CLI.wbb
