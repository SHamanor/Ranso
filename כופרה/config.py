import gen_pass
from Crypto.PublicKey import RSA
from pyasn1_modules import pem, rfc2459
from pyasn1.codec.der import decoder
from Crypto.Cipher import PKCS1_OAEP
import aes,os,binascii

import binascii
import ctypes

from Crypto.PublicKey import RSA
from pathlib import Path
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto import Random
def gen():

    password =gen_pass.generate()
    key = open("public_key_str.pem", "rb")
    public_key =key.read()
    key.close()

    # with open("password.txt", "w") as external_file:
    #     add_text = password
    #     print(add_text, file=external_file)
    #     external_file.close()
    
    recipient_key = RSA.import_key(public_key)
    encryptorRSA = PKCS1_OAEP.new(recipient_key)
    enckey=encryptorRSA.encrypt(password)

    f=open(os.environ['HOME'] +'/Desktop/','wb')
    f.write(binascii.hexlify(enckey))
    f.close()

    return password