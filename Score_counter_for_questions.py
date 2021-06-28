class Text():
    def __init__(self, text,answer):
        self.text=text
        self.answer=answer 
    def view(self):
        return self.text, self.answer
class QuizBrain():
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def questions_left(self):
        if self.question_number<len(self.question_list):
            return True
    def check_answer(self,original_ans,answer):
        if original_ans==answer:
            self.score+=1
            print(f'You are right and your score is {self.score} out of {self.question_number}')
            
        else:
            print('You are wrong')
            print(f'You are wrong and your score is {self.score} out of {self.question_number}')
        
    def next_que(self):
        new_q=self.question_list[self.question_number]
        self.question_number+=1
        new_ans=input(f'{self.question_number}: {new_q.text}: ')
        self.check_answer(new_q.answer,new_ans)
   
        
       
question_data=[
    {"text":"que 1","ans":"1"},
    {"text":"que 2","ans":"2"},
    {"text":"que 3","ans":"3"},
    {"text":"que 4","ans":"4"},
    {"text":"que 5","ans":"5"},
    {"text":"que 6","ans":"6"}
]
q_and_a=[]
for question in question_data:
    que=question["text"]
    ans=question["ans"]
    new_q=Text(text=que,answer=ans)
    q_and_a.append(new_q)
h=QuizBrain(q_and_a)
while h.questions_left():
    h.next_que()
