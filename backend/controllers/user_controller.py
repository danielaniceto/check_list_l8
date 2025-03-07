import logging
from hashlib import sha256
from backend.database.mongo import DataBaseConnection
from schemas.login_schema import RequestUserModelSchema

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("checklist_controller.log"), logging.StreamHandler()]
)

service_db_conection_users = DataBaseConnection.conection_db()["users"]

class RegisterUserController:
    def __init__(self):

        if service_db_conection_users is None:
            logging.critical("A conexão com banco de dados falhou, USER_CONTROLLER")
            raise ValueError("A conexão com banco falhou")

    def hash_password(password):
        return sha256(password.encode()).hexdigest()

    async def regiter_user(self, user: RequestUserModelSchema):
        hashed_password = self.hash_password(user.password)

        user_data = {
            "email": "usuario@example.com",
            "password": hashed_password("1234")
        }

        result = service_db_conection_users.insert_one(user_data)

        if result.inserted_id:
            logging.info(f"Usuário {user.email} registrado com sucesso.")
            return {"message": "Usuário registrado com sucesso."}
        else:
            logging.error("Falha ao registrar usuário.")
            return {"error": "Falha ao registrar usuário."}
