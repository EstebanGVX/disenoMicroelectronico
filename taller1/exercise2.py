try:
    x = [float(input("Ingrese un número: ")) for i in range(4)]
    
    print("\nLa suma de los número ingresados es:\n")
    print(f"({x[0]}) + ({x[1]}) + ({x[2]}) + ({x[3]}) = {sum(x)}")
except:
    print("Error al ingresar el número.")