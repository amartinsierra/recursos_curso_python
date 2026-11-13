class Notas_Service:
    dir_fichero="notas.txt"
    def __init__(self):
        try:
            f=open(self.dir_fichero,"r")
            f.close()
        except FileNotFoundError:
            f=open(self.dir_fichero,"w")
            f.close()
    def nueva_nota(self,nota):
        with open(self.dir_fichero,"a") as f:
            f.write(nota+"\n")
            
    def aprobados(self):
        with open(self.dir_fichero,"r") as f:      
            aprobados=0
            linea=f.readline()
            while(linea!=""):
                if int(linea.strip())>=5:
                    aprobados+=1
                linea=f.readline()
        return aprobados
    def nota_baja(self):
        with open(self.dir_fichero,"r") as f:
            notas=f.readlines()
        return min(notas,key=lambda n:int(n.strip()))
    def nota_alta(self):
        with open(self.dir_fichero,"r") as f:
            notas=f.readlines()
        return max(notas,key=lambda n:int(n.strip()))
    def media(self):
        with open(self.dir_fichero,"r") as f:
            notas=f.readlines()
        if not notas:
            return 0
        return sum([int(n.strip()) for n in notas])/len(notas)
    def mostrar_notas(self):
        with open(self.dir_fichero,"r") as f:
            return [int(n.strip()) for n in f.readlines()]
    #programa principal
    #intento abrir el fichero como lectura y si no existe lo creamos
    

