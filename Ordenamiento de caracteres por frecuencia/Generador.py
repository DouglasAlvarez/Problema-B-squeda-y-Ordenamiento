import random

class Generador_texto:

    def __init__(self):
        self.caracteres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
    def generador_tamanio_texto(self):
        return random.randint(1,100)
    
    def generador_texto_aleatorio(self):
        texto = ""
        for i in range(self.generador_tamanio_texto()):
            texto += random.choice(self.caracteres)
        return texto 
