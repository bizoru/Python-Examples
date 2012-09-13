# ejemplocalculadora

class Calculadora:
  
   def __init__(self):
       self._modelo = 'HP'
       print 'construido'

   def getModelo(self):
        return self._modelo

   def sumar(self,a,b):  # Pueden Haber Errores!
       return a + b

   def restar(self,a,b):
      return a - b

   def dividir(self,a,b):
      return a / b
   
   def multiplicar(self,a,b):
      return a*b
   
   


calculadora = Calculadora()
print calculadora.getModelo()
print calculadora.sumar(1,2)
print calculadora.dividir(2.0,3.0)
print calculadora.multiplicar(2,3)





