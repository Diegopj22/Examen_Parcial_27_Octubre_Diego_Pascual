import numpy as np

def main():
  
  m = np.diag([1,2,3,4,5])
   
  # calcula el determinante usando la regla de Sarrus
  det = np.linalg.det(m)

  print("El determinante de la matriz es: %f" % det)
   
if __name__== "__main__":
  main()
     
  
