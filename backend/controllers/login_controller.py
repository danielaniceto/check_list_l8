import logging
import jwt
import datetime
from schemas.login_schema import RequestUserModelSchema
from database.mongo import DataBaseConnection
import hashlib
from fastapi import HTTPException

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("checklist_controller.log"), logging.StreamHandler()]
)

SECRET_KEY = "ProjetoL8Checklist"
service_db_conection_users = DataBaseConnection.conection_db()["users"]

class LoginValidation:
    def __init__(self):
        if service_db_conection_users is None:
            logging.critical("A conexão com banco de dados falhou, RECORDER_CONTROLLER")
            raise ValueError("A conexão com banco falhou")
        
    def hash_password(self, password: str):
        # Criptografa a senha usando SHA-256.
        return hashlib.sha256(password.encode()).hexdigest()
       
    async def login_validate(self, user: RequestUserModelSchema):
        # Buscando usuário por email no banco
        seach_db_user = service_db_conection_users.find_one({"email": user.email})

        # Verificando se o usuário existe
        if seach_db_user is None:
            raise HTTPException(status_code=404, detail=f"Usuário {user.email} não encontrado no banco de dados!!!")
        
        # Verificando se a senha está correta
        if self.hash_password(user.password) != seach_db_user["password"]:
            raise HTTPException(status_code=401, detail="Senha incorreta!!!")
        
        # **Gerando o token JWT**
        payload = {
            "sub": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expira em 1 hora
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        
        # Se chegou aqui, significa que as credenciais estão corretas
        return {"message": "Login bem-sucedido!", "token": token}
