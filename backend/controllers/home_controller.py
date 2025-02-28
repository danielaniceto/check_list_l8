import logging

class HomeController:
    def __init__(self):
        logging.info("HOMECONTRLLER iniciada com sucesso")

    async def home(self):
        return {"message": "Bem vindo a page Home, aqui você pode escolher o que deseja fazer, "
                "escolha entre fazer o check list do veiculo ou a PTE!!!"}