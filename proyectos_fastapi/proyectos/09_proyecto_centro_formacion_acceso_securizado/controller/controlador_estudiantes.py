
from typing import List
from fastapi import APIRouter, HTTPException,Response
from service.servicio_estudiantes import EstudianteService
from model.modelo_estudiante import Estudiante
router=APIRouter()
estudiante_service=EstudianteService()
@router.get(path="/estudiantes/{nota}",response_model=List[Estudiante])
def estudiantes_nota(nota:float):
    return estudiante_service.estudiantes_nota_min(nota)
@router.post(path="/estudiantes",response_model=Estudiante)
def nuevo_estudiante(estudiante:Estudiante,response:Response):
    if(estudiante_service.nuevo_estudiante(estudiante)):
        response.status_code=200
        return estudiante
    raise HTTPException(status_code=409,detail="Email repetido")