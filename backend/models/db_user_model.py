from pydantic import BaseModel
from uuid import uuid4

class LoginUserModel(BaseModel):
    user_id: str = uuid4().hex
    user_email: str
    user_password: str
    