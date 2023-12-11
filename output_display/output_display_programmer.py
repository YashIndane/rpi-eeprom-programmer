def hex_to_bin(hex:str) -> str:
    scale = 16
    bit_length = 4*(len(hex_data) - 2)
    bin_data = bin(int(hex_data, scale))[2:].zfill(bit_length)
    return bin_data


#def write(addr, data) -> None:


def write_positive_integers() -> None:

    sign_bit = "0"
    for num in range(0, 256):
        print(num)
        ones_place = num % 10
        tens_place = (num // 10) % 10
        hunderds_place = (num // 100) % 10

        bin_num = bin(num)[2:].zfill(8)
        data_array = [digit_hex_codes[ones_place], digit_hex_codes[tens_place], digit_hex_codes[hunderds_place], pos]

        for digits_place in range(0, 4):
            digits_place_bits = bin(digits_place)[2:].zfill(2)
            addr = sign_bit + " " + digits_place_bits + " " + bin_num
            data = data_array[digits_place]
            #write(addr, data)
            print(addr, data)

        print("\n")

if __name__ == "__main__":

    #Digit hex codes
    zero = "0xfc"
    one = "0x60"
    two = "0xda"
    three = "0xf2"
    four = "0x66"
    five = "0xb6"
    six = "0xbe"
    seven = "0xe0"
    eight = "0xfe"
    nine = "0xf6"
    pos = "0x00"
    neg = "0x02"

    #Digit hex codes array
    digit_hex_codes = [zero, one, two, three, four, five, six, seven, eight, nine, pos, neg]
    write_positive_integers()
