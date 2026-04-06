arq_name:str = input("Insira o nome do arquivo que deseja ler:")
in_file = open(arq_name, 'rb')

def main() -> None:
    read_fields(in_file)

def read_fields(file):
    n_reg: int = 0
    reg_size: int = int.from_bytes(file.read(2), 'little')
    while reg_size:
        n_reg += 1
        registry = file.read(reg_size).decode().split('|')
        print("Registro "+ str(n_reg)+ " (tam="+str(reg_size)+')')
        i = 1
        for field in registry:
            if field:
                print("Campo #"+str(i)+": "+field)
            i+=1
        print("\n")
        reg_size = int.from_bytes(file.read(2), 'little')
        
main()