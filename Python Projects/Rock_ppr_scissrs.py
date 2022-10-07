import random

user_score=0
comp_score=0

choices=['r','p','s'] #list of valid input choices for user

#idea: create a list/ dict for cases where user wins, and use that in if statements
#IDEA WORKED
win={}
lose={}

while True:
    user_inp=input("Enter R/P/S/q: ").lower()
    if user_inp=='q':
        break #quit out of the while loop, which will automatically end the game
    

    if user_inp not in choices:
        continue #will ask user to retype either r/p/s
    
    index=random.randint(0, 2) #choices for computer
    #r:0, p:1, s:2
    
    comp_inp=choices[index]
    print("Computer picked:" + str(comp_inp))

    if (user_inp=='r' and comp_inp=='s')or(user_inp=='s' and comp_inp=='p')or (user_inp=='p' and comp_inp=='r'):
        print("You won!!!!")
        win.update({user_inp:comp_inp})
    elif user_inp==comp_inp:
        print("Both guessed the same, no points awarded to either :)")
    else:
        print("You lost!!!!")
        lose.update({user_inp:comp_inp})
    '''
    if user_inp=='r' and comp_inp=='s':
        print("Yaay!")
        user_score+=1
    elif user_inp=='s' and comp_inp=='p':
        print("Yaay")
        user_score+=1
    elif user_inp=='p' and comp_inp=='r':
        print("Yaay")
        user_score+=1
    else:
        print("Naay")
        comp_score+=1
    '''

user_score=len(win)
comp_score=len(lose)

print("You scored: ", user_score)
print("Computer scored: ", comp_score)

if (user_score>comp_score):
    print("You won")
elif(user_score<comp_score):
    print("You lost")
else:
    print("Tied")
    
    
print("Good game champ!") 
