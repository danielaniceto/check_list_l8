import logging

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers = [logging.FileHandler("api_controller.log"), logging.StreamHandler()]
)

class RequestUserModel():
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password