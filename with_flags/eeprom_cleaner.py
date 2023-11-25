#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

#$ sudo python3 eeprom_bulk_read.py

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


def write_data(addr:str, data:str) -> None:

    set_address(hex_to_bin(addr)[2:])
    set_data(hex_to_bin(data))
    time.sleep(0.20)
    
    GPIO.output(WE, GPIO.LOW)
    time.sleep(0.20)
    GPIO.output(WE, GPIO.HIGH)

    print(addr, data)


def set_address(eeprom_address:str) -> None:
    for index, bit in enumerate(eeprom_address):
        GPIO.output(address_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)


def set_data(eeprom_data:str) -> None:
    for index, bit in enumerate(eeprom_data):
        GPIO.output(data_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)

def clean() -> None:

    for flag_hex_bit, flag_bits in enumerate(["00", "01", "10", "11"]):

      for step in range(16):
          step_hex = hex(step)

          for opcode in range(16):
              opcode_hex = hex(opcode)
              addr = "0x" + str(flag_hex_bit) + step_hex[2:] + opcode_hex[2:]
              write_data(addr, "0x00")


      print("\n")


if __name__ == "__main__":
    
    #GPIO5 - CF (A8), GPIO6 - ZF (A9)
    address_pins = [5, 6, 14, 15, 25, 8, 7, 16, 20, 21]
    data_pins = [17, 27, 22, 10, 9, 11, 13, 26]

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #Setting up address, data, WE & OE pins
    for pi in address_pins:
        GPIO.setup(pi, GPIO.OUT)

    for pi_ in data_pins:
        GPIO.setup(pi_, GPIO.OUT)

    WE = 19 #Write Enable
    OE = 12 #Output Enable

    for pins in [WE, OE]:
        GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)

    GPIO.output(OE, GPIO.HIGH)

    clean()

    GPIO.cleanup()
