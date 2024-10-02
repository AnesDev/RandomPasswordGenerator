import time
import random
chars= "abcdefghijklmnopqrstuvwxyz"
charl = list(chars)
charu = list(chars.upper())
numbers = "0123456789"
nums = list(numbers) 
symbols = ["@","#","$","%"]
passkeys = charl + charu + nums + symbols
password = ""
print("Length of the password :")
for i in range(int(input())) :
    password += random.choice(passkeys)
print(password)
print(f"\n\n\n\n The excution time is : {time.process_time()} ")