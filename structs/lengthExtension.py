from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import MD5 
import struct 

SECRET_KEY = b'mysecretkey' 
KEY_LEN = len(SECRET_KEY) 

# Function to compute MD5 hash
def compute_md5(secret, message):
    digest = hashes.Hash(hashes.MD5(), backend=default_backend()) 
    digest.update(secret+message) 
    return digest.finalize()    # returns a byte object.

# Helper function to compute MD5 padding for a given message length
def md5_padding(message_length):
    padding = b'\x80'
    padding += b'\x00' * ((56 - (message_length + 1) % 64) % 64)
    padding += struct.pack("<Q", message_length * 8)  # Append length in bits (little-endian)
    return padding

msg = b'testing some random data' 
out = compute_md5(SECRET_KEY,msg) 
# print(out.hex())
print(out)

original_msg = b'I need a coffee' 
original_hash = b'\xa9(0\xac\x8f0\xc43y\xa9\x16\x9d\x9a\xc1\x11_'
data_to_add = b'and a tea.' 

# Compute padding
original_length = KEY_LEN + len(original_msg)
padding = md5_padding(original_length) 

# Extended message
extended_message = original_msg + padding + data_to_add 

# Extract internal state from original hash
state = struct.unpack('<IIII', original_hash) 
print(state) 

# Create a new MD5 and manually set its state
new_digest = hashes.Hash(MD5(), backend=default_backend()) 
new_digest._ctx = new_digest._ctx.copy(state) 
new_digest.update(data_to_add) 
new_hash = new_digest.finalize() 

print(f'Extended Message: {extended_message}') 
print(f'New Hash: {new_hash.hex()}') 

# Verify
expected_hash = compute_md5(SECRET_KEY,extended_message) 
print(f'Expected Hash: {expected_hash.hex()}') 