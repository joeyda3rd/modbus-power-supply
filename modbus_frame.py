import struct
from pymodbus.utilities import computeCRC

# Slave address
slave_address = 1

# Function code for read holding registers
function_code = 3

# Starting address and quantity of registers
starting_address = 1000
quantity = 10

# Construct the data field
data = struct.pack('>HH', starting_address, quantity)

# Compute the CRC
crc = computeCRC(slave_address.to_bytes(1, 'big') + function_code.to_bytes(1, 'big') + data)

# Construct the frame
frame = slave_address.to_bytes(1, 'big') + function_code.to_bytes(1, 'big') + data + crc.to_bytes(2, 'little')

# Print the frame
print(frame)

