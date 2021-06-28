h=input("Input heigts of students").split()
for i in range(0,len(h)):
    h[i]=int(h[i])
print(f"Your input is {h}")
k=0
for s in range(0,len(h)):
    k=k+h[1]
avg=float(k/len(h))
print(f"Average height is {avg}")
