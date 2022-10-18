from tkinter import E
import aes
import rsa
import files
import gen_pass
import base64
import os
import config
import os

def Main():
    #encrypt files and decrypt files
    choice = input("Would you like to (E)ncrypt of (D)ecrypt or (P)assword?: ").upper()

    if choice == 'E':
        password =config.gen() 
        # filename = input("File to encrypt: ")
        # password = input("Password: ")
        for i in files.getfiles_enc():
            file_name = i.split("/")[-1]
            print(file_name)
            file_path = i.replace(file_name, "")
        # word = cl.blue+"Encryption: "+cl.end+str(file_name)
        # write(word)
            os.chdir(file_path)
            aes.encrypt(aes.getKey(password),file_name)
            try:
                os.remove(file_name)
            except OSError:
                pass
        # for file in files.getfiles():
        #     print(file)
        #     aes.encrypt(aes.getKey(password),file)
        print("Done.")

    elif choice == 'D':
        # filename = input("File to decrypt: ")
        password = input("Password: ")
        for i in files.getfiles_dec():
            name = i.split("/")[-1]
            print(name)
            path = i.replace(name, "")
            os.chdir(path)
            # f = open("password.txt", "r")
            aes.decrypt(aes.getKey(password.encode('utf-8')), name)
            os.remove(name)
        # aes.decrypt(aes.getKey(password), files.getFile(list_d))
        print("Done.")

    elif choice == 'P':
        choice1 =input("Did you encrypt the files already? in order to get the current password \n (Y)es / (N)o\n")
        if choice1 =='Y':
            f = open('password.txt', 'r')
            file_contents = f.read()
            print("The password : " ,file_contents)
            f.close()
        elif choice1 == 'N':
            Main()

    else:
        print("No option selected, closing...")

if __name__ == "__main__":
    Main()