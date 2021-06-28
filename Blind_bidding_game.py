

bid_p={}

def highest(bidders):
    high_amount=0
    winner=""
    for bidder in bidders:
        bid_amount=bidders[bidder]
        if high_amount<bid_amount:
            high_amount=bid_amount
            winner=bidder
    print(f"The winner is {winner} with bid amount ${high_amount}")    
        
        
        
r=True
while r:    
    n=input("Whats the bidder name?")
    a=int(input("What's the bidding amount?"))
    bid_p[n]=a
    replay=input("Are there any bidders? Yes or NO?").lower()
    if replay=="no":
        r=False
highest(bid_p)    
print(bid_p)   
