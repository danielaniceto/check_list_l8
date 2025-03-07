import logging
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers = [logging.FileHandler("login_schema.log"), logging.StreamHandler()]
)

class RequestUserModelSchema(BaseModel):
        email:str
        password: str
