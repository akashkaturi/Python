# Python
<!-- Basic Interactive coding exercises using Python -->
print("Welcome to the tip calculator.\n")
print("What was the total bill? $\n")
amount=float(input())
print("What precentage tip would you like to give? 10, 12, or 15?\n")
tip=float(input())
print("How many people to split the bill?")
per=float(input())
am_tip=amount+((tip/100)*amount)
split=am_tip/per
final_per_person=round(split,2)
print(f"Each person should pay: ${final_per_person}")
