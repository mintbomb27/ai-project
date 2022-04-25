from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from routes.citizen import router as CitizenRouter
from routes.admin import router as AdminRouter

app = FastAPI()

token_listener = JWTBearer()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(CitizenRouter, tags=["Citizen"], prefix="/student", dependencies=[Depends(token_listener)])
