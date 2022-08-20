x = []
try:
    data = int(input("Ingrese un número entero: "))
    
    while data :
        x.append(data)
        data = int(input("Ingrese un número entero: "))
    
    x.sort()
    print("\nRESULTADO:\n")
    print(x)
except:
    print("Error al ingresar el número")