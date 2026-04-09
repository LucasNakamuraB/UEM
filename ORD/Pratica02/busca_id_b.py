import os

reg_size = 64
header = 4

def main():
    file = open("pessoasGOTfixo.dat", "rb")
    max_reg = int.from_bytes(file.read(4), "little")
    print(max_reg)
    id = int(input("insira o ID a ser buscado:"))
    i = 0
    pos = (i+ max_reg) // 2
    found = False
    while not found:
        pos = (i+ max_reg) // 2
        offset = (reg_size * (pos -1)) + header
        file.seek(offset, os.SEEK_SET)
        registry = file.read(reg_size).decode().split('|')
        if int(registry[0]) == id:
            found = True
        elif int(registry[0]) < id:
            i = pos + 1
        elif int(registry[0]) > id:
            max_reg = pos -1 

            
    
    if found:
        i = 1
        registry.pop()
        for field in registry:
            if field:
                print("Campo #"+str(i)+": "+field)
            i+=1
        
if __name__ == "__main__":
    main()