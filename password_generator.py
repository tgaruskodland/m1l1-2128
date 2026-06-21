import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght = int(input("Podaj dlugosc hasla: "))

password = ""

for i in range(lenght):
    password += random.choice(elements)

print(password)