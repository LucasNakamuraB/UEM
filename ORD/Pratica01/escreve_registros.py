arq_name: str = input("insira o nome do arquivo:")
out_file = open(arq_name + '.bin', 'wb')

fields: list[str] = ['SOBRENOME', 'NOME','ENDEREÇO', 'CIDADE', 'ESTADO', 'CEP','fodase']

def main() -> None:
    read_inputs()

def read_inputs():
    i: int = 0
    field_group: str = ''
    field: str = ''
    fg_size: int
    run: bool = True
    while run:
        field = input("insira "+ fields[i]+ ":")
        if field == '' and i == 0:
            return
        field_group = field_group + str(field) + '|'
        if i == len(fields) - 1:
            fg_size = len(field_group.encode("utf-8"))
            out_file.write(fg_size.to_bytes(2, byteorder="little"))
            out_file.write(field_group.encode('utf-8'))
            field_group = ''
        i = (i + 1)%len(fields)


main()