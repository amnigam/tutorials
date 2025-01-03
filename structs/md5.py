import struct
import math

# Left-rotation function
def left_rotate(x, amount):
    x &= 0xFFFFFFFF  # Ensure x is a 32-bit integer
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

# Constants for MD5 (sines of integers converted to radians and scaled)
S = [
    7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
    5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
    4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
    6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21
]

# Precomputed table of constants
K = [int(abs(math.sin(i + 1)) * (2 ** 32)) & 0xFFFFFFFF for i in range(64)]

# Initial hash values
IVs = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

def md5(message):
    # Step 1: Padding the message
    original_length = len(message) * 8  # Length in bits
    message += b'\x80'  # Append a '1' bit followed by '0' bits
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'

    # Append the original length as a 64-bit value
    message += struct.pack('<Q', original_length)

    # Step 2: Process the message in 512-bit chunks
    A, B, C, D = IVs
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        M = struct.unpack('<16I', chunk)

        # Initialize working variables
        a, b, c, d = A, B, C, D

        # Main MD5 computation loop
        for i in range(64):
            if 0 <= i <= 15:
                F = (b & c) | (~b & d)
                g = i
            elif 16 <= i <= 31:
                F = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                F = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                F = c ^ (b | ~d)
                g = (7 * i) % 16

            F = (F + a + K[i] + M[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + left_rotate(F, S[i])) & 0xFFFFFFFF

        # Add this chunk's hash to the result
        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Step 3: Produce the final hash value (digest)
    return struct.pack('<4I', A, B, C, D).hex()

# Example usage
if __name__ == "__main__":
    x = input('[+] Enter String that you would like to hash: ') 
    data = bytes(x,'utf-8')  
    print("MD5:", md5(data))
