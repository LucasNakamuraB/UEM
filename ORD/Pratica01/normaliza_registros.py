arq_name:str = input("Insira o nome do arquivo que deseja ler:")
in_file = open(arq_name, 'rb')
errors: list[str]=[]

def main() -> None:
    read_fields(in_file)
    for error in errors:
        print(error)

def read_fields(file):
    n_reg: int = 0
    reg_size: int = int.from_bytes(file.read(2), 'little')
    while reg_size:
        n_reg += 1
        registry = file.read(reg_size).decode().split('|')
        print("Registro "+ str(n_reg)+ " (tam="+str(reg_size)+')')
        i = 0
        while registry[i]:
            print("Campo #"+str(i+1)+": "+registry[i])
            if i == 4 and len(registry[i]) != 2:
                errors.append("ERRO: Registro #" + str(n_reg)+": ESTADO não possui 2 caracteres")
            if i == 5 and not registry[i].isdigit():
                errors.append("ERRO: Registro #" + str(n_reg)+": CEP não possui apenas digitos")
            i+=1
        if i > 6:
            errors.append("ERRO: Registro #" + str(n_reg)+": Possui mais de 6 campos")
        print("\n")
        reg_size = int.from_bytes(file.read(2), 'little')
        
main()