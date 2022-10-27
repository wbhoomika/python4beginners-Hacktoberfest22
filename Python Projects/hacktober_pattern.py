import turtle
t=turtle.Turtle()
t.penup()
t.goto(-30,50)


# H
t.pendown()
t.pensize(10)
t.pencolor("purple")
t.right(90)
t.forward(200)
t.goto(-30,-50)
t.goto(50,-50)
t.goto(50,50)
t.goto(50,-140)

t.penup();
t.goto(0, -200)

style = ('Courier', 30, 'normal')
t.write('Hacktoberfest', font=style, align='center')

