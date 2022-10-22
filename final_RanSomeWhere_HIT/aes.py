#!/usr/bin/env python3

# Knowledge:
# AES: Advanced Encryption Standard
# Symmetric Cipher
# 16 byte block size: each part of the encrypted data is
# encrypted 16 bytes, it must be full, so padding is required.
# The keys can be 128, 192 or 256 bits long
# IV: stands for initialization vector

import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
"""In this function we encrypt the files that we chooes and change the type of files to our own , ".MAD_HIT" """
def encrypt(key, filename):
    chunksize = 64*1024
    outputFile ="enc_"+ filename +".MAD_HIT"
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            #Add padding if the file size cannot be divide into 16 bytes
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

"""In this function we decrypt the files with the our type,".MAD_HIT"  and change them back to there original type """
def decrypt(key, filename):
    chunksize = 64*1024
    outputFile ="dec_" + filename.split('.MAD_HIT')[0] 

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

#get SHA256 digest of the random key
def getKey(password):
    hasher = SHA256.new(password.encode())
    return hasher.digest()

