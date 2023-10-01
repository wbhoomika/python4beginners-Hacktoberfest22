#imports
from art import welcome_art
import time
import random

#defining various functions
def greet_users():
    print("Please wait...")
    time.sleep(2)
    print(welcome_art)
    time.sleep(1)
    print("Welcome to tic-tac-toe game , pls note that there must be two players")

def playground(x_place, o_place):
    print(f" {'X' if x_place[0] ==1 else 'O'if o_place[0]==1 else ' '} | {'X' if x_place[1] ==1 else 'O'if o_place[1]==1 else ' '} | {'X' if x_place[2] ==1 else 'O'if o_place[2]==1 else ' '} ")
    print("---|---|---")
    print(f" {'X' if x_place[3] ==1 else 'O'if o_place[3]==1 else ' '} | {'X' if x_place[4] ==1 else 'O'if o_place[4]==1 else ' '} | {'X' if x_place[5] ==1 else 'O'if o_place[5]==1 else ' '} ")
    print("---|---|---")
    print(f" {'X' if x_place[6] ==1 else 'O'if o_place[6]==1 else ' '} | {'X' if x_place[7] ==1 else 'O'if o_place[7]==1 else ' '} | {'X' if x_place[8] ==1 else 'O'if o_place[8]==1 else ' '} ")

def checkwinner(x_place, o_place):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if x_place[win[0]]+x_place[win[1]]+x_place[win[2]] == 3:
            return 1
        if o_place[win[0]]+o_place[win[1]]+o_place[win[2]] == 3:
            return 0
    return -1

greet_users()
USER_X_NAME = str(input("What is the name of user X ? ")).title()
USER_O_NAME = str(input("What is the name of user O ? ")).title()
print("processing, pls wait ")
time.sleep(1)
print(f"USER X : {USER_X_NAME}")
print(f"USER O : {USER_O_NAME}")
is_x_ready = str(input(f"Is {USER_X_NAME} ready to start the game ? Type X , if not ready type EXIT ").title())
if is_x_ready == "X":
    global is_o_ready
    is_o_ready = str(input(f"Is {USER_X_NAME} ready to start the game ? Type O , if not ready type EXIT ").title())
    if is_o_ready == "O":
        print("Ok so both of you are ready to play the game lets start")
    else:
        print(
            f"user {USER_O_NAME} is not ready to play the game is aborted, {USER_X_NAME} pls tell your friend to be "
            f"ready if you want to play the game , or find any other friend ;)")
else:
    print(f"user {USER_X_NAME} is not ready to play the game is aborted, {USER_O_NAME} pls tell your friend to be ready "
          f"if you want to play the game , or find any other friend ;)")

if is_o_ready == "O" and is_x_ready == "X":
    game_is_on = True
x_place_list = [0,0,0,0,0,0,0,0,0]
o_place_list = [0,0,0,0,0,0,0,0,0]

#tossing the first turn
print("Lets toss the coin and check whos turn is first!")
time.sleep(2)
print("Coing is flipping...")
time.sleep(3)
toss_output = random.randint(0,1)

if toss_output == 0:
    print(f"Hey {USER_X_NAME} its your turn !")
    TURN = "X"
else:
    print(f"Hey {USER_O_NAME} its your turn")
    TURN = "O"

time.sleep(3)
print("INSTRUCTIONS:\n 1. The boxes are designed serially,\n 2.like 1,2,3,\n       4,5,6,\n       7,8,9\n3. you have "
      "to type number where you want to put your mark")
time.sleep(5)
#staring the game
while game_is_on == True:
    playground(x_place=x_place_list,o_place= o_place_list)
    if TURN == "X":
        x_mark = int(input(f"{USER_X_NAME} where X ?"))
        if x_place_list[x_mark-1] == 0 and o_place_list[x_mark-1] == 0:
            x_place_list[x_mark-1] = 1
        else:
            print("This place already contains mark, pls try again")
            continue
        TURN = "O"
    else:
        o_mark = int(input(f"{USER_O_NAME} where O ?"))
        if o_place_list[o_mark-1] == 0 and x_place_list[o_mark-1] == 0:
            o_place_list[o_mark-1] = 1
        else:
            print("This place already contains mark, pls try again")
            continue
        TURN = "X"

    #last game ending logic
    cwin = checkwinner(x_place = x_place_list, o_place=o_place_list)
    if cwin == 1:
        playground(x_place=x_place_list, o_place=o_place_list)
        print(f"Hurray! {USER_X_NAME} is the winner, The game is ended")
        break
    if cwin == 0:
        playground(x_place=x_place_list, o_place=o_place_list)
        print(f"Hurray! {USER_O_NAME} is the winner, The game is ended")
        break

    total_marks = sum(x_place_list)+sum(o_place_list)
    if total_marks >= 9:
        print("Game is ENDED, and the result is DRAW :-)")
        playground(x_place=x_place_list, o_place=o_place_list)
        game_is_on = False