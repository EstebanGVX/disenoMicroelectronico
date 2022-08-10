def normalizar(lista:list, a, b)->list:
    x_max = max(lista)
    x_min = min(lista)
    if (x_min == x_max):
        return lista
    res = []
    for i in lista:
        data = a+(((i-x_min)*(b-a))/(x_max-x_min))
        res.append(round(data,4))
    
    return res


def createList():
    x = []
    for i in range(21):
        x.append(i*i+i+1)
    return x
    


#x = [ k for k in range(1,21)]
x = createList()

print(normalizar(x,-1,1))
print("\n")
print(normalizar(x,1,10))
print("\n")
print(normalizar(x,0.5,1))