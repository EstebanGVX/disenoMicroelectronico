x = input("Ingrese una letra vocal ó consonante: ")

if ((ord(x)>ord('A')) and (ord(x)<ord('Z'))) or ((ord(x)>ord('a')) and (ord(x)<ord('z'))):
    for i in ['a','e','i','o','u']:
        if x == i or x == i.upper():
            x = True
            break
    if x == True:
        print("La letra ingresada es una letra")
    else:
        print("La letra ingresada es una consonante")
else:
    print("El caracter ingresado no es valido")