height=float(input("Enter yor height in mts: "))
weight=float(input("Enter your weight in kgs: "))
bmi=(weight/(height*height))
print(float(bmi))
bmi_r=round(bmi,1)
print(f"{bmi_r}")
if bmi_r<18.5:
    print("Underweight")
elif bmi_r<25:
    print("Normal weight")
elif bmi_r<30:
    print("Overweight")
elif bmi_r<35:
    print("obese")
else:
    print("Clinically Obese")    
