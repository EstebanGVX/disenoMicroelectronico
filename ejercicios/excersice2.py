def converC_F(gradeC):
    return (9/5)*gradeC + 32

def converF_C(gradeF):
    return (5/9)*(gradeF -32)

def run():
    x = float(input("Ingrese grados a convertir: "))
    s = input("Ingrese conversion \"C\" o \"F\": ")
    
    if s == "C":
        print(converF_C(x))
    elif s == "F":
        print(converC_F(x))
    else:
        print("conver not found")


run()