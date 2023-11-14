#!/usr/bin/python3

import json
import time
import argparse
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


#def write() -> None:

def read_data(address:str) -> str:
    eeprom_addr = hex_to_bin(address)
    set_address(eeprom_addr)
    byte_str = ""

    for pin in data_pins:
      byte_str += "1" if GPIO.input(pin) == "1" else 0

    hex_str = bin_to_hex(byte_str)
    return hex_str



def set_address(eeprom_address:str) -> None:
    for index, bit in enumerate(eeprom_address):
        GPIO.output(address_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)

def set_data(eeprom_data:str) -> None:
    for index, bit in enumerate(eeprom_data):
        GPIO.output(data_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)



def write_eeprom_data_file(file_path:str) -> None:
    data_file = open(file_path)

    ee_data = json.load(data_file)["eeprom_data"]

    for ins in ee_data:
        ins_data = ee_data[ins]

        for i in ins_data:
            eeprom_add = hex_to_bin(i)
            eeprom_data = hex_to_bin(ins_data[i])
            print(ins, eeprom_add, eeprom_data)
            set_address(eeprom_add)
            set_data(eeprom_data)
            #write()
            time.sleep(2)

        print("-"*21)

    #data_file.close()




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--eefile", required=True, type=str, help="EEPROM content file path")
    args = parser.parse_args()
    filepath = args.eefile

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #GPIO.cleanup()

    address_pins = [14,15,25,8,7,16,20,21]
    data_pins = [17,27,22,10,9,11,13,26]
    for pi in address_pins:
        GPIO.setup(pi, GPIO.OUT)

    for pi_ in data_pins:
        GPIO.setup(pi_, GPIO.OUT)

    #address = "0xd0"
    #ad = hex_to_bin(address)
    #set_address(ad)

    #time.sleep(4)

    #GPIO.cleanup()


    #data_oins = [1,2,3,4,5,6,7,8]
    #print(hex_to_bin("0xb3"))
    #print(bin_to_hex("01010111"))
    write_eeprom_data_file(filepath)

    GPIO.cleanup()
