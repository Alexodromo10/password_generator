import random
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
question = int(input("Quanti caratteri deve essere la password? "))
password = ""
for i in range(question):
    password += random.choice(chars)

print(password)