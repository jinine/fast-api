from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'sqlite:///./test.db'
engine = create_engine(db_url, connect_args={"check_same_thread": False})
Base = declarative_base()
Session = sessionmaker(bind=engine)
