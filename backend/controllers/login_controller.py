import logging
from schemas.login_schema import RequestUserModel
from database.mongo import DataBaseConnection

SERVICE_DB_CONECTION = DataBaseConnection()["users"]

class LoginValidation:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[logging.FileHandler("checklist_controller.log"), logging.StreamHandler()]

            if SERVICE_DB_CONECTION is None:
            logging.critical("A conexão com banco de dados falhou, RECORDER_CONTROLLER")
            raise ValueError("A conexão com banco falhou") 
)
        
    def validate(data: RequestUserModel):
        if self.user.username == 'admin' and self.user.password == 'admin':
            return True
        return False