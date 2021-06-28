height=float(input("Enter your Height!(in cms)"))
if height >= 120:
    print("You can ride rollercoaster")
    age=int(input("Enter Your age!"))
    # ch=5
    # yo=12
    # ad=18
    if age<12:
        # initial_price=ch
        bill=5
        print(f"Children Price is ${bill}")
    elif age<=18:
        # initial_price=yo
        bill=7
        print(f"Youth Price is ${bill}")
    elif age>=45 and age<=55:
            bill=0
            print(f"Special age category bill is ${bill}")
    else:
        # initial_price=ad
        bill=18
        print(f"Adults price is ${bill}")  
    
    k=input("Do you want any photo? Y or N")
    if k=="Y" or k=="y":
        bill=bill+3
        print(f"The total amount you need to pay is ${bill}")
    elif k=="N" or k=="n":
        print(f"The total amount you need to pay is ${bill}")

else:
    print("Sorry, You've to grow taller before you can ride")    
