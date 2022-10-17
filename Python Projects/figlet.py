from pyfiglet import Figlet

s = input("Enter a string: ")
f = Figlet(font='slant')
print(f.renderText(s))
