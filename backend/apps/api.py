from fastapi import FastAPI
from fastapi.responses import JSONResponse
from controllers.login_controller import LoginValidation
from controllers.checklist_controller import ChecklistController
from controllers.home_controller import HomeController
from schemas.login_schema import RequestUserModel
from schemas.checklist_schema import RequestCheckListModel

app = FastAPI()

login_controller = LoginValidation
check_list_controller = ChecklistController
home_controller = HomeController

@app.post("/api/login")
async def rota_login(user: RequestUserModel):
    return JSONResponse(content= await login_controller.login_validate(user), status_code=200)

@app.get("api/home")
async def rota_home():
    return JSONResponse(content= await home_controller.home(), status_code=200)


@app.post("/checklist")
async def create_check_list(data: RequestCheckListModel):
    return JSONResponse(content = await check_list_controller.create_check_list(data), status_code=201)
