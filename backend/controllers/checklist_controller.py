from database.mongo import DataBaseConnection
from uuid import uuid4, UUID
import logging
from schemas.checklist_schema import RequestCheckListModel

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("checklist_controller.log"), logging.StreamHandler()]
)

SERVICE_DB_CONECTION = DataBaseConnection()

class ChecklistController:
    def __init__(self):
    
        logging.info("Conectado com sucesso ao banco de dados, CHECK LIST CONTROLLER")
        logging.info("CHECKLISTCONTRLLER iniciada com sucesso")

        if SERVICE_DB_CONECTION is None:
            logging.critical("A conexão com banco de dados falhou, RECORDER_CONTROLLER")
            raise ValueError("A conexão com banco falhou") 
    
    async def create_check_list(data: RequestCheckListModel):
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
                "cartao_abastecineto": data.cartao_abastecineto,
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