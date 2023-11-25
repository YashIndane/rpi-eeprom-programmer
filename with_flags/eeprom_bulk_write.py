#!/usr/bin/python3

import time
import argparse
import json
import RPi.GPIO as GPIO

#$ sudo python3 eeprom_bulk_write.py --eefile="eefile.json"

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


def write(addr:str, data:str) -> None:

    #We dont need those first 2 bits
    set_address(hex_to_bin(addr)[2:])

    set_data(hex_to_bin(data))
    time.sleep(0.20)
    
    GPIO.output(WE, GPIO.LOW)
    time.sleep(0.20)
    GPIO.output(WE, GPIO.HIGH)

    #print("Write Successful!")


def set_address(eeprom_address:str) -> None:
    for index, bit in enumerate(eeprom_address):
        GPIO.output(address_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)


def set_data(eeprom_data:str) -> None:
    for index, bit in enumerate(eeprom_data):
        GPIO.output(data_pins[index], GPIO.HIGH if bit == "1" else GPIO.LOW)


def bulk_write(file_path:str) -> None:

    data_file = open(file_path)
    ee_data = json.load(data_file)["eeprom_data"]

    for ins in ee_data:
        ins_data = ee_data[ins]

        for i in ins_data:
            eeprom_add = i
            eeprom_data = ins_data[i]
            print(ins, eeprom_add, eeprom_data)

            
            write(eeprom_add, eeprom_data)

        print("-"*21)

    data_file.close()



if __name__ == "__main__":

    #Parsing args
    parser = argparse.ArgumentParser()
    parser.add_argument("--eefile", required=True, type=str, help="EEPROM ins-controlword JSON file")
    args = parser.parse_args()
    filepath = args.eefile

    #GPIO5 - CF (A8), GPIO6 - ZF (A9)
    address_pins = [5, 6, 14, 15, 25, 8, 7, 16, 20, 21]
    data_pins = [17, 27, 22, 10, 9, 11, 13, 26]

    WE = 19  #Write Enable
    OE = 12  #Output Enable

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

    bulk_write(filepath)

    GPIO.cleanup()
