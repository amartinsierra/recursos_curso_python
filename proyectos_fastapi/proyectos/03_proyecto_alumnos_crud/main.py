from fastapi import FastAPI
from controller import alumnos_controller
app=FastAPI()
app.include_router(alumnos_controller.router)
