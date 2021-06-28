from numpy import true_divide


def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def mul(num1,num2):
    return(num1*num2)
def div(num1,num2):
    return(num1/num2)
         

a=int(input("What's the first number?")) 
print(" + \n - \n / \n *")
o=input("Pick an operation: ")
b=int(input("What's the next number?"))
def cal(a,b,o):
    if o=="+":
        k=add(a,b)
        return k
    elif o=="-":
        k=sub(a,b)
        return k
    elif o=="/":
        k=div(a,b)
        return k
    else:
        k=mul(a,b)  
        return k
h=cal(a,b,o)    
print(f"You chose {o} and {a}{o}{b} of the numbers is {h}")
replay=True
while replay:
    j=input(f"Type 'y' to continue calculating with {h}, or type 'n' to start a new calculation").lower()
    if j=="y":
        a=int(h)
        o=input("Pick an operation: ")
        b=int(input("What's your next number"))
        h=cal(a,b,o)
        print(f"You chose {o} and {a}{o}{b} of the numbers is {h}")
    elif j=="n":
        a=int(input("What's the first number?")) 
        o=input("Pick an operation: ")
        b=int(input("What's the next number?"))
        h=cal(a,b,o)    
        print(f"You chose {o} and {a}{o}{b} of the numbers is {h}")
    else:
        replay=False 
        print("The calculator is stopped")
