file = open("pessoasGOT.dat", 'rb')
sobrenome = input("Insira o SOBRENOME a ser buscado: ")

def search_sobrenome(sb):
    found = False
    reg_size = int.from_bytes(file.read(2), 'little')
    registry = []
    while reg_size:
        registry = file.read(reg_size).decode().split('|')
        if registry[1] == sb:
            print_registry(registry)
            found = True
        reg_size = int.from_bytes(file.read(2), 'little')
    
    if found:
        pass
    else:
        print("Registro não encontrado")

def print_registry(reg: list):
    i = 1
    for field in reg:
        if field:
            print("Campo #"+str(i)+": "+field)
        i+=1
    print(' ')

search_sobrenome(sobrenome)