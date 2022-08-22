import numpy as np

def createMatrix():
    x = int(input("Ingrese el número de filas: "))
    y = int(input("Ingrese el numero de columnas: "))
    arrayAux = np.array([float(input("Ingrese un elemento: ")) for i in range(x*y)])
    arrayd2 = arrayAux.reshape(x,y)
    return arrayd2

def sumMatrix(matrix_1,matrix_2):
    if matrix_1.shape == matrix_2.shape:
        print("La suma de la primara matriz mas la matriz dos es:\n")
        print(matrix_1 + matrix_2)
        print("\n")
    else:
        print("La suma no es posible las dimensiones de las matrices son diferentes.\n")

def prodMatrix(matrix_1,matrix_2):
    if matrix_1.shape[1] == matrix_2.shape[0]:
        print("\nEl producto de la primara matriz por la matriz dos es:\n")
        print(np.dot(matrix_1,matrix_2))
        print("\n")
    else:
        print("\nLa multiplicación entre las dos matrices no es posible.\n")

def detMatrix(matrix,id):
    if matrix.shape[0] == matrix.shape[1]:
        print(f"\nEl determinante de la {id}  es: {np.linalg.det(matrix)}")
    else:
        print("\nLa matriz no es cuadrada.\n")

def invMatrix(matrix,id):
    if matrix.shape[0] == matrix.shape[1] and np.linalg.det(matrix) != 0 :
        inv = np.linalg.inv(matrix)
        print(f"\n La matriz inversa de la {id} es:")
        print(inv)
    else:
        print("\nLa matriz no tiene inversa.\n")


def run():
    print("\nFirst matrix\n")
    matrix1 = createMatrix()
    print("\nSecond matrix\n")
    matrix2 = createMatrix()
    print(matrix1)
    print("\n")
    print(matrix2)
    print("\n")
    sumMatrix(matrix1,matrix2)
    prodMatrix(matrix1,matrix2)
    detMatrix(matrix1,"matrix1")
    detMatrix(matrix2,"matrix2")
    invMatrix(matrix1,"matrix1")
    invMatrix(matrix2,"matrix2")
    
if __name__ == "__main__":
    run()