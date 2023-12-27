from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from sqlalchemy import create_engine
from configs.config import DB_URI

engine = create_engine(DB_URI, pool_size=5, max_overflow=5)

Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
