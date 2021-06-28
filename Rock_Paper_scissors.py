import random
x=input("Rock or paper or scissors?")
print(f"Your choice is {x}")
computer=["rock","paper","scissors"]
# c=random.choice(computer)
k=random.randint(0,3)
c=computer[k]

print(f"Computer choice is {c}")
if x!=c:
    if x=="rock" and c=="scissors":
        print("You Won")
    elif x=="paper" and c=="rock":
        print("You Won")
    elif x=="scissors" and c=="paper":
        print("You Won")
    else:
        print("You Lost")            
else:
    print("It's a Draw")
