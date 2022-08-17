x = float(input("Ingrese la longitud del campo (ft): "))
y = float(input("Ingrese el ancho del campo (ft): "))

conver_m_acr = (x*y)*(1/43560)

print("El área del campo es de: {value}".format(value = conver_m_acr))