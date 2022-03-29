#Homework-EP02_Turtle.py

import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

tao = turtle.Pen()
tao.speed(0)

turtle.bgcolor('brown')

def Go(x,y):
	tao.penup()
	tao.goto(x,y)
	tao.pendown()
	print(x)
	print(y)


def Draw():
	for j in range(90):
		tao.pencolor(colors[j%6])
		tao.width(j/50+1)
		tao.forward(j)
		tao.left(59)
Go(-100,100)
Draw()
Go(150,100)
Draw()
Go(-100,-150)
Draw()
Go(150,-150)
Draw()



