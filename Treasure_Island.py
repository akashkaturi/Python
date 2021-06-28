print("Welcome to the treasure Island, Your mission is to find treasure")
path=input("Choose a path..Right or Left")
if path=="left":
    print("Choose an action.. swim or wait")
    action=input()
    if action=="wait":
        print("Choose color of the door..red blue or yellow")
        color=input()
        if color=="yellow":
            print("You win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")         
