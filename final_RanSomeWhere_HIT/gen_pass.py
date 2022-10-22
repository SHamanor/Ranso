import random
import string

"""In this file we generate a random new password """
length=32

def generate():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all,length)
    password = "".join(temp)
    return password