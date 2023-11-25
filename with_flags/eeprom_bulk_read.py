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


def read_data(address:str) -> str:

    GPIO.output(OE, GPIO.LOW)
    
    #We dont need those first 2 bits
    eeprom_addr = hex_to_bin(address)[2:]
    set_address(eeprom_addr)

    time.sleep(0.20)

    byte_str = ""

    for pin in data_pins:
      byte_str += "1" if GPIO.input(pin) == 1 else "0"

    hex_str = bin_to_hex(byte_str)

    GPIO.output(OE, GPIO.HIGH)

    return hex_str


def set_address(eeprom_address:str) -> None:
    for index, bit in enumerate(eeprom_address):
        GPIO.output(address_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)


def bulk_reader() -> None:

    for flag_hex_bit, flag_bits in enumerate(["00", "01", "10", "11"]):
      print(f"CF={flag_bits[0]} ZF={flag_bits[1]}", flag_hex_bit)

      for step in range(16):
          step_string = ""
          step_hex = hex(step)

          for opcode in range(16):
              opcode_hex = hex(opcode)
              addr = "0x" + str(flag_hex_bit) + step_hex[2:] + opcode_hex[2:]
              controlword = read_data(addr)
              step_string += controlword + " "

          print(step_string)

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
        GPIO.setup(pi_, GPIO.IN, GPIO.PUD_DOWN)

    WE = 19 #Write Enable
    OE = 12 #Output Enable

    for pins in [WE, OE]:
        GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)

    GPIO.output(WE, GPIO.HIGH)

    bulk_reader()

    GPIO.cleanup()
