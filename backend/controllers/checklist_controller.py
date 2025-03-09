from database.mongo import DataBaseConnection
from models.db_checklist_model import RequestCheckListModel
from schemas.checklist_schema import RequestCheckListModelSchema
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from uuid import uuid4
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("checklist_controller.log"), logging.StreamHandler()]
)

class ChecklistController:
    def __init__(self):
        self.service_db_conection_check_list = DataBaseConnection.conection_db()["check_list"]

        logging.info("Conectado com sucesso ao banco de dados, CHECK LIST CONTROLLER")
        logging.info("CHECKLISTCONTRLLER iniciada com sucesso")

        if self.service_db_conection_check_list is None:
            logging.critical("A conexão com banco de dados falhou, CHECKLIST_CONTROLLER")
            raise ValueError("A conexão com banco falhou")
        
    FIELD_NAMES = {
        "placa_carro": "Placa do Carro",
        "nome_completo": "Nome Completo",
        "trecho": "Trecho",
        "data_ultima_manutencao": "Data da Última Manutenção",
        "hodometro": "Hodômetro",
        "nivel_combustivel": "Nível de Combustível",
        "validade_ipva": "Validade do IPVA",
        "conservacao_veiculo": "Conservação do Veículo",
        "ar_condicionado": "Ar Condicionado",
        "cartao_abastecimento": "Cartão de Abastecimento",
        "chave_ignicao": "Chave de Ignição",
        "cinto_seguranca": "Cinto de Segurança",
        "farol_lanternas": "Farol e Lanternas",
        "limpeza_interior": "Limpeza do Interior",
        "parabrisa": "Para-brisa",
        "pneus": "Pneus",
        "chave_roda": "Chave de Roda",
        "retrovisor": "Retrovisor",
        "tag_sem_parar": "TAG Sem Parar",
        "triangulo_sinalizacao": "Triângulo de Sinalização",
        "vidros": "Vidros",
        "macaco": "Macaco",
        "funcionamento_geral": "Funcionamento Geral",
        "limpador_parabrisa": "Limpador de Para-brisa",
        "esguicho_agua": "Esguicho de Água",
        "rack_escada": "Rack de Escada",
        "estado_geral": "Estado Geral",
        "descricao_avarias": "Descrição"
    }
    
    async def create_check_list(self, data: RequestCheckListModelSchema):
        identificador = uuid4().hex

        check_list_fields = {
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
                "descricao_avarias": data.descricao_avarias
            }
        
        try:
            with open("checklist.json", "w", encoding="utf-8") as file:
                json.dump(check_list_fields, file, ensure_ascii=False, indent=4)
            logging.info("Checklist salvo localmente como JSON.")

            response_db = self.insert_check_list_db(check_list_fields)

            self.create_pdf_check_list(check_list_fields, data)
            
            return response_db
        
        except Exception as error:
                logging.exception("Erro ao processar checklist")
                return {"erro": f"Erro ao processar checklist: {str(error)}"}
    
    def insert_check_list_db(self, check_list_fields: RequestCheckListModel):
        try:
            self.service_db_conection_check_list.insert_one(check_list_fields)
            logging.info("Checklist inserido com sucesso no banco de dados")
            return {"mensagem": "Checklist inserido com sucesso no banco de dados"}
        
        except Exception as error:
            logging.error(f"Erro ao inserir checklist no banco de dados: {str(error)}")
            return {"erro": f"Erro ao inserir checklist no banco de dados: {str(error)}"}

    def create_pdf_check_list(self, check_list_data: dict, data: RequestCheckListModelSchema):
        try:
            if not check_list_data:
                raise ValueError("Dados do checklist não encontrados")
            
            nome_completo = data.nome_completo.upper() if data.nome_completo else "NOME INDISPONÍVEL"
            placa_carro = data.placa_carro.upper() if data.placa_carro else "PLACA INDISPONÍVEL"

            file_name = f"{nome_completo}_{placa_carro}_checklist.pdf"

            check_list_pdf = canvas.Canvas(file_name, pagesize=letter)
            width, height = letter

            check_list_pdf.setFont("Helvetica-Bold", 16)
            check_list_pdf.drawCentredString(width // 2, height - 40, "Check List Veículos")

            check_list_pdf.line(50, height - 50, width - 50, height - 50)

            check_list_pdf.setFont("Helvetica", 12)
            y_position = height - 80
            left_margin = 50

            for key, value in check_list_data.items():
                label = self.FIELD_NAMES.get(key, key)
                check_list_pdf.drawString(left_margin, y_position, f"{label}: {value}")
                y_position -= 20

                if y_position < 40:
                    check_list_pdf.showPage()
                    check_list_pdf.setFont("Helvetica", 12)
                    y_position = height - 40
            
            check_list_pdf.save()
            logging.info("PDF do checklist gerado com sucesso!")

        except Exception as error:
            logging.error(f"Erro ao gerar PDF do checklist: {str(error)}")
