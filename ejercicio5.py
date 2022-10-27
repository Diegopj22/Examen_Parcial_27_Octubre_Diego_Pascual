import numpy as np

def main():
  
  m = np.array([(1, 2, 3), (2, 5, 2), (1, 3, 1),(2,3,2),(4,1,2)])
   
  # calcula el determinante usando la regla de Sarrus
  det = ((m[0][0] * m[1][1] * m[2][2]) + (m[0][1]  
    * m[1][2] * m[2][0]) + (m[0][2] * m[1][0] * m[2][1])) - ((m[2][0] 
    * m[1][1] * m[0][2]) + (m[2][1]  * m[1][2] * m[0][0]) + (m[2][2] 
    * m[1][0] * m[0][1]))

  print("El determinante de la matriz es: %f" % det)
   
if __name__== "__main__":
  main()
     
  
