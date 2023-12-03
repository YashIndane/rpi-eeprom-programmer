The code & schematic are MIT licensed.

The circuit and code are according to SAP-1.

| INS       | OPCODE |
|-----------|--------|
| ***NOP*** | `0x00` |
| ***LDA*** | `0x01` |
| ***ADD*** | `0x02` |
| ***SUB*** | `0x03` |
| ***STA*** | `0x04` |
| ***LDI*** | `0x05` |
| ***JMP*** | `0x06` |
| ***JC***  | `0x07` |
| ***JZ***  | `0x08` |
| --        | `0x09` |
| --        | `0x0a` |
| --        | `0x0b` |
| --        | `0x0c` |
| --        | `0x0d` |
| ***OUT*** | `0x0e` |
| ***HLT*** | `0x0f` |

|  ***LEFT EEPROM BITS***  |  ***RIGHT EEPROM BITS*** |
---------------------------|--------------------------|
`HLT MI RI RO IO II AI AO` | `EO SU BI OI CE CO J FI` |

## Schematic

![EEPROM-cd - Copy](https://github.com/YashIndane/rpi-eeprom-programmer/assets/53041219/49979c60-761a-4665-b10e-a54e12fb7a37)

## Understanding the JSON file

The JSON file contents the `address:data` mappings.

![mic](https://github.com/YashIndane/rpi-eeprom-programmer/assets/53041219/b147e6c2-5faa-416f-9d52-aeecd748a9b1)

ADDRESS BITS SPLIT

|   2 bits  |  4 bits   | 4 bits  |
|-----------|-----------|---------|
|   flag    |   step    |  opcode |

### Cleaning the EEPROM

```
$ sudo python3 eeprom_cleaner.py
```

### Bulk reading

```
$ sudo python3 eeprom_bulk_read.py
```

### Bulk writing

```
$ sudo python3 eeprom_bulk_write.py --eefile="<JSON-FILE>"
```
