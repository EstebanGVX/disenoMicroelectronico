import math

try:
    a = float(input("Ingrese un numero a:"))
    b = float(input("Ingrese un numero b:")) 
    
    print(f"La suma de {int(a)} y {int(b)} es: {a+b}")
    print(f"La resta de {int(b)}-{int(a)}: {b-a}")
    print(f"El producto de {int(a)} y {int(b)} es: {a*b}")
    print(f"El cociente de {int(a)}/{int(b)} es: {a/b}")
    print(f"El logaritmo en base 10 de {int(a)} es: {math.log10(a)}")
    print(f"La potencia de {int(a)} elevado a la {int(b)} es: {math.pow(a,b)}")
    print(f"El resultado de euler potencia de {int(a)} es: {math.exp(a)}")
    print(f"La raíz {int(b)} de {int(a)} es: {a**(1/b)}")
except:
    print("Error el ingresar el número.")