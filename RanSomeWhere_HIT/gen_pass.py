import random
import string

length=32

# lower = string.ascii_lowercase
# upper = string.ascii_uppercase
# num = string.digits
# symbols = string.punctuation

# all = lower + upper + num + symbols

# temp = random.sample(all,length)
# password = "".join(temp)

def generate():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all,length)
    password = "".join(temp)
    return password