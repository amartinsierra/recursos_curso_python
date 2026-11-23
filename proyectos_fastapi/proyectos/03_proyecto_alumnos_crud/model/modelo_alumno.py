from pydantic import BaseModel
class Alumno(BaseModel):
    nombre:str
    curso:str
    nota:float
    email:str