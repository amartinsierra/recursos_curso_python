
from fastapi import FastAPI
from controller import controlador_estudiantes

app=FastAPI()
app.include_router(controlador_estudiantes.router)