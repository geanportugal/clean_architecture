from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from sqlalchemy import create_engine

engine = create_engine(SQLALCHEMY_URL, pool_size=5, max_overflow=5)

Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
