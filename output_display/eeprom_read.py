#!/usr/bin/python3

import time
import logging
import argparse
import RPi.GPIO as GPIO

#$ sudo python3 eeprom_read.py --addr="<10-BIT-BIN-ADDR>"

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


def read_data(address:str) -> str:

    GPIO.output(OE, GPIO.LOW)

    set_address(address)

    time.sleep(1)

    byte_str = ""

    for pin in data_pins:
      byte_str += "1" if GPIO.input(pin) == 1 else "0"

    hex_str = bin_to_hex(byte_str)

    GPIO.output(OE, GPIO.HIGH)

    return hex_str


def set_address(eeprom_address:str) -> None:
    for index, bit in enumerate(eeprom_address):
        GPIO.output(address_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)


if __name__ == "__main__":

    #Setting logging configuration
    logging.basicConfig(level=logging.NOTSET)

    #Parsing args
    parser = argparse.ArgumentParser()
    parser.add_argument("--addr", required=True, type=str, help="10 bit binary address")
    args = parser.parse_args()
    address = args.addr

    address_pins = [5, 6, 14, 15, 25, 8, 7, 16, 20, 21]
    data_pins = [17, 27, 22, 10, 9, 11, 13, 26]

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #Setting up address, data, WE & OE pins
    for pi in address_pins:
        GPIO.setup(pi, GPIO.OUT)

    for pi_ in data_pins:
        GPIO.setup(pi_, GPIO.IN, GPIO.PUD_DOWN)

    WE = 19 #Write Enable
    OE = 12 #Output Enable

    for pins in [WE, OE]:
        GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)

    GPIO.output(WE, GPIO.HIGH)

    logging.info(read_data(address))

    GPIO.cleanup()
