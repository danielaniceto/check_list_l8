from database.mongo import DataBaseConnection
from models.db_checklist_model import RequestCheckListModel
from uuid import uuid4
import logging
from schemas.checklist_schema import RequestCheckListModelSchema
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("checklist_controller.log"), logging.StreamHandler()]
)

service_db_conection_check_list = DataBaseConnection.conection_db()["check_list"]

class ChecklistController:
    def __init__(self):
    
        logging.info("Conectado com sucesso ao banco de dados, CHECK LIST CONTROLLER")
        logging.info("CHECKLISTCONTRLLER iniciada com sucesso")

        if service_db_conection_check_list is None:
            logging.critical("A conexão com banco de dados falhou, RECORDER_CONTROLLER")
            raise ValueError("A conexão com banco falhou") 
    
    async def create_check_list(self, data: RequestCheckListModelSchema):
        identificador = uuid4().hex

        campos_check_list = {
                "uuid_check_list": identificador,
                "placa_carro": data.placa_carro,
                "nome_completo": data.nome_completo,
                "trecho": data.trecho,
                "data_ultima_manutencao": data.data_ultima_manutencao,
                "hodometro": data.hodometro,
                "nivel_combustivel": data.nivel_combustivel,
                "validade_ipva": data.validade_ipva,
                "conservacao_veiculo": data.conservacao_veiculo,
                "ar_condicionado": data.ar_condicionado,
                "cartao_abastecimento": data.cartao_abastecimento,
                "chave_ignicao": data.chave_ignicao,
                "cinto_seguranca": data.cinto_seguranca,
                "farol_lanternas": data.farol_lanternas,
                "limpeza_interior": data.limpeza_interior,
                "parabrisa": data.parabrisa,
                "pneus": data.pneus,
                "chave_roda": data.chave_roda,
                "retrovisor": data.retrovisor,
                "tag_sem_parar": data.tag_sem_parar,
                "triangulo_sinalizacao": data.triangulo_sinalizacao,
                "vidros": data.vidros,
                "macaco": data.macaco,
                "funcionamento_geral": data.funcionamento_geral,
                "limpador_parabrisa": data.limpador_parabrisa,
                "esguicho_agua": data.esguicho_agua,
                "rack_escada": data.rack_escada,
                "estado_geral": data.estado_geral,
                "descricao_varias": data.descricao_varias
            }
        
        try:
            with open("checklist.json", "w") as file:
                json.dump(campos_check_list, file, ensure_ascii=False, indent=4)
            logging.info("Checklist salvo localmente como JSON.")

            return self.insert_check_list_db(campos_check_list)
        
        except Exception as error:
                logging.error(f"Erro ao processar checklist: {str(error)}")
                return {"erro": f"Erro ao processar checklist: {str(error)}"}
    
    def insert_check_list_db(self, campos_check_list: RequestCheckListModel):
        try:
            service_db_conection_check_list.insert_one(campos_check_list)
            logging.info("Checklist inserido com sucesso no banco de dados")
            return {"mensagem": "Checklist inserido com sucesso no banco de dados"}
        
        except Exception as error:
            logging.error(f"Erro ao inserir checklist no banco de dados: {str(error)}")
            return {"erro": f"Erro ao inserir checklist no banco de dados: {str(error)}"}
