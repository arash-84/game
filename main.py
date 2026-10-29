from rich.console import Console
console = Console()
questions=[
    ("whats the best CMS?",["A:Wordpress","B:Joomla","C: Drupal","D:Headless"],"A"),
    ("whats the best programming Languge?",["A:Wordpress","B:JavaScript","C: Java","D:C++"],"B"),
    ("whats the best database?",["A:MySQl","B:JavaScript","C: mangoDB","D:SQlite"],"C"),
    ]
score=0
BONUS=10
PENALTY=3
user_corrects=0
def show_manu():

    user_input=input("Do you want to start the quiz? (yes/no):").strip(). lower()
    if user_input =="yes":
        return True
    elif user_input =="mo":
        print("Exiting the quiz. Goodbye!")
        exit()
    else:
         print("Invalid input. please enter 'yes' or 'no'.")

def play_quiz():
    score=0
    user_corrects=0
    BONUS=10
    PENALTY=3
    for questions,options,correct_answer in questions:
        print(questions)
    for option in options:
        print(option)
    user_answer:str= input("Your choice:").strip().upper()
    if  user_answer== correct_answer:
        print("correct!")
        score+=BONUS
        user_corrects +=1
    else:
        print("Incorrect")
        score -=PENALTY
        score-=3
    return score, user_corrects
def show_results(score,user_corrects):

    print(f"Your final score is:{score}")
    print(f'Your answered{user_corrects} questions correctly.')
    console. print(f"Percentage:{user_corrects /len(questions)*100}",style="white on blue") 
while True:
    if show_manu():
        break
score,user_correctst= play_quiz()
show_results(score, user_corrects)


