from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from controllers.login_controller import LoginValidation
from controllers.checklist_controller import ChecklistController

app = FastAPI()

login_controller = LoginValidation
check_list_controller = ChecklistController

@app.post("/login")
def rota_princial():
    return "login.html"

@app.get("validar_login")
async def login(data: username, password):
    return JSONResponse(content = await login_controller.validate(data), status_code=201)

@app.post("/checklist")
async def create_check_list(data: RequestCheckListModel):
    return JSONResponse(content = await check_list_controller.create_check_list(data), status_code=201)
