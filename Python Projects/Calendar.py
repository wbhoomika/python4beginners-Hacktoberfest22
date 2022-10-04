#for infinite loop
while 1>0:
    import calendar
    # Calendar is an built-in python Module
    
    # Next two lines take input of the year and month from the user.
    yyyy = int(input("Enter Year: "))
    mm = int(input("Enter Month: "))
    
    # Now, we will check whether the inputs are integers and the Month input is between 1 and 12.
    if isinstance(yyyy, int) and isinstance(mm, int):
        if mm >= 1 and mm <= 12:
            print(calendar.month(yyyy, mm))
        else:
            print("Not a valid Input.")
    else:
        print("Not valid")
