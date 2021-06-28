score={"Ram":91,"Akash":97,"Kiran":89,"Rajesh":78,"Latha":68}
for s in score:
    marks=score[s]
    if score[s]>90:
        score[s]="Outstanding"
    elif score[s]>80:
        score[s]="Exceeding expectations"
    elif score[s]>70:
        score[s]="Average"
    else:
        score[s]="Need to improve"
print(score) 
