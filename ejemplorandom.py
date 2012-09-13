# Ejemplo random

import random

elementos = '123456789'
eleccion = random.choice(elementos)
print eleccion


elementos = ['a','b','c','e','f']
random.shuffle(elementos)
print elementos


escogidos = random.sample(elementos,3)
print escogidos



