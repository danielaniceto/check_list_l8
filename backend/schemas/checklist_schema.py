from datetime import datetime
from typing import List
from uuid import uuid4
from pydantic import BaseModel
import logging
from schemas.checklist_schema import LiberacaoAtividadeModel

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers = [logging.FileHandler("checklist_controller.log"), logging.StreamHandler()]
)

class RequestCheckListModel(BaseModel):
    request_id_check_list: str = uuid4().hex
    placa_carro: str
    nome_completo: str
    trecho: str
    data_ultima_manutencao: str
    hodometro: int
    nivel_combustivel: str
    validade_ipva: str
    conservacao_veiculo: str
    ar_condicionado: str
    cartao_abastecimento: str
    chave_ignicao: str
    cinto_seguranca: str
    farol_lanternas: str
    limpeza_interior: str
    parabrisa: str
    pneus: str
    chave_roda: str
    retrovisor: str
    tag_sem_parar: str
    triangulo_sinalizacao: str
    vidros: str
    macaco: str
    funcionamento_geral: str
    limpador_parabrisa: str
    esguicho_agua: str
    rack_escada: str
    estado_geral: str
    descricao_varias: str


    
    