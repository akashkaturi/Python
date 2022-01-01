import random
names_csv = input(
    "Enter names who are ready to participate!(seperated by commas)")
names = names_csv.split(",")
length = len(names)

number = input("Create a seed number")
manipulation = random.randint(1, 100)
f_number = int(manipulation)-int(number)
random.seed(f_number)
k = random.choice(names)
print(k, "has to pay the bill")
