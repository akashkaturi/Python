
import random
from random import randint

from numpy import append, true_divide
def total_sum(cards):
    if (sum(cards)==21 and len(cards)==2):
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    
    
    return(sum(cards))
def compare(sum1,sum2):
    if sum1==sum2:
        return "Draw"
    elif sum2==0:
        return "You lost, Opponent has black jack"
    elif sum1==0:
        return "You Won with a Blackjack"
    elif sum1>21:
        return "You went over. You lose"
    elif sum2>21:
        return "Opponent went over. You won"
    elif sum1==21:
        return "You won"
    elif sum1>sum2:
        return "You won"
    else:
        return "You lose"
comp=[]
player=[]
def sel_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10]
    return(random.choice(cards))
for i in range(0,2):
    player+=[sel_cards()]
for i in range(0,2):
    comp+=[sel_cards()] 
is_game_over=False
while not is_game_over:
    sum1=total_sum(player)
    sum2=total_sum(comp)    

            
    print(f"Your cards - {player}\nCurrent score - {sum1}")
   
    print(f"Computers first card is {comp[0]}")  

    
    if sum1==0 or sum2==0 or sum1>21:
        is_game_over=True
    else:
        deal=input("Press Y to draw or N to pass").lower()
        if deal=="y":
            player+=[sel_cards()]
            sum1=total_sum(player)
        else:
            is_game_over=True

while sum2!=0 and sum2<17:
    comp+=[sel_cards()]
    sum2=total_sum(comp)        
print(f"Your final hand: {player}, final score: {sum1}")
print(f"Computer's final hand: {comp}, final score: {sum2}")

compare(sum1,sum2)
