with open("matrix","w") as f:
    for i in range(1,11):
        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}\n")

        