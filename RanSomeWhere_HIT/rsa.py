from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from Crypto.PublicKey import RSA

# generate private/public key pair
key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
    key_size=512)

# get public key in OpenSSH format
pem_public_key = key.public_key().public_bytes(encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo)


# get private key in PEM container format
pem = key.private_bytes(encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption())

# decode to printable strings
private_key_str = pem.decode('utf-8')
public_key_str = pem_public_key.decode('utf8')


private_key_file = open("private_key_str.pem", "wb")
private_key_file.write(private_key_str.encode())
private_key_file.close()


public_key_file = open("public_key_str.pem", "w")
public_key_file.write(pem_public_key.decode())
public_key_file.close()

