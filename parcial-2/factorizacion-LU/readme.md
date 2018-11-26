Suponga que la matriz A es una matriz m×n se puede escribir como el producto de dos matrices:
A = LU
donde L es una matriz triangular inferior m×m y U es una matriz escalonada m × n. Entonces para resolver el sistema:
Ax = b,
escribimos 
Ax= (LU)x =L(Ux).

Una posible estrategia de solución consiste en tomar y = Ux y resolver para y:
Ly = b.

Una vez con los valores encontrados de y, las incognitas al sistemainicial se resuelve despejando x de 
Ux = y.

Nuevamente, como U es escalonada, este sistema puede resolverse en caso de tener soucion mediante sustitucion hacia atras, lo cual es sencillo.
Estas observaciones nos dan la pauta para ver la conveniencia de una factorizacion como la anterior, es decir factorizar A como el producto de una matriz L triangular superior, por otra U la cual es escalonada. Esta factorizaci ́on se llama usualmente Descomposici ́on LU
