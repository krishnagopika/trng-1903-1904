import sqlalchemy as db
from dotenv import load_dotenv
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from redis import Redis

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    role = db.Column(db.String(80), unique=False, nullable=False)

load_dotenv()


engine = db.create_engine(url=f"mysql+pymysql://{os.getenv('USER_NAME')}:{os.getenv('PASSWORD')}@{os.getenv('DB_URL')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}" )

cache = Redis(host=os.getenv('REDIS_DB_URL'), port=6379, db=0)

Session = sessionmaker(bind=engine)

session = Session()

def lazy_loading():
    try:
        cache.get("user_id")
    except Exception as e:

        user_id = session.query(User).filter_by(email='sample@email.com').first()

        cache.set("user_id", user_id)
        cache.expire()
lazy_loading()
print(cache.get("user_id"))