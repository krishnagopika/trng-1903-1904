from fastapi import FastAPI, HTTPException
import logging
logging.basicConfig(filename="user_controller.log", encoding='utf-8', filemode='a', level=logging.INFO)

logger=logging.getLogger(__name__)

app = FastAPI()


@app.get("/users")
def get_users():
    try:
        return {"users" :[
            {"id": 1, "name": "Jane Smith", "email": "jane.doe@email.com", "password": "1234"},
        ]}
    
    except Exception as e:
        logger.error(e)
        print("Error")
        raise HTTPException(500)

@app.get("/")
def get_users():
    
    return "welcome to revhire"


