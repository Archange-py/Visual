_A='magenta'
from ext_turtle import*
from time import sleep
def infinity():setheading(0);pendown();color('blue');pensize(3);pendown();left(90);circle(50,180);home();right(90);circle(50,180)
def rosace():
	setheading(0);pendown();pensize(1);colors=['red',_A,'blue','cyan','green','white','yellow']
	for _ in range(6):
		for col in colors:pencolor(col);circle(50);left(10)
def von_koch():
	def _von_koch(n,L):
		if n==0:forward(L)
		else:_von_koch(n-1,L/3);left(60);_von_koch(n-1,L/3);right(120);_von_koch(n-1,L/3);left(60);_von_koch(n-1,L/3)
	setheading(0);pendown();color(_A);pensize(1)
	for i in range(6):clear();penup();goto(0,111);pendown();_von_koch(i,320);sleep(1)
von_koch()