#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

def hex_to_bin(hex_data:str) -> str:
    scale = 16
    bit_length = 4*(len(hex_data) - 2)
    bin_data = bin(int(hex_data, scale))[2:].zfill(bit_length)
    return bin_data


def bin_to_hex(bin_data:str) -> str:
    scale = 2
    length = len(bin_data) // 4
    hex_data = "0x" + hex(int(bin_data, scale))[2:].zfill(length)
    return hex_data


def write(addr, data) -> None:

    set_address(hex_to_bin(addr))
    set_data(hex_to_bin(data))
    
    GPIO.output(WE, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(WE, GPIO.HIGH)


    
def set_address(eeprom_address:str) -> None:
    for index, bit in enumerate(eeprom_address):
        GPIO.output(address_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)

def set_data(eeprom_data:str) -> None:
    for index, bit in enumerate(eeprom_data):
        GPIO.output(data_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)


if __name__ == "__main__":

    address_pins = [14,15,25,8,7,16,20,21]
    data_pins = [17,27,22,10,9,11,13,26]

    WE = 19
    OE = 12

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pi in address_pins:
        GPIO.setup(pi, GPIO.OUT)

    for pi_ in data_pins:
        GPIO.setup(pi_, GPIO.OUT)

    for pins in [WE,OE]:
        GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)

    GPIO.output(OE, GPIO.HIGH)

    write("0x12", "0x77")

    GPIO.cleanup()

