def file_range(name:str,rango:list):
    with open(name,"w") as f1:
         for i in range(rango[0],rango[1]+1):
             f1.write(str(i) + "\n")


def filePair(file1:str,file2:str):
    with open(file1,"r") as f1:
        with open(file2,"w") as pair_f1:
            f1_lines = f1.readlines()
            f1_lines.reverse()
            for line in f1_lines:
                if int(line)%2 == 0:
                    pair_f1.write(line)

 
            
    
def run():
    file_range("file_1.txt",[0,100])
    file_range("file_2.txt",[50,200])
    filePair("file_1.txt","file_1pair.txt")
    filePair("file_2.txt","file_2pair.txt")


if __name__ == "__main__":
    run()