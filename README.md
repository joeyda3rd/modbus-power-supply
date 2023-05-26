# hanmatek-power-supply
A python script to control Hanmatek HM310T power supply on modbus protocol

Some previous work on the topic for a previous version  

http://www.roedan.com/controlling-a-cheap-usb-power-supply/  
https://bitbucket.org/roedan/powersupply/src/master/  
http://nightflyerfireworks.com/home/fun-with-cheap-programable-power-supplies

[Documentation provided by the OEM](OEM-docs/Modbus.pdf)

Registers from documentation
| Number | Function | Type | Decimal Places Capacity | Read/Write | Register Address |
| ------ | -------- | ---- | ----------------------- | ---------- | ---------------- |
| 0 | Output On/Off | Boolean | 0 | r,w | 0x0001 |
| 1 | Protect Status | Struct | 0 | r | 0x0002 |
| 2 | Specification | unsigned short | 0 | r | 0x0003 |
| 3 | Tail Classification | hexadecimal | 0 | r | 0x0004 |
| 4 | Decimal Point Values | hexadecimal | 0 | r | 0x0005 |
| 5 | Voltage Display Value | unsigned short | 2 | r | 0x0010 |
| 6 | Current Display Value | unsigned short | 3 | r | 0x0011 |
| 7 | Power Display Value | 2 integers? | 3 | r | 0x0012,0x0013 |
| 9 | Set Voltage | unsigned short | 2 | r,w | 0x0030 |
| 10 | Set Current | unsigned short | 3 | r,w | 0x0031 |
| 12 | Set OVP | unsigned short | 2 | r,w | 0x0020 |
| 13 | Set OCP | unsigned short | 2 | r,w | 0x0021 |
| 14 | Set OPP | unsigned short? | 2 | r,w | 0x0022,0x0023 |
| 15 | Set Comm Address | byte (1-250) | 0 |  r,w | 0x9999 |

**Notes**  
#2 See struct below from documentation.   
#3 no idea  
#4 when it's reading 0x0233 that equals voltage has 2 decimal places, current 3, power 3  
#7, #14 Not sure, it says "32 digit capacity", maybe 2 integers to make a 32 digit number (first register is first 16 digits, 2nd is last 16)
#14 type (range as it's calle in docs) says 0-65535 (unsigned short) but I question that since it's a combination of two registers like #7
#15 docs say the range is 1-250, not sure of the best type to use for that. 

```
// protection status bit

union _ST
{
  struct
  {
    uint8_t isOVP:1；//Over voltage protection 
    uint8_t isOCP:1；//Over current protection
    uint8_t isOPP:1；//Over power protection
    uint8_t isOTP:1；//Over tempreture protection
    uint8_t isSCP:1；//short-circuit protection
  }OP;
  uint8_t Dat;
｝
```
