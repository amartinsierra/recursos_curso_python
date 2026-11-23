from pydantic import BaseModel
class Estudiante(BaseModel):
    nombre:str
    curso:str
    nota:float
    email:str