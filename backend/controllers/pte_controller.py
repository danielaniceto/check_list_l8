from database.mongo import DataBaseConnection
from models.db_pte_model import RequestPteModel
from uuid import uuid4
import logging
from schemas.pte_schema import RequestPteModelSchema
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("pte_controller.log"), logging.StreamHandler()]
)

service_db_conection_pte = DataBaseConnection.conection_db()["pte"]

class PteController:
    def __init__(self):
        
        logging.info("Conectado com sucesso ao banco de dados, PTE CONTROLLER")
        logging.info("PTE CONTROLLER iniciada com sucesso")

        if service_db_conection_pte is None:
            logging.critical("A conexão com banco de dados falhou, PTE_CONTROLLER")
            raise ValueError("A conexão com banco falhou")
        
    async def create_pte(self, data: RequestPteModelSchema):
        identificador = uuid4().hex

        campos_pte = {
            "uuid_pte": identificador,
            "validade": data.validade,
            "atividade": data.atividade,
            "hora_abertura": data.hora_abertura,
            "hora_fechamento": data.hora_fechamento,
            "local_trabalho": data.local_trabalho,
            "trabalho_autorizado": data.trabalho_autorizado,
            "area": data.area,
            "descricao_atividade": data.descricao_atividade,
            "empresa_setor": data.empresa_setor,
            "nomes_envolvidos_atividade": data.nomes_envolvidos_atividade,
            "riscos_potenciais": data.riscos_potenciais,
            "equipamentos_ou_produtos_utilizados": data.equipamentos_ou_produtos_utilizados,
            "precaucoes_trabalho_altura": data.precaucoes_trabalho_altura,
            "precaucoes_energia_eletrica": data.precaucoes_energia_eletrica,
            "precaucoes_abastecimento_geradores": data.precaucoes_abastecimento_geradores,
            "epis_utilizados": data.epis_utilizados,
            "epcs_utilizados": data.epcs_utilizados,
            "aspectos_ambientais": data.aspectos_ambientais,
            "impactos_ambientais": data.impactos_ambientais,
            "liberacao_trabalho": data.liberacao_trabalho
        }

        try:
            with open("pte.json", "w") as file:
                json.dump(campos_pte, file, ensure_ascii=False, indent=4)
            logging.info("PTE salvo localmente como JSON.")

        except Exception as error:
            logging.error(f"Erro ao salvar PTE localmente: {error}")
            return {f"Erro ao processar PTE: {str(error)}"}
    
    def insert_pte_db(self, campos_pte: RequestPteModel):
        try:
            service_db_conection_pte.insert_one(campos_pte)
            logging.info("PTE inserido no banco de dados com sucesso.")
            return {"PTE inserido no banco de dados com sucesso."}
        except Exception as error:
            logging.error(f"Erro ao inserir PTE no banco de dados: {error}")
            return {f"Erro ao inserir PTE no banco de dados: {error}"}
        