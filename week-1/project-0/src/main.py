from fastapi import FastAPI, HTTPException
from user_dao import UserDAO
import logging
import jwt
from user_service import UserService
from dto.user_request import UserRequest
from dto.user_response import UserResponse
from dto.login_credentials import Login

logging.basicConfig(filename="user_controller.log", encoding='utf-8', filemode='a', level=logging.INFO)

logger=logging.getLogger(__name__)

app = FastAPI()


user_service = UserService()
@app.get("/users")
def get_users(user_jwt:str):
    try:
        user_info = jwt.decode(user_jwt, "secret", algorithms=["HS256"])
        print(user_info)
        id=0
        logger.info("User data retreived")
        return users
    
    except Exception as e:
        logger.error(e)
        print("Error")

@app.post("/signup")
def create_user(user_request:UserRequest):
    try:
        user_service.create_user(user_request)
        logger.info("User Created")
        return "user created"
    except Exception as e:
        logger.error("failed to create user")
        raise HTTPException(status_code=500, detail="failed to create user")

@app.post("/login")
def login(login:Login):

    return jwt.encode({"id": 1}, "secret", algorithm="HS256")


