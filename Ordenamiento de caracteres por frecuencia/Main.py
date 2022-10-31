from Generador import Generador_texto

class Solution:

    def frequencySort(self, s: str) -> str:
        output = []
        for letter in set(s):
            count = s.count(letter)  
            output.append(letter*count) 
        output = sorted(output, key=len, reverse = True) 
        return "".join(output)
    
for i in range (100):  
      
    mi_texto = Generador_texto()
    texto_aorden = mi_texto.generador_texto_aleatorio() 
    print("caso "+ str(i)+": " + str(texto_aorden) ) 
           
    solucion = Solution()
    palabra_orden = solucion.frequencySort(texto_aorden)
    print("resultado caso "+ str(i)+": " + str(palabra_orden))
    print("\n") 
