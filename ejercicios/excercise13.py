class myCat:
    def __init__(self):
        self.catHappy = True
        self.catSad = not self.catHappy
        self.catSleep = False
        self.catPlay  = not self.catSleep
    
    def cathappy(self):
        
        self.catHappy = True
        self.catSad = False
        
        print(" /\     /\ ")
        print("{  `---'  }")
        print("{  O   O  }")
        print("~~>  V  <~~")
        print(" \  \|/  /")
        print("  `-----'____")
        print("  /     \    \_")
        print(" {       }\  )_\_ _")
        print(" |  \_/  |/ /  \_\_/ )")
        print("  \__/  /(_/     \__/")
        print("    (__/")
        
    def catsad(self):
        
        self.catSad = True
        self.catHappy = False
        
        print("    /\_____/\ ")
        print("   /  o   o  \ ")
        print("  ( ==  ^  == )")
        print("   )         (")
        print("  (           )")
        print(" ( (  )   (  ) )")
        print("(__(__)___(__)__)")

    def catsleep(self):
        
        self.catSleep = True
        self.catPlay = False
        
        print("      |\      _,,,---,,_")
        print("ZZZzz /,`.-'`'    -.  ;-;;,_")
        print("     |,4-  ) )-,_. ,\ (  `'-'")
        print("    '---''(_/--'  `-'\_)")
    
    def catplay(self):
        
        self.catSleep = False
        self.catPlay = True
        
        print("    /\_/\           ___")
        print("   = o_o =_______    \ \ ")
        print("    __v      __(  \.__) )")
        print("(@)<_____>__(_____)____/")


gato = myCat()
message = "Ingrese acción del michi: \n 1.cat happy\n 2.cat sad\n 3.cat sleep\n 4.cat play\n 0.salir\n"
while True:
    
    command = int(input(message))
    print("\033[2J\033[H")
    
    if command == 0:
        break
    elif command == 1:
        gato.cathappy()
    elif command == 2:
        gato.catsad()
    elif command == 3:
        gato.catsleep()
    elif command == 4:
        gato.catplay()
    else:
        print("Opcion incorrecta")
    