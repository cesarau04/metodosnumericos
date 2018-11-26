En estadística, la regresión no lineal es un problema de inferencia para un modelo tipo:

    y = f (x,θ) + ε

basado en datos multidimensionales x, y, donde f es alguna función no lineal respecto a algunos parámetros desconocidos θ. Como mínimo, se pretende obtener los valores de los parámetros asociados con la mejor curva de ajuste (habitualmente, con el método de los mínimos cuadrados). Con el fin de determinar si el modelo es adecuado, puede ser necesario utilizar conceptos de inferencia estadística tales como intervalos de confianza para los parámetros así como pruebas de bondad de ajuste.

El objetivo de la regresión no lineal se puede clarificar al considerar el caso de la regresión polinomial, la cual es mejor no tratar como un caso de regresión no lineal. Cuando la función f toma la forma:

    f(x) = ax^2 + bx + c 

la función f es no lineal en función de x pero lineal en función de los parámetros desconocidos a, b, y c. Este es el sentido del término "lineal" en el contexto de la regresión estadística. Los procedimientos computacionales para la regresión polinomial son procedimientos de regresión lineal (múltiple), en este caso con dos variables predictoras x y x^2. Sin embargo, en ocasiones se sugiere que la regresión no lineal es necesaria para ajustar polinomios. Las consecuencias prácticas de esta mala interpretación conducen a que un procedimiento de optimización no lineal sea usado cuando en realidad hay una solución disponible en términos de regresión lineal. Paquetes (software) estadísticos consideran, por lo general, más alternativas de regresión lineal que de regresión no lineal en sus procedimientos. 

Recuperado de: https://es.wikipedia.org/wiki/Regresi%C3%B3n_no_lineal#Regresi%C3%B3n_polinomial
