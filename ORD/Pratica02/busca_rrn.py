import os

reg_size = 64
header = 4

def main():
    file = open("pessoasGOTfixo.dat", "rb")
    max_reg = int.from_bytes(file.read(4), "little")
    print(max_reg)
    rrn = int(input("Insira RRN a ser buscado: "))
    
    if rrn <= max_reg:
        offset = (reg_size * (rrn - 1)) + header
        file.seek(offset, os.SEEK_SET)
        print_registry(file)
    else:
        print("RRN invalido")

def print_registry(file):
    registry = file.read(reg_size).decode().split('|')
    registry.pop()
    i = 1
    for field in registry:
        if field:
            print("Campo #"+str(i)+": "+field)
        i+=1

if __name__ == "__main__":
    main()