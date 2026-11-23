
from typing import List
from fastapi import APIRouter, HTTPException, Response
from service.alumnos_service import AlumnoService
from model.modelo_alumno import Alumno
router=APIRouter()
alumno_service=AlumnoService()
@router.post(path="/alumnos",response_model=Alumno)
def alta_alumno(alumno:Alumno,response:Response):
    if alumno_service.alta_alumno(alumno):
        response.status_code=200
        return alumno
    raise HTTPException(status_code=409,detail="Email ya existente")
@router.get(path="/alumnos",response_model=List[Alumno])
def todos_alumnos():
    return alumno_service.todos_alumnos()
@router.get(path="/alumnos/porcurso",response_model=List[Alumno])
def alumnos_por_curso(curso:str):
    return alumno_service.alumnos_curso(curso)  
@router.delete(path="/alumnos",response_model=Alumno)
def eliminar_alumno(email:str):
    return alumno_service.eliminar_alumno(email) 