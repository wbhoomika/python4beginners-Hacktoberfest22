'''
This basic reddit bot lets the user view the titles of posts of any subreddit of their choice. 
They can also select the category and the number of titles they wan't to view.
'''

import praw

reddit=praw.Reddit(client_id='YsTBaKbPcMPQkFMyjm49tQ',
                   client_secret='ibQen4u2get7HLGsn_Z_kcOAr9_F3w',
                   user_agent='<console:Hello:1.0>')

subchoice=input("Enter name of subreddit:")
sub=reddit.subreddit(str(subchoice))

n=int(input('Enter number of posts you want to see:'))

def hot():
    for post in sub.hot(limit=n):
        print(post.title)
        print("")
        
def top():
    for post in sub.top(limit=n):
        print(post.title)
        print("")
        
def new():
    for post in sub.new(limit=n):
        print(post.title)
        print("")
        
def rising():
    for post in sub.rising(limit=n):
        print(post.title)
        print("")
    
def main():
    print("*************************")
    print("Subreddit Scraper v1.0")
    print("*************************")
    print("----------MENU----------")
    print("1-Hot")
    print("2-Top")
    print("3-New")
    print("4-Rising")
    print("5-QUIT PROGRAM")

    while True:
        
        posttype=int(input("Enter choice:"))
        
        if posttype==1:
            hot()
            print("****************")
            
        elif posttype==2:
            top()
            print("****************")
            
        elif posttype==3:
            new()
            print("****************")
            
        elif posttype==4:
            rising()
            print("****************")
            
        elif posttype==5:
            quit()
            
        else:
            print("Wrong choice entered. Enter again.")
        

main()
    
