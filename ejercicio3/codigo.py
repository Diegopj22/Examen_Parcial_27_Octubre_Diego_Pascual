class Alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def __str__(self):
         return(self.nombre,self.nota)
    
    
    def calificacion (self):
        if self.nota < 5 :
            print("Suspenso")
        else:
            print("Aprobado") 
    


        