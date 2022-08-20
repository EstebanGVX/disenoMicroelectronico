try:
    data = input("Ingrese una palabra: ")
    
    while data.upper() != "FIN" :
        data = input("")
except:
    print("Error al ingresar la palabra")
    