import logging
from schemas.login_schema import RequestUserModelSchema
from database.mongo import DataBaseConnection
import hashlib

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("checklist_controller.log"), logging.StreamHandler()]
)

service_db_conection_users = DataBaseConnection.conection_db()["users"]

class LoginValidation:
    def __init__(self):
    
        if service_db_conection_users is None:
            logging.critical("A conexão com banco de dados falhou, RECORDER_CONTROLLER")
            raise ValueError("A conexão com banco falhou")
        
    def hash_password(self, password: str):
        
        #Criptografa a senha usando SHA-256.
        return hashlib.sha256(password.encode()).hexdigest()
       
    async def login_validate(self, user: RequestUserModelSchema):

        #buscando usuário por email no banco
        seach_db_user = service_db_conection_users.find_one({"email": user.email})

        #verificando se o usuário existe e se a senha está correta
        if seach_db_user is None:
            return{"error": f"Usuário {user.email} não encontrado no banco de dados!!!"}
        
        elif self.hash_password(user.password) != seach_db_user["password"]:
            return {"error": "Senha incorreta!!!"}
        
        return {"error": "Senha incorreta!!!"}
    