_D=True
_C=False
_B=None
_A='0'
from kandinsky import set_pixel,get_pixel,fill_rect,draw_string,color
from math import pi,cos,sin,radians,factorial
a,b,perm,distance,milieu,average=lambda P1,P2:(P2.y-P1.y)/(P2.x-P1.x),lambda a,P1:-(a*P1.x-P1.y),lambda n,k:factorial(n)/factorial(n-k),lambda P1,P2:((P2.x-P1.x)**2+(P2.y-P1.y)**2)**.5,lambda P1,P2,p=2:Point((P1.x+P2.x)/p,(P1.y+P2.y)/p),lambda liste:sum(liste)/len(liste)
DrawWithStyle={'O':'fill_circle(P,3,color)','+':'draw_croix(P,3,0,color)','*':'draw_croix(P,4,45,color)','.':'set_pixel(P.x,P.y,color)'}
class Point:
	def __init__(self,x,y,name=''):self.x,self.y,self.name=x,y,name
	def __str__(self):return str(self.name)
	def __iter__(self):return iter([self.x,self.y])
	def __repr__(self):return'Point({}, {})'.format(self.x,self.y)
	def __eq__(self,other):return self.x==other.x and self.y==other.y if isinstance(other,Point)else _C
	def round(self):self.x,self.y=round(self.x),round(self.y)
	def copy(self):return Point(self.x,self.y,self.name)
class Vector:
	def __init__(self,P1=_B,P2=_B,x=_B,y=_B,name=''):cond=P1!=_B and P2!=_B;self.x,self.y,self.name=P2.x-P1.x if cond else x,P2.y-P1.y if cond else y,name
	def __str__(self):return str(self.name)
	def __iter__(self):return iter([self.x,self.y])
	def __repr__(self):return'Vector({}, {})'.format(self.x,self.y)
	def __eq__(self,other):return self.x==other.x and self.y==other.y if isinstance(other,Vector)else _C
	def __add__(self,other):return Vector(x=self.x+other.x,y=self.y+other.y)if isinstance(other,Vector)else Point(other.x+self.x,other.y+self.y)if isinstance(other,Point)else _B
	def __sub__(self,other):return Vector(x=self.x-other.x,y=self.y-other.y)if isinstance(other,Vector)else Point(other.x-self.x,other.y-self.y)if isinstance(other,Point)else _B
	def __mul__(self,other):return Vector(x=self.x*other.x,y=self.y*other.y)if isinstance(other,Vector)else Vector(x=self.x*other,y=self.y*other)if isinstance(other,(int,float))else _B
	def __truediv__(self,other):return Vector(x=self.x/other.x,y=self.y/other.y)if isinstance(other,Vector)else Vector(x=self.x/other,y=self.y/other)if isinstance(other,(int,float))else _B
	def rotate(self,angle):angle=radians(angle);return Vector(x=self.x*cos(angle)-self.y*sin(angle),y=self.x*sin(angle)+self.y*cos(angle),name=self.name)
	def neg(self):return Vector(x=-self.x,y=-self.y,name=self.name)
	def copy(self):return Vector(x=self.x,y=self.y,name=self.name)
	def round(self):self.x=round(self.x);self.y=round(self.y)
def expend(liste,d,M=_B):M=Point(round(average([P.x for P in liste])),round(average([P.y for P in liste])))if M==_B else M;return[Point(round(P.x+(P.x-M.x)*d),round(P.y+(P.y-M.y)*d))if d!=0 else P for P in liste]
def connect_points(liste,ending=_C):line=[(liste[p],liste[p+1])for p in range(len(liste))if p<len(liste)-1];line.append((liste[-1],liste[0]))if ending else _B;return line
def findWithPoint(P1,P2,length):N=distance(P1,P2);return Point(P1.x+(P2.x-P1.x)*length/N,P1.y+(P2.y-P1.y)*length/N)
def alpha_pixel(x,y,col,alpha=1.):set_pixel(x,y,tuple(C1*alpha-C2*alpha+C2 for(C1,C2)in zip(color(col),get_pixel(x,y))))
def interpolate(C1,C2,N=100):C1,C2=color(C1),color(C2);interpolated_colors=[(C1[0]+(C2[0]-C1[0])*i/(N+1),C1[1]+(C2[1]-C1[1])*i/(N+1),C1[2]+(C2[2]-C1[2])*i/(N+1))for i in range(N+2)];return interpolated_colors[1:-1]
def scatter(X,Y,color=_A,style='*',C=Point(160,111)):draw_points([Point(round(C.x+x),round(C.y-y))for(x,y)in zip(X,Y)],color,style,_C)
def plot(X,Y,color=_A,C=Point(160,111)):set_lines(connect_points([Point(round(C.x+x),round(C.y-y))for(x,y)in zip(X,Y)]),color)
def draw_points(liste,color=_A,style='*',text=_D):
	for P in liste:exec(DrawWithStyle[style],{'P':P,'color':color,'set_pixel':set_pixel,'fill_circle':fill_circle,'draw_croix':draw_croix});draw_string(str(P.name),P.x+6,P.y+6,_A,'1')if text else _B
def draw_croix(center,r,angle=90,color=_A):
	R=Vector(center,Point(center.x+r,center.y));R=R.rotate(angle)
	for _ in range(4):R=R.rotate(90);R.round();set_lines([(center,R+center)],color)
