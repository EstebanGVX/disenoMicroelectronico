#Determinar tipo de triángulo (Equilatero,isósceles,escaleno)
#Triángulo equilatero -> Tiene sus tres lados iguales.
#Triángulo isósceles  -> Tiene dos de sus lados iguales.
#Triángulo escaleno   -> Tiene sus tres lados diferentes.

print("Ingrese tres ángulos en grados:")

try:
    x = [float(input("Ingrese ángulo: ")) for i in range(3)]
    
    if sum(x) == 180:
        if x.count(60) == 3:
            print("\n---TRIÁNGULO EQUILATERO---\n")
            print("            *a*")
            print("           *a a* ")
            print("          *a a a* ")
            print("         *a a a a* ")
            print("        *a a a a a* ")
        elif x.count(x[1]) == 1:
            print("\n---TRIÁNGULO ESCALENO---\n")
            print("      *a*")
            print("       *a a a*")
            print("        *a a a a*")
            print("         *a a a a a* ")
            print("          *a a a a a a* ")
            print("           *a a a a a a a* ")
            print("            *a a a a a a a a* ")
        else:
            print("\n---TRIÁNGULO ISÓSCELES---\n")
            print("            *a*")
            print("           *a a*")
            print("         *a a a a*")
            print("       *a a a a a a*")
            print("     *a a a a a a a a*")
            
except:
    print("Error al ingresar el núnero.")
        
