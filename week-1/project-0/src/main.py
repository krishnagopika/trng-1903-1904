from fastapi import FastAPI
from user import User
from user_dao import UserDAO
import logging
import jwt

from login_credentials import Login

logging.basicConfig(filename="user_controller.log", encoding='utf-8', filemode='a', level=logging.INFO)

logger=logging.getLogger(__name__)

app = FastAPI()


@app.get("/users")
def get_users(user_jwt:str):
    try:
        user_info = jwt.decode(user_jwt, "secret", algorithms=["HS256"])
        print(user_info)
        id=0
        user_dao = UserDAO()
        users = user_dao.get_users(id)
        logger.info("User data retreived")
        return users
    
    except Exception as e:
        logger.error(e)
        print("Error")

@app.post("/signup")
def create_user(user:User):
    user_dao = UserDAO()
    print(type(user))
    return user_dao.create_user(user)

@app.post("/login")
def login(login:Login):

    return jwt.encode({"id": 1}, "secret", algorithm="HS256")


