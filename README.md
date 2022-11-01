# Problema-Busqueda-y-Ordenamiento :computer:

![version](https://i.ytimg.com/vi/QrM2ofM5Dz4/maxresdefault.jpg) 

## Tabla de Contenido

* [Algoritmo:memo:](#Algoritmos)
* [Herramientas Utilizadas :memo:](#Herramientas)
* [Documentacion :memo:](#Documentacion)
* [Video :memo:](#Video)
* [Autores :memo:](#autores)
* [Conclusiones :memo:](#Conclusiones)
* [Bibliografía :memo:](#bibliografía)

## Algoritmo
_El algoritmo utilizado para el desarrollo del trabajo fue:_
* <b> Sort Characters By Frequency </b>
Dada una cadena s, ordénela en orden decreciente según la frecuencia de los caracteres. La frecuencia de un carácter es el número de veces que aparece en la cadena. Devuelve la cadena ordenada. Si hay varias respuestas, devuelve cualquiera de ellas.

[![codigo.png](https://i.postimg.cc/jSCcnxjm/codigo.png)](https://postimg.cc/3k5mPHmF)

Ejemplo 1:
* <b>Input: s = "tree" </b>
* <b>Output: "eert" </b>
* <b>Explicación: El caracter 'e' aparece al principio del string ya que aparec dos veces en el string y las letras 't' y  'r' solo una vez; el resultado "eert" tambien es una solucion valida. </b>

Ejemplo 2:
* <b>Input: s = "cccaaa" </b>
* <b>Output: "aaaccc" </b>
* <b>Explicación: Ambos caracteres aparecen tres veces, entonces la solucion "cccaaa" tambien es valida, la solucion "cacaca" es incorrecta ya que el mismo caracter debe estar junto. </b>

Ejemplo 3:
* <b>Input: s = "Aabb" </b>
* <b>Output: "bbAa" </b>
* <b>Explicación: la solucion "bbaA" tambien es una respuesta valida, pero "Aabb" es incorrecto ya que el caracter 'A' y 'a' son tratados como 2 caracteres distintos. </b>

## Herramientas 

_Las herramientas utilizadas para el desarrollo del trabajo fueron:_

* [Python](https://www.python.org) - Lenguaje de Programación
* [LeetCode](https://leetcode.com) - Plataforma Web
* [Visual Studio Code](https://code.visualstudio.com) - Editor de Código Fuente

<p
   align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" width="64" height="64" margin-right: 20px><img src="https://cdn.cdo.mit.edu/wp-content/uploads/sites/67/2021/01/0_zuhXdNAIUoxEem4-.png" width="68" height="64" >
   <img src="https://www.comparasoftware.com/wp-content/uploads/2018/08/logovisualstudiocode.png" width="80" height="64" >
</p>

## Documentacion
_Puedes visualizar la documentacion en el siguiente enlace:_ 
* [Problema de Búsqueda y Ordenamiento](https://drive.google.com/file/d/1QjYKfQIAtwfXIXyRdrumAjz1Rio7u3C1/view)

## Video
_Puedes visualizar el video realizado en el siguiente enlace:_
* [Sort Characters By Frequency - 1151923, 1151925.](https://youtu.be/-atBgm_LVSA)

## Autores
* DOUGLAS ARLEY ALVAREZ OCHOA - 1151923
* SAID FERNANDO LOPEZ GONZALES - 1151925

## Conclusiones
* La respuesta de salida que nos puede arrojar el algoritmo Sort Characters By Frequency, como por ejemplo que se ingrese la palabra "tree", este nos arrojaría de salidas "eert" y también "eetr", ambas son válidas ya que están ordenados ante todo por el nivel de frecuencia.
* Si los caracteres dados en la entrada presentan la misma frecuencia, las salidas de estos podrán estar de principio o de final, por ejemplo: la entrada "cccaaa", el string respuesta podrá ser de la forma "aaaccc" o como estuvo al principio de la forma "cccaaa".
* Las entradas que presentan caracteres de la misma letra pero en mayúsculas serán tomadas como caracteres independientes a sus homogéneos en minúsculas.

## Bibliografía

* Problema realizado en <b> Python </b> tomado de la plataforma web <b> [LeetCode] *(https://leetcode.com/problems/sort-characters-by-frequency/)
* Desafío para desarrolladores (https://www.grupodigital.eu/blog/desafios-para-desarrolladores/#8_LeetCode)
