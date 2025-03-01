from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime

class RequestCheckListModel(BaseModel):
    request_id_check_list: str = uuid4().hex
    placa_carro: str
    nome_completo: str
    trecho: str
    data_ultima_manutencao: str
    hodometro: float
    nivel_combustivel: str
    validade_ipva: datetime
    conservacao_veiculo: str
    ar_condicionado: str
    cartao_abastecineto: str
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
