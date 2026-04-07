games = open("games.txt", 'r')
out_file = open("games.bin", 'wb')

def main() -> None:
    line = games.readline()[:-2]
    while line:
        bin_line = line.encode('utf-8')
        line_size = len(bin_line).to_bytes(2, "little")
        out_file.write(line_size)
        out_file.write(bin_line)
        line = games.readline()[:-2]
        

    

if __name__ == "__main__":
    main()