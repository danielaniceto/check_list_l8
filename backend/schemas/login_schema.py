import logging

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers = [logging.FileHandler("login_schema.log"), logging.StreamHandler()]
)

class RequestUserModelSchema():
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
