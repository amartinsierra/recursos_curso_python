import httpx
from model.modelo_estudiante import Estudiante
class EstudianteService:
    url="http://localhost:8000/alumnos"
    def estudiantes_nota_min(self,nota_min:float):
        response=httpx.get(self.url)
        respuesta_json=response.json()
        return filter(lambda e:e["nota"]>=nota_min,respuesta_json)
    
    def nuevo_estudiante(self,estudiante:Estudiante):
        try:
            response=httpx.post(self.url,json=estudiante.model_dump())
            response.raise_for_status()
            return True
        except httpx.HTTPStatusError:
            return False