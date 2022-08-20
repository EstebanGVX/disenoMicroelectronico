try:
    x = [float(input("Ingrese un número: ")) for i in range(0,3)]

    x.sort()
    print(f"\nEl valor medio es: {x[1]}")
except:
    print("Error al digitar el número. ")
    