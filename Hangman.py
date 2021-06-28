
#Hangman problem
#It is basically guessing a word letter by letter until it is correct. If the letter you 
#guessed is not in the word then you'll lose a life. complete the word to win the game.
#code
import random
words=["apple","balloon","catastrophe","daughter","elephant"]
#randomly select a word from the list
sword=random.choice(words)
stage=[1,2,3,4,5,6]
slen=len(sword)
display=[]
for i in range(slen):
    display+="_"
end_game=False    
lives=5
while lives > 0:
    while not end_game:
        guess=input("Guess the letter").lower()
       
        if guess in display:
            print("You already guessed this word")
        for position in range(slen):
            letter=sword[position]
            if letter==guess:
                display[position]=letter
    
        if guess not in sword:
            print(f"Sorry your guess is {guess} and it's wrong. Your remaining lives {stage[lives]}")
            lives-=1
            if lives==0:
                end_game=True
                print("You lost")
                                
        print(f"{' '.join(display)}")
        if "_" not in display:
            end_game=True
            print("You won.")        
    
                
        
        
