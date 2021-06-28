#Caesar's cipher
import math
    

# if direction=="encrypt":
def caesar(t,s,direction):
    s=s%25
    end_word=""
    for char in t:
        if char in alpha:
            position=alpha.index(char)
            if direction=="decode":
                s=-1*s
            new_position=position+s
            new_letter=alpha[new_position]
            end_word+=new_letter
        else:
            end_word+=char    
    print(f"The {direction}d code is {end_word}") 
replay=True
while replay:
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction=input("Type encode to encrypt and decode to decrypt").lower()
    text = input("Enter your text here").lower()
    shift = int(input("Type the shift number:"))       
    caesar(t=text,s=shift,direction=direction)  
    r=input("Do you want to do it again?").lower()  
    if r=="no":
        replay=False
        print("Thanks for using the machine")    
        
