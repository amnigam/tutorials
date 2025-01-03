# attacker.py
from Cryptodome.Hash import SHA256

# Simulate the known data from the "server"
KNOWN_MESSAGE = b"user=guest"
KNOWN_HASH = "5ffa216dce4521155b8808f304fc75e17eb5bc8774d7ac0ce24a1703698200b7"
# KNOWN_HASH = b'_\xfa!m\xceE!\x15[\x88\x08\xf3\x04\xfcu\xe1~\xb5\xbc\x87t\xd7\xac\x0c\xe2J\x17\x03i\x82\x00\xb7'
DATA_TO_APPEND = b";admin=true"

def sha256_padding(message_length):
    """Calculate SHA-256 padding for a given message length."""
    padding = b'\x80' + b'\x00' * ((56 - (message_length + 1) % 64) % 64)
    padding += (message_length * 8).to_bytes(8, byteorder="big")
    return padding

def perform_length_extension_attack(known_hash, known_message, data_to_add, secret_length_guess):
    """Perform the hash length extension attack."""
    # Calculate padding as SHA-256 would
    original_length = secret_length_guess + len(known_message)
    padding = sha256_padding(original_length)

    # Create the forged message
    forged_message = known_message + padding + data_to_add

    # Recreate the internal SHA-256 state from the known hash
    forged_hash = SHA256.new()
    forged_hash._h = tuple(int(known_hash[i:i+8], 16) for i in range(0, 64, 8))
    # forged_hash._state = known_hash._state
    forged_hash.update(data_to_add)

    return forged_message, forged_hash.hexdigest()

if __name__ == "__main__":
    # Assume the secret length is 12 (try different guesses in practice)
    secret_length_guess = 16

    forged_message, forged_hash = perform_length_extension_attack(
        KNOWN_HASH, KNOWN_MESSAGE, DATA_TO_APPEND, secret_length_guess
    )

    print(f"Forged Message: {forged_message.decode(errors='ignore')}")
    print(f"Forged Hash: {forged_hash}")
