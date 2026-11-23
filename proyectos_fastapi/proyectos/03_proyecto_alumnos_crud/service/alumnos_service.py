from model.modelo_alumno import Alumno
class AlumnoService:
    alumnos:list[Alumno]=[]
    
    def alta_alumno(self,alumno:Alumno):
        #no puede haber alumnos con mismo email
        if self.existe_alumno(alumno.email):
            return False
        else:
            self.alumnos.append(alumno)
            return True
    def existe_alumno(self,email:str):
        for a in self.alumnos:
            if a.email==email:
                return True
        return False
    
    def todos_alumnos(self):
        return self.alumnos
    
    def alumnos_curso(self,curso:str):
        return list(filter(lambda a:a.curso==curso,self.alumnos))
    
    def eliminar_alumno(self, email:str):
        pos_eliminar=-1
        i=0
        alumno_eliminado=None
        for a in self.alumnos:
            if a.email==email:
                pos_eliminar=i
                alumno_eliminado=a
                break
            i=i+1
        if pos_eliminar!=-1:
            self.alumnos.pop(pos_eliminar)
        return alumno_eliminado
        