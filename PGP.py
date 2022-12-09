'''
PGP using cryptography library
'''



from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


# Generate a new private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Convert the private key to PEM format
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Extract the public key from the private key
public_key = private_key.public_key()

# Convert the public key to PEM format
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Encrypt some data with the public key
data = b"Hello, World!"
encrypted_data = public_key.encrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt the encrypted data with the private key
decrypted_data = private_key.decrypt(
    encrypted_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Print the original data and the decrypted data
print("Original data: {}".format(data))
print("Decrypted data: {}".format(decrypted_data))
