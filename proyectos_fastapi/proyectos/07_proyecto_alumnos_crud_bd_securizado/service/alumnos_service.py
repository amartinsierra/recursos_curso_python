from repository.alumnos_repository import AlumnoRepository
from model.alumnos_model import AlumnoDto,AlumnoEntity
class AlumnoService:
    alumno_repository=AlumnoRepository()    
    def alta_alumno(self,alumno:AlumnoDto):
        #no puede haber alumnos con mismo email
        if self.existe_alumno(alumno.email):
            return False
        else:
            self.alumno_repository.save(AlumnoEntity(idAlumno=0,nombre=alumno.nombre,curso=alumno.curso,nota=alumno.nota,email=alumno.email))
            return True
    def existe_alumno(self,email:str):
        alumno=self.alumno_repository.findByEmail(email)
        return alumno!=None
    
    def todos_alumnos(self):
        return self.alumno_repository.findAll()
    
    def alumnos_curso(self,curso:str):
        return self.alumno_repository.findByCurso(curso)
    
    def eliminar_alumno(self, email:str):
        alumno=self.alumno_repository.findByEmail(email)
        if alumno!=None:
            self.alumno_repository.deleteByEmail(email)
        return alumno
        