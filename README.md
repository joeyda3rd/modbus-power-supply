# Hanmatek Power Supply Python Library

This repository contains a Python library to interact with the Hanmatek HM310T power supply over the Modbus interface.  
See [further reading](#further-reading) below for technical details and register values.

⚠️ **Safety Warning**

The Hanmatek HM310T power supply is a device that can produce potentially dangerous levels of voltage and current. Always follow safety guidelines when working with electricity. Ensure your device is properly grounded and do not work on live circuits. 

This software is provided "as is", without warranty of any kind, express or implied. Incorrect use of this software could lead to damage to your power supply or other equipment, or personal injury. Use this software responsibly and at your own risk.

## Requirements

- Python 3.7 or higher
- PyModbus
- A Hanmatek HM310T power supply connected to a PC by USB
- May work with other Hanmatek power supplies, requires you to reverse engineer the unit

⚠️ **Use At Your Own Risk**

By using this software, you agree that the authors and maintainers of this software are not liable for any damage to equipment, or any personal injury, that may occur through normal or abnormal use of this software. Always double-check your work and never leave a powered device unattended.

...

## Installation

To install the library, clone this repository and install it using pip:

```bash
git clone https://github.com/joeyda3rd/hanmatek-power-supply.git
cd hanmatek-power-supply
pip install .
```

## Usage

Here are usage examples:

```python
from pyHM310T import PowerSupply

# Create instance with default parameters
# COM port, baudrate = 9600, slave=1, voltage_limit=30.0, current_limit=10.0):
power_supply = PowerSupply(port='/dev/ttyUSB0')

# Alternatively, create instance with custom parameters
# power_supply = PowerSupply('COM4', 115200, 2, 10.0, 5.0)

# Enable the output
power_supply.enable_output()

# Check if output is enabled
if power_supply.is_output_enabled():
    print("Output is enabled")

# Set the voltage to 5V
power_supply.set_voltage(5.0)

# Get the set voltage
set_voltage = power_supply.get_voltage()
print(f"Set voltage: {set_voltage}V")

# Set the current to 1A
power_supply.set_current(1.0)

# Get the set current
set_current = power_supply.get_current()
print(f"Set current: {set_current}A")

# Get voltage, current and power display (requires a load present)
print(f"Voltage display: {power_supply.get_voltage_display()}V")
print(f"Current display: {power_supply.get_current_display()}A")
print(f"Power display: {power_supply.get_power_display()}W")

# Get and set communication address
print(f"Communication address: {power_supply.get_comm_address()}")
power_supply.set_comm_address(2)
print(f"New communication address: {power_supply.get_comm_address()}")

# Get protection status
print(f"Protection status: {power_supply.get_protection_status()}")

# Get and set Over Voltage Protection (OVP) status
print(f"OVP status: {power_supply.get_ovp()}")
power_supply.set_ovp(True)
print(f"New OVP status: {power_supply.get_ovp()}")

# Get and set Over Current Protection (OCP) status
print(f"OCP status: {power_supply.get_ocp()}")
power_supply.set_ocp(True)
print(f"New OCP status: {power_supply.get_ocp()}")

# Get and set Over Power Protection (OPP) status
print(f"OPP status: {power_supply.get_opp()}")
power_supply.set_opp(True)
print(f"New OPP status: {power_supply.get_opp()}")

```

Please refer to the library API documentation for more details.

## Contributing

Contributions are welcome! Please open an issue if you encounter a bug or have a feature request. If you want to contribute code, please open a pull request.

## License

This library is licensed under the MIT license.

---
## Further Reading

Some previous work on the topic and documentation from OEM 

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
#1 See bit field below from documentation.   
#3 no idea  
#4 when it's reading 0x0233 that equals voltage has 2 decimal places, current 3, power 3  
#7, #14 Two 16 bit registers are used to make one 32 bit value.  
#14 type (range as it's called in docs) says 0-65535 (unsigned short) but I question that since it's a combination of two registers like #7
#15 docs say the range is 1-250, not sure of the best type to use for that, although not using a type in python. 

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
