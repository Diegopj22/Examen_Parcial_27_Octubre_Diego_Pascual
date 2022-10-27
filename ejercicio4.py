class Alumno2:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

          
    
    def __str__(self):
        return '''
        nombre\t{}´
        nota\t{}
        
        '''.format(self.nombre,self.nota)
        
    
    
    def calificacion (self):
        if self.nota < 5 :
            print("Suspenso")
        else:
            print("Aprobado") 
    
carlos=Alumno2("carlos ",1)
pedro=Alumno2(" pedro ",10)

print(carlos,pedro)