"""
========================================================
LIBRERÍA DE OPERACIONES DE VECTORES Y MATRICES COMPLEJAS
========================================================
"""

#
import numpy as np
import OperacionesNumerosComplejos as nc

#####################################
# Extrae la columna j de la matriz W
#####################################
def columna(j, W):
    Z = [0]*len(W)
    k = 0
    for i in W:
        Z[k] = [i[j]]
        k = k+1
    return Z

########################################################################
# Hace la operación componente a componente de una fila por una columna
########################################################################
def fila_por_columna(V, W):
    t = [0, 0]
    for i in range(len(V)):
        t = nc.suma(t, nc.producto(V[i], W[i][0]))
    return t  

###################################################################
# Retorna una matriz llena de 0's de las dimensiones especificadas
###################################################################
def matriz_cero(m, n):
    C = [[0]*n for fila in range(m)]
    return C

###########################
# Multiplicar dos matrices
###########################
def producto_de_matrices(A, B):
    f = len(A)       # Número de de filas de A
    c = len(B[0])    # Número de columnas de B
    C = matriz_cero(f, c)  # C es una lista matriz con las dimensiones de AB
    for i in range(f):
        for j in range(c):
            C[i][j] = fila_por_columna(A[i], columna(j, B))
    return C  

#############################################    
# Produce una matriz con entradas aleatorias
#############################################
def matriz_aleatoria(m, n):
    A = matriz_cero(m, n)
    for i in range(m):
        for j in range(n):
            A[i][j] = [np.random.randint(-9,9), np.random.randint(-9,9)]
    return A

############################
# Matriz transpuesta
############################
def transpuesta(A):
    f = len(A)
    c = len(A[0])
    B = matriz_cero(c, f)
    for i in range(c):
        for j in range(f):
            B[i][j] = A[j][i]
    return B

############################
# Matriz conjugada
############################
def conjugada(A):
    f = len(A)
    c = len(A[0])
    B = matriz_cero(f, c)
    for i in range(f):
        for j in range(c):
            B[i][j] = nc.conjugado(A[i][j])
    return B

#############################
# Matriz adjunta (daga)
#############################
def adjunta(A):
    B = conjugada(transpuesta(A))
    return B 

###############################
# Producto interno de vectores
###############################
def producto_interno(V, W):
    Z = producto_de_matrices(adjunta(V), W)
    return Z[0][0]

##############################
# Norma de un vector
#############################
def norma_vector(V):
    n = np.sqrt(producto_interno(V, V))
    return n[0]

##########################
# Suma de vectores
##########################
def suma_de_vectores(V,W):
    f = len(V)
    B = matriz_cero(f, 1)
    for i in range(f):
        B[i][0] = nc.suma(V[i][0], W[i][0])
    return B

###########################
# Suma de matrices
###########################
def suma_de_matrices(A, B):
    f = len(A)
    c = len(A[0])
    C = matriz_cero(f, c)
    for i in range(f):
        for j in range(c):
            C[i][j] = nc.suma(A[i][j], B[i][j])
    return C

########################
# Escalar por matriz
########################
def escalar_por_matriz(z, A):
    f = len(A)
    c = len(A[0])
    B = matriz_cero(f, c)
    for i in range(f):
        for j in range(c):
            B[i][j] = nc.producto(z, A[i][j])
    return B

########################
# Producto tensorial
########################
def producto_tensorial(A, B):
    f_A = len(A)
    c_A = len(A[0])
    f_B = len(B)
    c_B = len(B[0])
    f_T = f_A * f_B
    c_T = c_A * c_B
    T = matriz_cero(f_T, c_T)
    for i in range(f_T):
        for j in range(c_T):
            T[i][j] = nc.producto(A[i // f_B][j // c_B], B[i % f_B][j % c_B])
    return T