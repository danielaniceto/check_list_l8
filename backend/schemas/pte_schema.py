from datetime import datetime
from typing import List
from uuid import uuid4
from pydantic import BaseModel
import logging

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers = [logging.FileHandler("pte_schema.log"), logging.StreamHandler()]
)

class LiberacaoAtividadeModel(BaseModel):
    emitente: str
    responsavel_equipe: str

class RequestPteModelSchema(BaseModel):
    request_id_pte: str = uuid4().hex
    validade: datetime
    atividade: datetime
    hora_abertura: datetime
    hora_fechamento: datetime
    local_trabalho: str
    trabalho_autorizado: str
    area: str
    descricao_atividade: str
    empresa_setor: str
    nomes_envolvidos_atividade: List[str]
    riscos_potenciais: List[str]
    equipamentos_ou_produtos_utilizados: List[str]
    precaucoes_trabalho_altura: List[str]
    precaucoes_energia_eletrica: List[str]
    precaucoes_abastecimento_geradores: List[str]
    epis_utilizados: List[str]
    epcs_utilizados: List[str]
    aspectos_ambientais: List[str]
    impactos_ambientais: List[str]
    liberacao_trabalho: List[LiberacaoAtividadeModel]
