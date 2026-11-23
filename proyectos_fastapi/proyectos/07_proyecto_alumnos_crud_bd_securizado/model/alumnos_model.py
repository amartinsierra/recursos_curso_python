from pydantic import BaseModel

class AlumnoEntity(BaseModel):
    idAlumno:int
    nombre:str
    curso:str
    nota:float
    email:str
    
class AlumnoDto(BaseModel):
    nombre:str
    curso:str
    nota:float
    email:str