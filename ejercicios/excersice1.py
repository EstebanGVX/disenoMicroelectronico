def fun_01(n):
    return n**n

def fun_02(n):
    return n*n + 1000*n

def fun_03(n):
    if n >= 10:
        return 10
    elif n > 1 and n < 5:
        return (n**n) + n + 1
    else:
        return 2*n -1

def run():
    x = float(input("Ingrese un numero decimal: "))
    n = int(input("Ingrese la opción: "))
    
    if n == 1:
        print(fun_01(x))
    elif n == 2:
        print(fun_02(x))
    elif n == 3:
        print(fun_03(x))
    else:
        print("Operation not found")

if __name__ == '__main__':
    run()