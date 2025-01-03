import hashlib 
from Cryptodome.Hash import MD5 
import pickle 

secret = b'secret_key' 

def internal_state(data):
    md5 = MD5.new() 
    md5.update(data) 
    # state = md5._state 
    state = pickle.dumps(md5) 
    print(dir(state)) 
    return state 

def padding(msgLen): 
    padding = b'\x80' + b'\x00' * ((56 - msgLen - 1-10) % 64)  # Remove 1 byte for 0x80. 10 for secret key.
    padding += (msgLen * 8).to_bytes(8, byteorder="little") 
    return padding

def md5_hash(data): 
    m = hashlib.md5() 
    m.update(secret) 
    m.update(data) 
    m.digest() 
    return m.hexdigest() 

def hashExtender(hash, message, extension):
    hashBytes = bytes.fromhex(hash) 
    h = hashlib.md5()

    h.update(hashBytes) 
    pad = padding(len(message)) 
    h.update(pad) 

    h.update(extension) 
    newHash = h.hexdigest() 
    
    return newHash 

t = b'Hello, Custom MD5!'
# print(len(t)) 
hash = md5_hash(t) 
print(f'[+] Original Hash of message: {hash}') 

e = b'roams free' 
serverHash = md5_hash(t+e) 
print(f'[+] Server side hash calculation is: {serverHash}') 

attackerHash = hashExtender(hash, t, e) 
print(f'[+] Attacker hash: {attackerHash}') 

print(internal_state(t))