from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# def rsa_keys():
# generate private/public key pair
key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
    key_size=2048)

# get public key in OpenSSH format
pem_public_key = key.public_key().public_bytes(serialization.Encoding.OpenSSH, \
    serialization.PublicFormat.OpenSSH)

# get private key in PEM container format
pem = key.private_bytes(encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())

# decode to printable strings
private_key_str = pem.decode('utf-8')
public_key_str = pem_public_key.decode('utf-8')

# print('Private key = ')
# print(private_key_str)
# print('Public key = ')
# print(public_key_str)

private_key_file = open("private_key_str.pem", "wb")
private_key_file.write(private_key_str.encode())
private_key_file.close()



public_key_file = open("public_key_str_ssh.pem", "w")
public_key_file.write(pem_public_key.decode())
public_key_file.close()

# public_key_file = open("public_key_str.pem", "rb")
# public_key_file = public_key_file.readlines()
# mytext = ""
# for items in public_key_file:
#     mytext = mytext + items +"\n"
# public_key_file.close()
# mytext = mytext[7:]
# public_key_file = open("public_key_str.pem","wb")
# public_key_file.write(mytext)

with open("public_key_str.pem","w") as output:
    with open("public_key_str_ssh.pem","r") as input:
        output.write(input.read()[8:])
# rsa_keys()