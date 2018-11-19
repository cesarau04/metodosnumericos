"""
EL LIBRO TIENE UN PEQUEÑO ERROR EN LAS SOLUCIONES DEL SISTEMA DE EQUACIONES PARA EL VIENTO HACIA A LA DERECHA. POR LO DEMAS LOS RESULTADOS COINCIDIERON.
"""
def createMatrix(m,n, valor=0):
    C = []
    for i in range(m):
        C.append([])                            #could be c.append([valor]*n)
        for j in range(n):
            C[i].append(valor)
    return C

def getDimensions(A):
    return (len(A),len(A[0]))

def copyMatrix(B):
    m,n = getDimensions(B)
    A = createMatrix(m,n)
    for i in range(m):
        for j in range(n):
            A[i][j]=B[i][j]
    return A

def sumMatrix(A,B):
    Am, An = getDimensions(A)
    Bm, Bn = getDimensions(B)
    if (Am != Bm or An != Bn):
        print("Error, matrix of diferent size")
        return []
    C = createMatrix(Am,An)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] + B[i][j]
    return C

def restaMatrix(A,B):
    Am, An = getDimensions(A)
    Bm, Bn = getDimensions(B)
    if (Am != Bm or An != Bn):
        print("Error, matrix of diferent size")
        return []
    C = createMatrix(Am,An)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] - B[i][j]
    return C

def multMatrix(A,B):
    Am, An = getDimensions(A)
    Bm, Bn = getDimensions(B)
    if (An != Bm):
        print("Error multiplicacion # columnas y # renglos no son iguales")
        return []
    C = createMatrix(Am,Bn)
    counter = 0
    for i in range(Am):
        for j in range(Bn):
            for k in range(An):
                C[i][j] += A[i][k] * B[k][j]
    return C

def getAdyacente(A,r,c):
    Am, An = getDimensions(A)
    C = createMatrix(Am-1, An-1, 0)
    for i in range(Am):
        if (i == r):
            continue
        for j in range(An):
            if (j == c):
                continue
            ci = 0
            cj = 0
            if (i < r):
                ci = i
            else:
                ci = i-1
            if (j < c):
                cj = j
            else:
                cj = j-1
            C[ci][cj] = A[i][j]
    return C

def detMatrix(A):
    m,n = getDimensions(A)
    if m!=n:
        print("Matriz no es cuadrada")
        return []
    if (n==1):
        return A[0][0]
    if (n==2):
        return (A[0][0]*A[1][1]) - (A[1][0]*A[0][1])
    det = 0
    for j in range(m):
        det += (-1)**j*A[0][j]*detMatrix(getAdyacente(A,0,j))
    return det

def getMatrizTranspuesta(A):
    m,n = getDimensions(A)
    C = createMatrix(n,m,0)
    for i in range(m):
        for j in range(n):
            C[j][i] = A[i][j]
    return C

def getMatrizAdjunta(A):
    m,n = getDimensions(A)
    if m != n:
        print("La matriz no es cuadrada")
        return []
    C = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j] = ((-1)**(i+j))*detMatrix(getAdyacente(A,i,j))
    return C

def getMatrizInversa(A):
    m,n = getDimensions(A)
    if m != n:
        print("La matriz no es cuadrada")
        return []
    detA = detMatrix(A)
    if detA== 0:
        print("La matriz no tiene inversa")
        return []
    At = getMatrizTranspuesta(A)
    adjA = getMatrizAdjunta(At)
    invDetA = 1/detA
    C = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j]=invDetA*adjA[i][j]
    return C

A = createMatrix(6,6)
C = createMatrix(6,1)

#Sistema de equaciones
A[0] = [0.866,0,-0.5,0,0,0]
A[1] = [0.5,0,0.866,0,0,0]
A[2] = [-0.866,-1,0,-1,0,0]
A[3] = [-0.5,0,0,0,-1,0]
A[4] = [0,1,0.5,0,0,0]
A[5] = [0,0,-0.866,0,0,-1]

#[0 -1000 0 0 0 0]
C[0] = [0]
C[1] = [-1000]
C[2] = [0]
C[3] = [0]
C[4] = [0]
C[5] = [0]

#Solucion del sistema
A1 = getMatrizInversa(A)
B = multMatrix(A1,C)
print(B)

#Viento IZQ
#[-1000 0 1000 0 0 0]
C[0] = [-1000]
C[1] = [0]
C[2] = [1000]
C[3] = [0]
C[4] = [0]
C[5] = [0]
D = multMatrix(A1,C)
print(D)

#Viento DER
#[-1000 0 0 0 -1000 0]
C[0] = [-1000]
C[1] = [0]
C[2] = [0]
C[3] = [0]
C[4] = [-1000]
C[5] = [0]
F = multMatrix(A1,C)

print(F)
