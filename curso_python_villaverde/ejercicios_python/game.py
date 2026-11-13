class Arma:
    nombre=""
    potencia=0
    peso=0
    def __init__(self,nombre,potencia,peso):
        self.nombre=nombre
        self.potencia=potencia
        self.peso=peso
    def ataque(self):
        return self.potencia+2*self.peso   
class Personaje:
    nombre=""
    tipo=""
    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo       
class Protagonista(Personaje):
    nivel_acceso:0
    def __init__(self, nombre, tipo,nivel_acceso=2):
        super().__init__(nombre, tipo)
        self.nivel_acceso=nivel_acceso
    def avanzar(self):
        print("avance básico")
class Avatar(Protagonista):
    categoria:0
    def avanzar(self):
        if self.categoria>10:
           print("fin del juego") 
        else:
            super().avanzar()
    