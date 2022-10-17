"""
Program to perform various function related to Stacks.
"""

def push_stack(stack,item):
    '''
    To push an element into the Stack. 

    Parameters
    ----------
    stack : LIST
        list of umeric characters.
    item : NUMERIC
        Element to be pushed in stack.

    '''
    stack.append(item)
    print(item,"pushed successfully into stack.")

def pop_stack(stack):
    '''
    To pop last element of the stack.

    Parameters
    ----------
    stack : LIST
        list of numeric characters.

    '''
    if len(stack)==0:
        print("Stack Underflow !!!")
    
    else:
        top=len(stack)-1
        top_element=stack.pop(top)
        print("Element",top_element," poped.")
        

def display_stack(stack):
    '''
    To view stack.

    Parameters
    ----------
    stack : LIST
        list of numeric characters.

    '''
    length=len(stack)
    if length==0:
        print("Stack is empty.")
        
    else:
        print("Stack is: ")
        for i in range(len(stack)-1, -1, -1):
            print("\t",stack[i])


def peek_stack(stack):
    '''
    To view topmost/last element of the stack.

    Parameters
    ----------
    stack : LIST
        list of numeric characters.

    '''
    length=len(stack)
    if length==0:
        print("Stack is Empty")
    else:
      print('Topmost element is:',stack[length-1])

#--------------------main--------------------------
stack=[] 
menu='''
----------------------------------
| {:^30s} |
----------------------------------
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
----------------------------------
'''.format("MENU",
            "1. Add element to stack.",
            "2. Remove element from stack.",
            "3. View stack contents.",
            "4. Peek stack.",
            "5. QUIT."
            )

while True:
    print(menu)
    act=input("Enter the serial number of the task you want to perform: ")
    
    if act=='1':
        item=int(input("Enter new element: "))
        push_stack(stack, item)
        
    elif act=='2':
        pop_stack(stack)
        
    elif act=='3':
        display_stack(stack)
        
    elif act=='4':
        peek_stack(stack)
        
    elif act=='5':
        print("Thank you for using this program.")
        break
    
    else:
        print("Please enter valid number !!!")
    
    print("*"*100)
    