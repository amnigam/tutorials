import struct 

# Struct essentially defines a format in which data is getting formatted.
# Assume, I want to send DOB in this format across different systems. 
date = 9
month = 'December'
year = 1988

# Define a structure template => Integer 10Strings Integer. 
dob_struct = struct.pack('I 10s I',date, month.encode(), year ) 
print(dob_struct) 

# Unpack the struct to get back data. 
day, mon, year = struct.unpack('I 10s I', dob_struct) 
mon = mon.decode().rstrip('\x00') 

print(f'[+] Extracted Day: {day}') 
print(f'[+] Extracted Month: {mon}') 
print(f'[+] Extracted Year: {year}') 

print('-----------------------------------------------------------')

# Understanding Endian-ness. h = SHORT (2 bytes)
test = struct.pack(">h", 1500)
print(f'[-] Big Endian: {test}')        # Outputs => b'\x05\xdc'
test = struct.pack("<h", 1500)
print(f'[-] Little Endian: {test}')     # Outputs => b'\xdc\x05'