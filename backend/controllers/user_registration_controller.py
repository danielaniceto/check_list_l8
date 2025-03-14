import asyncio
from backend.schemas.login_schema import RequestUserModelSchema
from backend.controllers.user_controller import RegisterUserController

# Criando uma instância do controlador
controller = RegisterUserController()

# Criando um usuário de teste
test_user = RequestUserModelSchema(email="usuarioteste@exampleemail.com", password="5678")

# Registrando o usuário (chamando dentro do asyncio, pois é async)
asyncio.run(controller.register_user(test_user))
