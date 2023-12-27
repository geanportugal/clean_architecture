""" Configuration file
"""


import os
from dotenv import load_dotenv


load_dotenv()


DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_DRIVER = "postgresql+psycopg2"

SECRET_KEY_CARD = os.getenv("SECRET_KEY_CARD")
SALT = os.getenv("SALT")
DB_URI = f"{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
