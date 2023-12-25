#!/usr/bin/python3

import time
import RPi.GPIO as GPIO


#$ sudo python3 output_display_programmer.py

def hex_to_bin(hex_data:str) -> str:
    scale = 16
    bit_length = 4*(len(hex_data) - 2)
    bin_data = bin(int(hex_data, scale))[2:].zfill(bit_length)
    return bin_data


def write(addr:str, data:str) -> None:

    set_address(addr)
    set_data(hex_to_bin(data))
    time.sleep(0.20)

    GPIO.output(WE, GPIO.LOW)
    time.sleep(0.20)
    GPIO.output(WE, GPIO.HIGH)



def set_address(eeprom_address:str) -> None:
    for index, bit in enumerate(eeprom_address):
        GPIO.output(address_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)



def set_data(eeprom_data:str) -> None:
    for index, bit in enumerate(eeprom_data):
        GPIO.output(data_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)



def write_positive_integers() -> None:

    for num in range(0, 256):
        print(num)
        ones_place = num % 10
        tens_place = (num // 10) % 10
        hunderds_place = (num // 100) % 10

        bin_num = bin(num)[2:].zfill(8)
        data_array = [digit_hex_codes[ones_place], digit_hex_codes[tens_place], digit_hex_codes[hunderds_place], pos]

        for digits_place in range(0, 4):
            digits_place_bits = bin(digits_place)[2:].zfill(2)
            addr = digits_place_bits + bin_num
            data = data_array[digits_place]
            write(addr, data)
            print(addr, data)

        print("\n")

if __name__ == "__main__":

    address_pins = [5, 6, 14, 15, 25, 8, 7, 16, 20, 21]
    data_pins = [17, 27, 22, 10, 9, 11, 13, 26]

    WE = 19 #Write Enable
    OE = 12 #Output Enable

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #Setting up address, data, OE & WE pins
    for pi in address_pins:
        GPIO.setup(pi, GPIO.OUT)

    for pi_ in data_pins:
        GPIO.setup(pi_, GPIO.OUT)

    for pins in [WE,OE]:
        GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)

    GPIO.output(OE, GPIO.HIGH)

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

    #Digit hex codes array
    digit_hex_codes = [zero, one, two, three, four, five, six, seven, eight, nine, pos]

    write_positive_integers()

    GPIO.cleanup()
