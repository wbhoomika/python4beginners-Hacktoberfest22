import random
# Importing Random Module

# Iniitiating an endless loop
while 1 > 0:
    l = []

    # Asking User for number of members and adding them to the list l[].
    m = int(input("How many members do you want to add to the wheel: "))
    for i in range(m):
        a = input("Enter Member: ")
        l.append(a)

    # Making Menu to select Spin or Quit for the User.
    i = 1
    while i == 1:
        a = int(input("""1. Spin
    2. Quit
    Enter Option: """))
        if a == 1:
            print(random.choice(l))
        elif a == 2:
            print("Quiting Loop")
            i = 0
        else:
            print("Invalid Character")
