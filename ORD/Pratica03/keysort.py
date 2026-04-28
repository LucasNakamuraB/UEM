from sys import argv
import os

def main() -> None:
    in_file = open(argv[1], 'rb')
    out_file = open(argv[2], 'wb')
    n_reg = int.from_bytes(in_file.read(4), "little")
    index = readall(in_file, n_reg)
    index.sort()
    out_file.write(n_reg.to_bytes(4, "little"))
    for i in index:
        in_file.seek(i[1], os.SEEK_SET)
        out_file.write(read_registry(in_file))


def readall(file, n_reg) -> list[tuple]:
    lst = []
    for i in range(n_reg):
        lst.append(make_index(file))
        print(lst)
    return lst
    
def make_index(file):
    offset = file.seek(0, os.SEEK_CUR)
    size = int.from_bytes(file.read(2), 'little')
    reg = file.read(size).decode().split('|')
    id = int(reg[0])
    tup = (id, offset)
    return tup

def read_registry(file):
    b_size = file.read(2)
    size = int.from_bytes(b_size, "little")
    buffer = file.read(size)
    return b_size + buffer
    


main()