def set_lines(line,color=_A):
	for(P1,P2)in line:
		up,right=_D if P2.y>P1.y else _C,_D if P2.x>P1.x else _C;h,b=P2.y-P1.y if up else P1.y-P2.y,P2.x-P1.x if right else P1.x-P2.x;n=_D if h<=b else _C;set_pixel(P2.x,P2.y,color)
		if b!=0 or h!=0:e=h/b if n else b/h
		for i in range(b if n else h):set_pixel(int(round(P1.x+i)if right else round(P1.x-i))if n else int(round(P1.x+e*i)if right else round(P1.x-e*i)),int(round(P1.y+e*i)if up else round(P1.y-e*i))if n else int(round(P1.y+i)if up else round(P1.y-i)),color)
def draw_arrows(liste,color=_A,length=10,angle=45,fill=_C):
	for(A,B)in liste:V1=Vector(findWithPoint(B,A,length),B).neg();V2,V3=V1.rotate(angle),V1.rotate(-angle);V2.round();V3.round();set_lines([(A,B)],color);set_lines([(B,V2+B),(B,V3+B)],color)if not fill else fill_triangles([(V2+B,B,V3+B)],color)
def draw_vector(P,V,color=_A):x,y=milieu(P,V+P);draw_arrows([(P,V+P)],color,fill=_C);draw_string(str(V.name),round(x-6),round(y-6),_A,'1')
def draw_droite(P1,P2,color=_A,name=_B):
	if P1.x==P2.x:set_lines([(Point(P1.x,0),Point(P1.x,222))],color)
	elif P1.y==P2.y:set_lines([(Point(0,P1.y),Point(320,P1.y))],color)
	else:_a=a(P1,P2);_b=b(_a,P2);P0,P3=Point(round((222-_b)/_a),222)if abs(P2.x-P1.x)<abs(P2.y-P1.y)else Point(0,round(_a*0+_b)),Point(round((-1-_b)/_a),-1)if abs(P2.x-P1.x)<abs(P2.y-P1.y)else Point(320,round(_a*320+_b));set_lines([(P0,P3)],color)
	if name!=_B:M=milieu(P1,P2);draw_string(str(name),round(M.x-6),round(M.y-6),_A,'1')
def fill_triangles(liste,color=_A,alpha=1):
	eq=lambda p,a,b:(a.x-p.x)*(b.y-p.y)-(a.y-p.y)*(b.x-p.x)
	for(P1,P2,P3)in liste:
		xmin,xmax,ymin,ymax=min(P1.x,P2.x,P3.x),max(P1.x,P2.x,P3.x)+1,min(P1.y,P2.y,P3.y),max(P1.y,P2.y,P3.y)+1;width,height=abs(xmax+xmin),abs(ymax+ymin)
		for y in range(ymin,ymax):
			if 0<=y<height:
				for x in range(xmin,xmax):
					pos=Point(x,y);w1,w2,w3=eq(pos,P3,P1),eq(pos,P1,P2),eq(pos,P2,P3)
					if 0<=x<width and(w1>=0 and w2>=0 and w3>=0 or-w1>=0 and-w2>=0 and-w3>=0):set_pixel(x,y,color)if alpha==1 else alpha_pixel(x,y,color,alpha)
def draw_polygone(n,rayon,coord,color=_A):alpha=2*pi/n;set_lines(connect_points([Point(round(coord.x+rayon*cos(k*alpha)),round(coord.y+rayon*sin(k*alpha)),color)for k in range(1,n+1)],_D),color)
def fill_polygone(n,rayon,coord,color=_A,c_map=_B,alpha=1):
	_alpha=2*pi/n;points=[Point(round(coord.x+rayon*cos(k*_alpha)),round(coord.y+rayon*sin(k*_alpha)))for k in range(1,n+1)]
	for(p,c)in zip(connect_points(points,_D),[color for _ in range(len(points))]if not isinstance(c_map,list)else c_map):fill_triangles([[coord,p[0],p[1]]],c,alpha)
def draw_rectangle(P1,P4,color=_A):fill_rect(P1.x,P1.y,P4.x-P1.x,1,color);fill_rect(P4.x,P1.y,1,P4.y-P1.y+1,color);fill_rect(P1.x,P4.y,P4.x-P1.x,1,color);fill_rect(P1.x,P1.y,1,P4.y-P1.y,color)
def fill_rectangle(P1,P4,color=_A,alpha=1):
	for x in range(P4.x-P1.x if P4.x>P1.x else P1.x-P4.x):
		for y in range(P4.y-P1.y if P4.y>P1.y else P1.y-P4.y):alpha_pixel(P1.x+x,P1.y+y,color,alpha)
def draw_circle(center,rayon,color=_A):
	for x in range(-abs(rayon),abs(rayon)):
		l=round((abs(rayon)**2-x**2)**.5)
		if abs(x)<=l:set_pixel(center.x+l,center.y+x,color);set_pixel(center.x-l,center.y-x,color);set_pixel(center.x-x,center.y-l,color);set_pixel(center.x+x,center.y+l,color)
def fill_circle(center,rayon,color=_A,alpha=1):
	for x in range(-round(rayon),round(rayon)+1):
		for y in range(-round(rayon),round(rayon)+1):
			if round(distance(center,Point(center.x+x,center.y+y)))<=rayon:alpha_pixel(center.x+x,center.y+y,color,alpha)if alpha!=1 else set_pixel(center.x+x,center.y+y,color)
def bezier_curve(liste,color=_A,thickness=1,N=1500):
	for _t in range(N):
		x,y,t=0,0,_t/N
		for i in range(len(liste)):x+=perm(len(liste)-1,i)/factorial(i)*t**i*(1-t)**(len(liste)-1-i)*liste[i].x;y+=perm(len(liste)-1,i)/factorial(i)*t**i*(1-t)**(len(liste)-1-i)*liste[i].y
		P=Point(round(x),round(y));set_pixel(P.x,P.y,color)if thickness==1 else fill_circle(P,thickness,color,1)