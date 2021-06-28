import turtle as t 
import random
t.colormode(255)
screen=t.Screen()

def colint():
    k=random.randint(0,255)
    return k
def tup():
    h=[]
    for i in range(3):
        n=colint()
        h.append(n)
    return tuple(h)
def move_forwards():
    bun.forward(20)
def clockwise():
    k=bun.heading()
    bun.setheading(k+10)
def anti_clockwise():
    k=bun.heading()
    bun.setheading(k-10)
def home():
    bun.reset()

game_on=False
screen.setup(width=500, height=400)
user_bet=screen.textinput(title='Make your bet', prompt='Which trutle will win the race? Enter a Number? (1-6)')
y_postion=[-100,-60,-20,20,60,100]
y_postion.reverse()
players=[]
for i in range(0,6):
    new_bun=t.Turtle(shape='turtle') 
    new_bun.color(tup())
    new_bun.penup() 
    new_bun.goto(x=-230,y=y_postion[i])
    players.append(new_bun)
if user_bet:
    game_on=True 
while game_on:
    for player in players:
        if player.xcor()>230:
            game_on=False
            winning_number=players.index(player)+1
            if user_bet==winning_number:
                print(f'Yay you are a winner the winner is {winning_number}, your selection is {user_bet}')
            else:
                print(f'oops you lost, the winner is {winning_number}, your selection is {user_bet}')

        rand_distance=random.randint(0,10)
        player.forward(rand_distance)
        

    
screen.exitonclick()
