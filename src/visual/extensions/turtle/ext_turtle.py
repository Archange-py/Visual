from visuel import Vector,fill_rect,set_lines,draw_string
from math import sin,atan2,degrees,radians
import kandinsky as kd
try:from ext_lines import draw_lines
except:pass
class Screen:palette={"Background":(248,252,248),"PrimaryColor":(0,0,0),"SecondaryColor":(200,200,200),"PrimaryText":(0,0,0),"SecondaryText":(248,252,248),"PrimaryColor":(0,0,0),"SecondaryColor":(200,200,200),"ThirdColor":(235,235,235)}
class Turtle:
  def __init__(self,position=Vector(x=160,y=111),color=Screen.palette["PrimaryColor"],angle=Vector(x=1,y=0),pensize=1):self._color,self._penup,self._pendown,self._pensize,self._position,self._angle=color,True,False,pensize,position,angle
  @staticmethod
  def _lines(lines,color,pensize):set_lines(lines,color) if pensize==1 else draw_lines(lines,color,pensize)
  def forward(self,l):V=self._position+self._angle*l;V.round();Turtle._lines([(self._position,V)],self._color,self._pensize) if self._pendown else None;self._position=V
  def backward(self,l):V=self._position+self._angle*-l;V.round();Turtle._lines([(self._position,V)],self._color,self._pensize) if self._pendown else None;self._position=V
  def pendown(self):self._pendown,self._penup=True,False
  def penup(self):self._penup,self._pendown=True,False
  def right(self,a):self._angle=self._angle.rotate(a)
  def left(self,a):self._angle=self._angle.rotate(-a)  
  def goto(self,x,y):self._position=Vector(x=x,y=y)
  def pensize(self,t):self._pensize=abs(int(t))
  def pencolor(self,color):self._color=color
  def setx(self,x):self._position.x=x
  def sety(self,y):self._position.y=y
  def setheading(self,a):self._angle=self._angle.rotate(((a-self.heading())+360/2)%360-360/2)
  def write(self,text,color=Screen.palette["PrimaryText"],background=Screen.palette["SecondaryText"]):draw_string(text,self._position.x,self._position.y,color,background)
  def reset(self):fill_rect(0,0,320,222,Screen.palette['Background']);Screen.palette["Background"],self._color,self._penup,self._pendown,self._pensize,self._position,self._angle="white",Screen.palette["PrimaryColor"],True,False,1,Vector(x=160,y=111),Vector(x=1,y=0)
  def home(self):self.goto(160,111);self.setheading(0)
  def position(self):return(self.xcor(),self.ycor())
  def distance(self,x,y):return abs(Vector(x=x,y=y)-self._position)
  def towards(self,x,y):x,y=Vector(x=x,y=y)-self._position;return degrees(atan2(y,x))%360
  def heading(self):x,y=self._angle;return round(degrees(atan2(y,x)),10)
  def isdown(self):return(self._pendown==True)
  def xcor(self):return self._position.x
  def ycor(self):return self._position.y
  def circle(self,radius,extent=360,steps=None):
    if steps is None:steps=1+int(min(11+abs(radius)/6.0,59.0)*(abs(extent)/360))
    w=extent/steps;w2=0.5*w;l=2*radius*sin(radians(w2));l,w,w2=(-l,-w,-w2) if radius<0 else (l,w,w2);self.left(w2)
    for _ in range(steps):self.forward(l);self.left(w)
    self.left(-w2)
DefaultTurtle=Turtle()
def forward(*args,turtle=DefaultTurtle,**kwds):turtle.forward(*args,**kwds)
def backward(*args,turtle=DefaultTurtle,**kwds):turtle.backward(*args,**kwds)
def pendown(*args,turtle=DefaultTurtle,**kwds):turtle.pendown(*args,**kwds)
def penup(*args,turtle=DefaultTurtle,**kwds):turtle.penup(*args,**kwds)
def right(*args,turtle=DefaultTurtle,**kwds):turtle.right(*args,**kwds)
def left(*args,turtle=DefaultTurtle,**kwds):turtle.left(*args,**kwds)
def goto(*args,turtle=DefaultTurtle,**kwds):turtle.goto(*args,**kwds)
def pensize(*args,turtle=DefaultTurtle,**kwds):turtle.pensize(*args,**kwds)
def pencolor(*args,turtle=DefaultTurtle,**kwds):turtle.pencolor(*args,**kwds)
def setx(*args,turtle=DefaultTurtle,**kwds):turtle.setx(*args,**kwds)
def sety(*args,turtle=DefaultTurtle,**kwds):turtle.sety(*args,**kwds)
def setheading(*args,turtle=DefaultTurtle,**kwds):turtle.setheading(*args,**kwds)
def write(*args,turtle=DefaultTurtle,**kwds):turtle.write(*args,**kwds)
def reset(*args,turtle=DefaultTurtle,**kwds):turtle.reset(*args,**kwds)
def home(*args,turtle=DefaultTurtle,**kwds):turtle.home(*args,**kwds)
def circle(*args,turtle=DefaultTurtle,**kwds):turtle.circle(*args,**kwds)
def position(*args,turtle=DefaultTurtle,**kwds):return turtle.position(*args,**kwds)
def distance(*args,turtle=DefaultTurtle,**kwds):return turtle.distance(*args,**kwds)
def towards(*args,turtle=DefaultTurtle,**kwds):return turtle.towards(*args,**kwds)
def heading(*args,turtle=DefaultTurtle,**kwds):return turtle.heading(*args,**kwds)
def isdown(*args,turtle=DefaultTurtle,**kwds):return turtle.isdown(*args,**kwds)
def xcor(*args,turtle=DefaultTurtle,**kwds):return turtle.xcor(*args,**kwds)
def ycor(*args,turtle=DefaultTurtle,**kwds):return turtle.ycor(*args,**kwds)
def bgcolor(color):Screen.palette["Background"]=kd.color(color);fill_rect(0,0,320,222,Screen.palette["Background"])
def clear():fill_rect(0,0,320,222,Screen.palette['Background'])
color,fd,rt,lt,pos,color,background,width=pencolor,forward,right,left,position,pencolor,bgcolor,pensize;bk=back=backward;setpos=setposition=goto;pu=up=penup;pd=down=pendown