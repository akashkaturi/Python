import random
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', ]
a = int(input("No. of alphabetical characters required?"))
x = int(input("No. of numerical characters required?"))
s = int(input("No. of special characters required?"))
password = []
for i in range(1, a+1):
    password += random.choice(alpha)
for k in range(1, x+1):
    password += random.choice(num)
for j in range(1, s+1):
    password += random.choice(symbols)
random.shuffle(password)
passstr = ''.join(password)
print(f"Your recommended strong password is {passstr}")
