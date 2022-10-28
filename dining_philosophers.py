def test(x):
    if(state[x]=="Hungry"):
        if(state[(x+1)%n]!="Eating" and state[(x+n-1)%n]!="Eating"):
           state[x]="Eating"
           print("Philospher "+str(x)+" is eating")
def pickup(x):
    state[x] = "Hungry"
    test(x)
    if(state[x]=="Hungry"):
        print("Philospher "+str(x)+" is waiting")
def putdown(x):
    if(state[x]=="Eating"):
        print("philospher "+str(x)+" completed eating")
    state[x] = "Thinking"
    test((x+1)%n)
    test((x+n-1)%n)
n = int(input("enter no of philosphers : "))
state = ["Thinking"]*n
while(1):
    c = int(input("select any options 1.pickup 2.putdown 3.Exit : "))
    if(c==1):
        pickup(int(input("enter philopher number : ")))
    elif(c==2):
        putdown(int(input("enter philopher number : ")))
    else :
        break
