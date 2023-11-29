The code & schematic are MIT licensed.

## Schematic

![EEPROM-cd](https://github.com/YashIndane/rpi-eeprom-programmer/assets/53041219/ac0aa24b-a778-4c38-bb5d-bf76adbc03c2)

## Usage

### Reading a byte

```
$ sudo python3 eeprom_read.py --addr="<HEX-ADDR>"
```

### Writing a byte

```
$ sudo python3 eeprom_write.py --addr="<HEX-ADDR>" --data="<HEX-DATA>"
```

### Bulk reading

```
$ sudo python3 eeprom_bulk_read.py
```

### Bulk writing from JSON file

```
$ sudo python3 eeprom_bulk_write.py --eefile="JSON-FILE"
```
