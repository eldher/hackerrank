def print_formatted(number):
    width = len(str(bin(number)))-2

    for i in range(1,number+1):

        dec1 = str(i)
        oct1 = oct(i).lstrip("0o").rstrip("L")
        hex1 = hex(i).lstrip("0x").rstrip("L").upper()
        bin1 = bin(i).lstrip("0b").rstrip("L")
        
        print(dec1.rjust(width)+ " " + oct1.rjust(width)+ " " + hex1.rjust(width)+ " "+ bin1.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
