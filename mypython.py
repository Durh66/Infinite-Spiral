import math
import turtle
bob = turtle.Turtle()
a = 0
b= 0
s = turtle.Screen()
bob.pencolor("white")
s.bgcolor("black")
bob.speed(0)
bob.penup()
bob.goto(0,200)
bob.pendown()

while True:
    bob.fd(a)
    bob.rt(b)
    a +=3
    b+=1
    if b == 210:
        break
    bob.hideturtle
    
 




turtle.mainloop()
    