# ejemploCalculadoraCientifica

from  ejemplocalculadoraObjetos import Calculadora
import math

class CalculadoraCientifica(Calculadora):
   
   def __init__(self):
      Calculadora.__init__(self)
   
   def aproximar(self,numero):
      return math.ceil(numero)
      
      
calculadora = CalculadoraCientifica()
print calculadora.aproximar(3.5)
print calculadora.sumar(2,2)
