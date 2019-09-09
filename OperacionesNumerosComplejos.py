"""
========================================================
LIBRERÍA DE OPERACIONES BÁSICAS ENTRE NÚMEROS COMPLEJOS
========================================================
"""

#
import numpy as np

##############################
# Imprimir un número complejo
##############################
def imprimir(z):
    """
    Recibe una lista [a, b] e imprime un número complejo en formato a + ib
    """
    signo = ""
    if z[1] == 0:
        print(z[0], end='')
    elif z[0] == 0:
        print(z[1], "i", sep='' , end='')
    else:
        if z[1] > 0:
            signo = " + "
        elif z[1] < 0:
            signo = " - "
        print (z[0] , signo , np.abs(z[1]), "i", sep='', end='')
    return

##################################
# Conjugado de un número complejo
##################################
def conjugado(z):
    """
    Devuelve la lista que representa el conjugado de un número complejo
    """
    w = [z[0], -z[1]]
    return w

################################
# Suma de dos números complejos
################################
def suma(z1, z2):
    """
    Devuelve una lista que representa la suma de dos números complejos
    """
    w = [z1[0] + z2[0], z1[1] + z2[1]]
    return w

#################################
# Resta de dos números complejos
#################################
def resta(z1, z2):
    """
    Devuelve una lista que representa la resta de dos números complejos
    """
    w = [z1[0] - z2[0], z1[1] - z2[1]]
    return w

####################################
# Producto de dos números complejos
####################################
def producto(z1, z2):
    """
    Devuelve una lista que representa el producto de dos números complejos
    """
    w = [z1[0]*z2[0] - z1[1]*z2[1], z1[0]*z2[1] + z1[1]*z2[0]]
    return w

###############################
# Módulo de un número complejo
###############################
def modulo(z):
    """
    Devuelve un número igual al módulo de un número complejo
    """
    r = np.sqrt(producto(z, conjugado(z)))
    return r[0]

####################################
# División de dos números complejos
####################################
def division(z1, z2):
    """
    Devuelve una lista que representa la división entre dos números complejos
    """
    if z2[0] == 0 and z2[1] == 0:
        print("Error. División entre 0.")
        return
    w = (1/modulo(z2)**2)*producto(z1, conjugado(z2))
    return w

###########################################################
# Imprimir un número complejo en forma polar (exponencial)
###########################################################
def imprimir_polar(z):
    """
    Imprime un número complejo en la forma rho*e^{i*theta}
    """
    signo = ""
    if z[0] == 0:
        print(z[0])
    print (z[0],"*e^(i*", z[1] ,")", sep='')
    return

####################################################################################
# Imprimir un número complejo en forma polar (exponencial) Unidad angular de grados
####################################################################################
def imprimir_polar_grados(z):
    """
    Imprime un número complejo en la forma rho*e^{i*theta}. Ángulo en grados.
    """
    signo = ""
    if z[0] == 0:
        print(z[0])
    angulo = z[1]*180/np.pi
    print (z[0],"*e^(i*", angulo ,"°)", sep='')
    return

#################################################################
# Convertir un número complejo de forma cartesiana a forma polar
#################################################################
def Car_a_Pol(z):
    """
    Convierte un número complejo de forma cartesiana [a, b] a forma polar [rho, theta]
    """
    Rho = modulo(z)
    Theta = np.arctan2(z[1],z[0])
    p = [Rho, Theta]
    return p

#################################################################
# Convertir un número complejo de forma polar a forma cartesiana
#################################################################
def Pol_a_Car(p):
    nr = p[0]*np.cos(p[1])
    ni = p[0]*np.sin(p[1])
    z = [nr, ni]
    return z
