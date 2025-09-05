_H='SecondaryText'
_G='PrimaryText'
_F='SecondaryColor'
_E=None
_D=False
_C='PrimaryColor'
_B=True
_A='Background'
from visuel import Vector,fill_rect,set_lines,draw_string
from math import sin,atan2,degrees,radians
import kandinsky as kd
try:from ext_lines import draw_lines
except:pass
class Screen:palette={_A:(248,252,248),_C:(0,0,0),_F:(200,200,200),_G:(0,0,0),_H:(248,252,248),_C:(0,0,0),_F:(200,200,200),'ThirdColor':(235,235,235)}
class Turtle:
	def __init__(A,position=Vector(x=160,y=111),color=Screen.palette[_C],angle=Vector(x=1,y=0),pensize=1):A._color,A._penup,A._pendown,A._pensize,A._position,A._angle=color,_B,_D,pensize,position,angle
	@staticmethod
	def _lines(lines,color,pensize):C=pensize;B=color;A=lines;set_lines(A,B)if C==1 else draw_lines(A,B,C)
	def forward(A,l):B=A._position+A._angle*l;B.round();Turtle._lines([(A._position,B)],A._color,A._pensize)if A._pendown else _E;A._position=B
	def backward(A,l):B=A._position+A._angle*-l;B.round();Turtle._lines([(A._position,B)],A._color,A._pensize)if A._pendown else _E;A._position=B
	def pendown(A):A._pendown,A._penup=_B,_D
	def penup(A):A._penup,A._pendown=_B,_D
	def right(A,a):A._angle=A._angle.rotate(a)
	def left(A,a):A._angle=A._angle.rotate(-a)
	def goto(A,x,y):A._position=Vector(x=x,y=y)
	def pensize(A,t):A._pensize=abs(int(t))
	def pencolor(A,color):A._color=color
	def setx(A,x):A._position.x=x
	def sety(A,y):A._position.y=y
	def setheading(A,a):A._angle=A._angle.rotate((a-A.heading()+360/2)%360-360/2)
	def write(A,text,color=Screen.palette[_G],background=Screen.palette[_H]):draw_string(text,A._position.x,A._position.y,color,background)
	def reset(A):fill_rect(0,0,320,222,Screen.palette[_A]);Screen.palette[_A],A._color,A._penup,A._pendown,A._pensize,A._position,A._angle='white',Screen.palette[_C],_B,_D,1,Vector(x=160,y=111),Vector(x=1,y=0)
	def home(A):A.goto(160,111);A.setheading(0)
	def position(A):return A.xcor(),A.ycor()
	def distance(A,x,y):return abs(Vector(x=x,y=y)-A._position)
	def towards(A,x,y):x,y=Vector(x=x,y=y)-A._position;return degrees(atan2(y,x))%360
	def heading(A):B,C=A._angle;return round(degrees(atan2(C,B)),10)
	def isdown(A):return A._pendown==_B
	def xcor(A):return A._position.x
	def ycor(A):return A._position.y
	def circle(C,radius,extent=360,steps=_E):
		G=extent;F=radius;D=steps
		if D is _E:D=1+int(min(11+abs(F)/6.,59.)*(abs(G)/360))
		B=G/D;A=.5*B;E=2*F*sin(radians(A));E,B,A=(-E,-B,-A)if F<0 else(E,B,A);C.left(A)
		for H in range(D):C.forward(E);C.left(B)
		C.left(-A)
DefaultTurtle=Turtle()
def forward(*A,turtle=DefaultTurtle,**B):turtle.forward(*A,**B)
def backward(*A,turtle=DefaultTurtle,**B):turtle.backward(*A,**B)
def pendown(*A,turtle=DefaultTurtle,**B):turtle.pendown(*A,**B)
def penup(*A,turtle=DefaultTurtle,**B):turtle.penup(*A,**B)
def right(*A,turtle=DefaultTurtle,**B):turtle.right(*A,**B)
def left(*A,turtle=DefaultTurtle,**B):turtle.left(*A,**B)
def goto(*A,turtle=DefaultTurtle,**B):turtle.goto(*A,**B)
def pensize(*A,turtle=DefaultTurtle,**B):turtle.pensize(*A,**B)
def pencolor(*A,turtle=DefaultTurtle,**B):turtle.pencolor(*A,**B)
def setx(*A,turtle=DefaultTurtle,**B):turtle.setx(*A,**B)
def sety(*A,turtle=DefaultTurtle,**B):turtle.sety(*A,**B)
def setheading(*A,turtle=DefaultTurtle,**B):turtle.setheading(*A,**B)
def write(*A,turtle=DefaultTurtle,**B):turtle.write(*A,**B)
def reset(*A,turtle=DefaultTurtle,**B):turtle.reset(*A,**B)
def home(*A,turtle=DefaultTurtle,**B):turtle.home(*A,**B)
def circle(*A,turtle=DefaultTurtle,**B):turtle.circle(*A,**B)
def position(*A,turtle=DefaultTurtle,**B):return turtle.position(*A,**B)
def distance(*A,turtle=DefaultTurtle,**B):return turtle.distance(*A,**B)
def towards(*A,turtle=DefaultTurtle,**B):return turtle.towards(*A,**B)
def heading(*A,turtle=DefaultTurtle,**B):return turtle.heading(*A,**B)
def isdown(*A,turtle=DefaultTurtle,**B):return turtle.isdown(*A,**B)
def xcor(*A,turtle=DefaultTurtle,**B):return turtle.xcor(*A,**B)
def ycor(*A,turtle=DefaultTurtle,**B):return turtle.ycor(*A,**B)
def bgcolor(color):Screen.palette[_A]=kd.color(color);fill_rect(0,0,320,222,Screen.palette[_A])
def clear():fill_rect(0,0,320,222,Screen.palette[_A])
color,fd,rt,lt,pos,color,background,width=pencolor,forward,right,left,position,pencolor,bgcolor,pensize
bk=back=backward
setpos=setposition=goto
pu=up=penup
pd=down=pendown