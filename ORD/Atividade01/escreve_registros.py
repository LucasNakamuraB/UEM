arq_name: str = input("insira o nome do arquivo:")
out_file = open(arq_name + '.txt', 'wb')

fields: list[str] = ['SOBRENOME', 'NOME','ENDEREÇO', 'CIDADE', 'ESTADO', 'CEP']

def main() -> None:
    read_inputs()

def read_inputs():
    i: int = 0
    field_group: str = ''
    field: str = ''
    fg_size: int
    buffer: bytes
    run: bool = True
    while run:
        field = input("insira "+ fields[i]+ ":")
        field_group = field_group + field + '|'
        fg_size = len(field_group).to_bytes(2, byteorder="little")
        i = (i + 1)%len(fields)

main()