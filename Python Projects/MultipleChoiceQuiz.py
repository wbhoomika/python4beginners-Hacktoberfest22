#Import the needed libraries
#Import namedtuple from collections library
from collections import namedtuple

Question = namedtuple("Question", ["question", "answers", "correct_answer"])

#Welcoming message
#User adds their name
welcome = """Hello {name}, welcome 
Enter the appropriate number to answer the question correctly
Good luck!"""

#The functions needed 

def play_quiz(name, questions):
    score = 0 #Counting scores
    for question in questions:
        print(question.question)
        for i, answer in enumerate(question.answers, start=1): #Answers are numbered from 1
            print(f"{i}. {answer}")

        response = input("Your answer is: ")
        if response != question.correct_answer:
            print("Sorry, that is incorrect!") #Message if answer is incorrect
        else:
            print(f"Well done! {response} is correct!") #Message if answer is right
            score += 1
        print(f"Your current score is {score} out of {len(questions)}") #Updating score after each question

    print(f"Your total score is {score} out of {len(questions)}") #Message of final score after finishing the quiz
    print(f"Thank you for playing {name}, goodbye!")

#Questions asked

if __name__ == "__main__":
    questions = [Question("In Greek Mythology, who is the Queen of the Underworld and wife of Hades?",
                          ["Hestia", "Persephone", "Athena", "Artemis"], "2"),
                 Question("In which ocean is the Bermuda Triangle located?",
                          ["Artic", "Southern", "Indian", "Atlantic"], "4"),
                Question("What group of animals is known as a flamboyance??",
                          ["Peacocks", "Purple harlquin toads", "Flamingos", "Cuttlefish"], "4") ] #Numbers in "" represent the correct answers
    
#Adding the welcome function to the quiz
name = input("What is your name? ").title()
print(welcome.format(name=name, n=len(questions)))
play_quiz(name, questions) #Adding the play quiz def