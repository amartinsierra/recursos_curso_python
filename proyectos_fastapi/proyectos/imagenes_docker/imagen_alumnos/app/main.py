from fastapi import FastAPI
from controller import alumnos_controller 
from fastapi.middleware.cors import CORSMiddleware
from security import controlador_login
app=FastAPI()
#para evitar el problema de bloqueo CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(alumnos_controller.router)
app.include_router(controlador_login.routerlogin)
