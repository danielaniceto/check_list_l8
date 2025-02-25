from pymongo import MongoClient, errors
import logging

logging.basicConfig(
    level=logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [logging.FileHandler("database_connection.log"), logging.StreamHandler()]
)

class DataBaseConnection():
    def conection_db():
        url_conection_db = "mongodb+srv://daniel_l8:1234@cluster0.p5fb5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        try:
            logging.info("Conectando ao Banco de Dados, MONGODB")

            client = MongoClient(url_conection_db, serverSelectionTimeoutMS=50000)
            db = client["dbtest"]
            logging.info(f"Conectado com sucesso ao banco de dados, MONGODB")

            client.admin.command("ping")
            logging.info("Conexão feita com sucesso, MONGODB!!!")

            return db
        
        except errors.ServerSelectionTimeoutError:
            logging.error("Erro: Não foi possível conectar ao MongoDB, verifique a string de conexão ou a disponibilidade do servidor.")
        
        except errors.ConnectionFailure:
            logging.error("Erro: Falha na conexão com o MongoDB.")

        except Exception as error:
            logging.error(f"Erro inesperado: {error}")

        return None
