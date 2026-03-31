arq_name: str = input("insira o nome do arquivo:")
out_file = open(arq_name + '.txt', 'w')

fields: list[str] = ['SOBRENOME', 'NOME','ENDEREÇO', 'CIDADE', 'ESTADO', 'CEP']

def main() -> None:
    read_inputs()

def read_inputs():
    field: str = ''
    i = 0
    while not (field == '|' and i == 1):
        field = input("insira "+ fields[i]+ ":") + '|'
        if not (field == '|' and i == 0):
            out_file.write(field)
        i = (i + 1)%len(fields)
    out_file.close()

main()