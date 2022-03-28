from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ as env

from dotenv import load_dotenv
load_dotenv()

db_user = env['db_user']
db_password = env['db_password']
db_host = env['db_host']
db_dbname = env['db_dbname']


SQLALCHAMY_DATABASE_URL = f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_dbname}'

engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
