from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import os

engine = create_engine(os.getenv('DATABASE_URL'))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class DbSession:
    db = db_session
    func = func

def init_db():
    import src.models
    Base.metadata.create_all(bind=engine)
