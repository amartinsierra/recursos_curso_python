
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from security.security_config import crear_token,autenticar

routerlogin = APIRouter()

@routerlogin.post("/login")
#con Depends() se extraen los datos de la petición y se proporcionan
#a un objeto OAuth2PasswordRequestForm, que es referenciado por la variable form
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = autenticar(form.username, form.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = crear_token(user)
    return {"access_token": token, "token_type": "bearer"}