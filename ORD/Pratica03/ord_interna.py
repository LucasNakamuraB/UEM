from sys import argv



def main() -> None:
    in_file = open(argv[1], 'rb')
    out_file = open(argv[2], 'wb')
    n_reg = int.from_bytes(in_file.read(4), "little")
    registries = readall(in_file, n_reg)
    registries.sort()
    out_file.write(n_reg.to_bytes(4, "little"))
    for r in registries:
        out_file.write(len(r[1]).to_bytes(2,"little"))
        out_file.write(r[1])

def readall(file, n_reg):
    lst = []
    for i in range(n_reg):
        size = int.from_bytes(file.read(2), "little")
        b_reg = file.read(size)
        id =int(b_reg.decode().split('|')[0])
        tup = (id, b_reg)
        lst.append(tup)
    return lst


main()