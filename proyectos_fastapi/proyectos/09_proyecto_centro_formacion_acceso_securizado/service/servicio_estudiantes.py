import httpx
from model.modelo_estudiante import Estudiante
class EstudianteService:
    url="http://localhost:8000/alumnos"
    url_login="http://localhost:8000/login"
    token:str
    USERNAME="user1"
    PASSWORD="user1"
    def __init__(self):
        self.token=self.obtener_token()
    def obtener_token(self):
        try:
            response = httpx.post(self.url_login, data={"username": self.USERNAME, "password": self.PASSWORD})
            response.raise_for_status()
            return response.json().get("access_token")
        except httpx.HTTPStatusError:
            raise Exception("Error al obtener el token de acceso")
    def estudiantes_nota_min(self,nota_min:float):
        response=httpx.get(self.url)
        respuesta_json=response.json()
        return filter(lambda e:e["nota"]>=nota_min,respuesta_json)
    
    def nuevo_estudiante(self,estudiante:Estudiante):
        try:
            headers={"Authorization":f"Bearer {self.token}"}
            response=httpx.post(self.url,json=estudiante.model_dump(),headers=headers)
            response.raise_for_status()
            return True
        except httpx.HTTPStatusError:
            return False