The code & schematic are MIT licensed.

![EEPROM-cd - Copy](https://github.com/YashIndane/rpi-eeprom-programmer/assets/53041219/d155f820-180a-4b5e-ad1f-bc2b9e4451ed)

Digit Codes -

| Decimal/sign |a|b|c|d|e|f|g|.|Hex|
|--------------|-|-|-|-|-|-|-|-|---|
|      0       |1|1|1|1|1|1|0|0|0xfc|
|      1       |0|1|1|0|0|0|0|0|0x60|
|      2       |1|1|0|1|1|0|1|0|0xda|
|      3       |1|1|1|1|0|0|1|0|0xf2|
|      4       |0|1|1|0|0|1|1|0|0x66|
|      5       |1|0|1|1|0|1|1|0|0xb6|
|      6       |1|0|1|1|1|1|1|0|0xbe|
|      7       |1|1|1|0|0|0|0|0|0xe0|
|      8       |1|1|1|1|1|1|1|0|0xfe|
|      9       |1|1|1|1|0|1|1|0|0xf6|
|      +       |0|0|0|0|0|0|0|0|0x00|
|      -       |0|0|0|0|0|0|1|0|0x02|


Example of displaying the number 158 using Multiplexed display -

| Sign-bit | Digit-selectors | Decimal | Binary | Display-word | Unit's place |
|----------|-----------------|---------|--------|--------------|--------------|
|     0    |        00       |   158   |10011110|     0xfe     |     ONES     |
|     0    |        01       |   158   |10011110|     0xb6     |     TENS     |
|     0    |        10       |   158   |10011110|     0x60     |   HUNDEREDS  |
|     0    |        11       |   158   |10011110|     0x00     |     SIGN     |
