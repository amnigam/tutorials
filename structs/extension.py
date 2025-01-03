from Cryptodome.Hash import SHA256

# Simulate known hash
original_message = b"hello"
known_hash = SHA256.new(data=original_message)

# Manually extend the hash (Requires crafting padding and extension)
def sha256_length_extension(hash_object, additional_data, original_length):
    # Pad original message like SHA-256 would
    padding = b'\x80' + b'\x00' * ((56 - (original_length + 1) % 64) % 64)
    padding += (original_length * 8).to_bytes(8, byteorder="big")

    # Create new hash with padded message + additional_data
    extended_hash = SHA256.new()
    print(dir(extended_hash))
    extended_hash._state = hash_object._state  # Transfer internal state
    extended_hash.update(additional_data)
    return extended_hash

# Perform length extension
additional_data = b";admin=true"
# random = b"super_secret_keyuser=guest"   # Testing...
extended_hash = sha256_length_extension(known_hash, additional_data, len(original_message))

# Print results
print("Extended Hash:", extended_hash.hexdigest())
print("Server Generated: ", SHA256.new(data=additional_data).hexdigest()) 
