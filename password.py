import random
import string

print("welcome to our random password generator : ")

def password():
    len = int(input("enter length of password : "))
    lowerd = string.ascii_lowercase
    upperd = string.ascii_uppercase
    digits = string.digits
    symbold = string.punctuation
    combine = lowerd+upperd+digits+symbold
    x = random.sample(combine , len)
    pwd = "".join(x)
    print(pwd)
    password()
password()