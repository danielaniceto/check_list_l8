from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from controllers.login_controller import LoginValidation
from controllers.checklist_controller import ChecklistController
from controllers.home_controller import HomeController
from controllers.pte_controller import PteController
from schemas.login_schema import RequestUserModelSchema
from schemas.checklist_schema import RequestCheckListModelSchema
from schemas.pte_schema import RequestPteModelSchema

app = FastAPI()

login_controller = LoginValidation()
check_list_controller = ChecklistController()
home_controller = HomeController()
pte_controller = PteController()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, DELETE, PUTH)
    allow_headers=["*"],  # Permite todos os headers
)

@app.get("/")
def principal_rote():
    return "Rota Principal"

@app.post("/login")
async def login(user: RequestUserModelSchema):
    return JSONResponse(content= await login_controller.login_validate(user), status_code=200)

@app.get("/home")
async def home():
    return JSONResponse(content= await home_controller.home(), status_code=200)

@app.post("/checklist")
async def create_check_list(data: RequestCheckListModelSchema):
    return JSONResponse(content = await check_list_controller.create_check_list(data), status_code=201)

@app.post("/pte")
async def create_pte(data: RequestPteModelSchema):
    return JSONResponse(content = await pte_controller.create_pte(data), status_code=201)
