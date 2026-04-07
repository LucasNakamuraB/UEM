file = open("pessoasGOT.dat", 'rb')
id = input("Insira o ID a ser buscado: ")

def search_id(id):
    found = False
    reg_size = int.from_bytes(file.read(2), 'little')
    registry = []
    while reg_size and not found:
        registry = file.read(reg_size).decode().split('|')
        if registry[0] == id:
            found = True
        reg_size = int.from_bytes(file.read(2), 'little')
    
    if found:
        i = 1
        for field in registry:
            if field:
                print("Campo #"+str(i)+": "+field)
            i+=1
    else:
        print("Registro não encontrado")
        
search_id(id)