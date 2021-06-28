
print("Welcome to Love Calculator")
name1=input("What is your name?")
name2=input("What is their name?")
lower1=name1.lower()
lower2=name2.lower()
lower1=lower1+lower2
k=lower1.count("t")
k=k+lower1.count("r")
k=k+lower1.count("u")
k=k+lower1.count("e")
l=lower1.count("l")
l=l+lower1.count("o")
l=l+lower1.count("v")
l=l+lower1.count("e")
h=(k*10)+l
if (h<10) or (h>90):
    print(f"Your love score is {h}%, You go together as coke and mentos")
elif (h>=40) and (h<=50):
    print(f"Your score is {h}%, You're allright together")
else:
    print(f"Your score is {h}%")        
    print(f"True Love % of {name1} and {name2} is {h}%")
