import os

reg_size = 64
header = 4
fields: list[str] = ["ID", "SOBRENOME", "NOME", "CASTELO", "CIDADE", "REGIÃO"]
filename = input("Insira o nome do arquivo: ")
file = open(filename, "rb+")
max_reg = int.from_bytes(file.read(4), "little")
print(str(max_reg))


def main():
    run = True
    while run:
        print(max_reg)
        print("-- INSIRA O NUMERO DA OPÇÃO -- \n")
        print("1. Adicionar novo registro")
        print("2. Buscar um registro por RRN para alteração")
        print("3. Terminar programa\n")
        command = input("Opção:")

        match command:
            case "1":
                add_registry(file, -1)
            case "2":
                rrn = (int(input("insira o RRN: ")))
                search_registry(file, rrn)
            case "3":
                run = False

def print_registry(file):
    registry = file.read(reg_size).decode().split('|')
    registry.pop()
    i = 1
    for field in registry:
        if field:
            print("Campo #"+str(i)+": "+field)
        i+=1

def add_registry(out_file, offset):
    field_group = ''
    if offset == -1:
        out_file.seek(0, os.SEEK_SET)
        #max_reg = int.from_bytes(out_file.read(4), "little")
        print(str(max_reg))
        max_reg += 1
        out_file.seek(0,os.SEEK_SET)
        out_file.write(max_reg.to_bytes(4, "little"))
        out_file.seek(0, os.SEEK_END)

    else:
        out_file.seek(offset,os.SEEK_SET)
    for field in fields:
        new_field = input("insira "+ field+ ":")
        field_group = field_group + str(new_field) + '|'
    field_size = len(field_group.encode('utf-8'))
    out_file.write(field_group.encode('utf-8'))
    zero = 0
    out_file.write(zero.to_bytes(reg_size-field_size,"little"))

def search_registry(file, rrn):
    if rrn <= max_reg:
        offset = (reg_size * (rrn - 1)) + header
        file.seek(offset, os.SEEK_SET)
        print_registry(file)
        file.seek(offset, os.SEEK_SET)
    else:
        print("RRN invalido")
        return

    resp = input("gostaria de Modificar? y/n")
    if resp == 'y':
        add_registry(file, offset)


if __name__ == "__main__":
    main()