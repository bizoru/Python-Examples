# Ejemplo de URLib2

import urllib2

url = 'http://www.google.com'
sitioweb = urllib2.urlopen(url)   # Recuerda Aqui no hay comas!
contenido = sitioweb.read()
sitioweb.close()

print contenido
