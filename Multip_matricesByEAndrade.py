# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:18:23 2021

@author: Guillermo_Erick_Andrade_ EPN

"""

def llenar_matriz(matriz, fila, columna):
    for i in range (fila):
        matriz.append([])
        for j in range (columna):
                itera = True       
                while itera:
                    try:            
                        valor = float(input("Filas {}, Columnas {} : ".format(i+1, j+1)))
                        matriz[i].append(valor)
                        itera = False
                    except ValueError:
                        print("\nPor favor ingrese numeros :D")  

def multiplicar_matrices (m1, m2):
    
    if (len(m1[0]) == len(m2)): #evalua fila y columna
        
        m3 = []
        for i in range(len(m1)):
            m3.append([])

            for j in range(len(m2[0])):

                m3[i].append(0)
        for i in range(len(m1)):
            for j in range (len(m2[0])):
                for k in range (len(m1[0])):
                    m3 [i][j] += m1[i][k] * m2[k][j]
                   
        return m3
    else:
        return None

def impresion_matriz(mat):
    num = int(len(mat[0]) - 1)#
    for fila in mat:
        i = 1
        print("[", end=" ")
        for elemento in fila:
            print("{:8.2f}".format(elemento), end=" ") 
            if len(mat[0]) == 1:
                i = 0
            elif i <= num:
                    print(",", end=" ")
            i += 1
        print(" ]")

def impresion(a, b):
        print("==========================================")
        print("          Matriz[1] * Matriz[2]: ")
        print("==========================================")
        impresion_matriz(c)
        print("==========================================")
        impresion_matriz(d)
        print("==========================================")
        print("\nResultado:")
        matriz_z = multiplicar_matrices(a, b)
        if matriz_z == None:
            print("no se puede multiplicar la matriz")
        else: 
            impresion_matriz(matriz_z)

print("=====================================================")
print("|Bienvenido al Sistema de Multiplicación de Matrices|")
print("=====================================================\n")
print("              Ingresemos la matriz :D")
print("-----------------------------------------------------")
print("->Coincide filas[*] y columnas[*]<-")
print("\nMatriz [1]:")
itera = True
while itera:
    try:
        mat1_fila = int(input("Ingresa el número de filas en matriz [1]: "))
        if mat1_fila < 0:
            print("Por favor, ingrese numeros positivos! :D")
        else:
            itera = False
    except ValueError:
          print("\nPor favor ingrese numeros :D")   

itera = True
while itera:
    try:
        mat1_columna = int(input("Ingresa el número de columnas en matriz [*][1]: "))
        if mat1_columna < 0:
            print("Por favor, ingrese numeros positivos! :D")
        else:
            itera = False
    except ValueError:
          print("\nPor favor ingrese numeros :D")   

print("\nMatriz [2]:")
itera = True
while itera:
    try:
        mat2_fila = int(input("Ingresa el número de filas en matriz [*][2]: "))
        if mat2_fila < 0:
            print("Por favor, ingrese numeros positivos! :D")
        else:
            itera = False
    except ValueError:
          print("\nPor favor ingrese numeros :D")   

itera = True
while itera:
    try:
        mat2_columna = int(input("Ingresa el número de columnas en matriz [2]: "))
        if mat2_columna < 0:
            print("Por favor, ingrese numeros positivos! :D")
        else:
            itera = False
    except ValueError:
          print("\nPor favor ingrese numeros :D")  
c = []
d = []
 
print("\nCampos Matriz[1]:")
llenar_matriz(c, mat1_fila, mat1_columna)
print("\nCampos Matriz[2]:")
llenar_matriz(d, mat2_fila, mat2_columna)
        
print()
impresion(c, d)
print("Gracias por utilizar el programa :D")

    


 




