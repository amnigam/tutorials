from Cryptodome.Hash import SHA256
import hashlib 

def md5_hash(data): 
    m = hashlib.md5() 
    m.update(data) 
    m.digest() 
    return m.hexdigest() 

def sha256_padding(message_length):
    """Calculate SHA-256 padding for a given message length."""
    padding = b'\x80' + b'\x00' * ((56 - (message_length + 1) % 64) % 64)
    print(padding) 
    print((56 - (message_length + 1) % 64))
    padding += (message_length * 8).to_bytes(8, byteorder="big")
    return padding

# x = sha256_padding(24) 
text = b'the white tiger jumped over the fucking wall'
print(md5_hash(text)) 