The code & schematic are MIT licensed.

The circuit and code are according to SAP-1.

| INS       | OPCODE |
|-----------|--------|
| ***NOP*** | `0x0` |
| ***LDA*** | `0x1` |
| ***ADD*** | `0x2` |
| ***SUB*** | `0x3` |
| ***STA*** | `0x4` |
| ***LDI*** | `0x5` |
| ***JMP*** | `0x6` |
| ***JC***  | `0x7` |
| ***JZ***  | `0x8` |
| --        | `0x9` |
| --        | `0xa` |
| --        | `0xb` |
| --        | `0xc` |
| --        | `0xd` |
| ***OUT*** | `0xe` |
| ***HLT*** | `0xf` |

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
