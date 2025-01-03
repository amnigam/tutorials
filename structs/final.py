import hashlib 

msg = b'Original Message' 
secret = b'my_secret_key'  

o = hashlib.sha256()
o.update(msg+secret) 
orignal_hash = o.digest().hex() 
print(orignal_hash)

def sha256_padding(message_length):
    """Calculate SHA-256 padding for a given message length."""
    padding = b'\x80' + b'\x00' * ((56 - (message_length + 1) % 64) % 64)
    padding += (message_length * 8).to_bytes(8, byteorder="big")
    return padding

def hash_len_extension(hash,len,extension):
    original_hash_bytes = bytes.fromhex(hash) 
    extension_bytes = extension.encode('utf-8') 
    padding = sha256_padding(len(extension_bytes))
    
    # New hash object
    h = hashlib.md5()
    h.update() 
