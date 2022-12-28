from data import question_data

class Question:
    def __init__(self,q_text,q_answer):
        self.text = q_text 
        self.answer = q_answer 

class QuizBrain:
    def __init__(self,q_list):#question_bank - jismai question or ans ka hold ha
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_have_questions(self):
        # if self.question_number <  len(self.question_list) :
        #     return True
        # else:
        #     return False     
        # short cut
        return self.question_number < len(self.question_list) #this is going to return true or false
 
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}  (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score +=1
        else:
            print("Thsts wrong")    
        print(f"The correct answwer is: {correct_answer} ")    
        print(f"Your current score is {self.score}/{self.question_number} ")
        print("\n")

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)#holding all data(question and answer)

quiz = QuizBrain(question_bank) 
while quiz.still_have_questions():#if quiz still have questions remaining
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final answer is: {quiz.score}/{quiz.question_number} ")

















