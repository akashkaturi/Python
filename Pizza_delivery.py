print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size=="s" or size=="S":
    bill=15


elif size=="m" or size=="M":
     bill=20            


elif size=="l" or size=="L":
     bill=25   
    
if add_pepperoni=="Y" or add_pepperoni=="y":
    if size=="s" or size=="S":
        bill=bill+2
    else:
        bill=bill+3
if extra_cheese=="y" or extra_cheese=="Y":
    bill=bill+1
print(f"Your Total Bill is ${bill}")     
