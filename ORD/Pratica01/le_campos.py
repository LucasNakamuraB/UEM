file_name = input('insira arquivo que deseja ler: ')
in_file = open(file_name, 'r')

def main() -> None:
    read_file(in_file)

def read_file(file):
    field = ''
    char = '_'
    i = 0
    while char != '':
        char = file.read(1)
        if char == '|':
            print("Campo #"+ str(i)+": "+ field)
            field = ''
            i += 1
        else:
            field = field + char



main()