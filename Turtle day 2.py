from turtle import *

speed(2)
bgcolor("orange")

penup()
goto(-180,-150)
pendown()

fillcolor("red")
begin_fill()

left(90)
forward(400)
right(90)
forward(380)
right(90)
forward(400)
right(90)
forward(380)

end_fill()

penup()

right(90)
forward(80)
right(90)
forward(50)

pendown()

fillcolor("yellow")
begin_fill()

forward(280)
left(120)
forward(280)
left(120)
forward(280)

end_fill()

hideturtle()
