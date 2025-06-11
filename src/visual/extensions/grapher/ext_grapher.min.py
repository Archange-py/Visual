_N='Liste X an Y must have the same size'
_M=False
_L=True
_K='SecondaryText'
_J='ThirdColor'
_I='style'
_H='SecondaryColor'
_G='Background'
_F='PrimaryColor'
_E='color'
_D=None
_C='Y'
_B='X'
_A='liste'
from visual import Point,Vector,fill_rect,draw_string,draw_points,set_lines,draw_vector,expend,connect_points
from ion import keydown,KEY_UP,KEY_DOWN,KEY_RIGHT,KEY_LEFT,KEY_MINUS,KEY_PLUS,KEY_BACKSPACE,KEY_ZERO
from time import sleep
class Screen:p,center,width,height,palette=3,Point(160,111),320,222,{_G:(248,252,248),_F:(0,0,0),_H:(200,200,200),'PrimaryText':(0,0,0),_K:(248,252,248),_F:(0,0,0),_H:(200,200,200),_J:(235,235,235)}
class Grapher:
	def __init__(A,p=45,Lxg=round(Screen.width/2),Lxd=round(Screen.width/2),Lyh=round(Screen.height/2),Lyb=round(Screen.height/2),C=Screen.center,text=_L,background=_L,color1=Screen.palette[_F],color2=Screen.palette[_H],color3=Screen.palette[_J],pas=_D):Screen.palette[_F],Screen.palette[_H],Screen.palette[_J]=color1,color2,color3;A.p,A.Lxg,A.Lxd,A.Lyh,A.Lyb,A._Lxg,A._Lxd,A._Lyh,A._Lyb,A.C,A._C,A.text,A.background,A.pas=p,Lxg,Lxd,Lyh,Lyb,Lxg,Lxd,Lyh,Lyb,Point(C.x,C.y),Point(C.x,C.y),text,background,round(p/5)if pas==_D else pas;A._liste_scatter,A._liste_plot,A._liste_point,A._liste_line,A._liste_droite,A._liste_vector,A.liste_scatter,A.liste_plot,A.liste_point,A.liste_line,A.liste_droite,A.liste_vector=[],[],[],[],[],[],[],[],[],[],[],[]
	def check(A,x,y):return round(A._C.x+x*A.p)>A.C.x-A.Lxg+Screen.p and round(A._C.x+x*A.p)<A.C.x+A.Lxd-Screen.p and round(A._C.y-y*A.p)>A.C.y-A.Lyh+Screen.p and round(A._C.y-y*A.p)<A.C.y+A.Lyb-Screen.p
	def find_intersections(B,P0,P1,segments,droite=_M):
		I=droite
		def A(P0,P1,A,B):
			C=P0;D,F=Point(P1.x-C.x,P1.y-C.y),Point(B.x-A.x,B.y-A.y);G=D.x*F.y-D.y*F.x
			if G==0:return
			E,J=((A.x-C.x)*F.y-(A.y-C.y)*F.x)/G,((A.x-C.x)*D.y-(A.y-C.y)*D.x)/G
			if not I and 0<=E<=1 and 0<=J<=1:H=Point(C.x+E*D.x,C.y+E*D.y);return H
			elif I and 0<=J<=1:H=Point(C.x+E*D.x,C.y+E*D.y);return H
		return[A(P0,P1,B,C)for(B,C)in segments]
	def scatter(A,X,Y,color=Screen.palette[_F],style='O'):
		C=style;B=color
		if len(X)!=len(Y):raise TypeError(_N)
		if not{_B:X,_C:Y,_E:B,_I:C}in A.liste_scatter:A._liste_scatter.append({_B:X,_C:Y,_E:B,_I:C});A.liste_scatter.append({_B:X,_C:Y,_E:B,_I:C})
		else:draw_points([Point(round(A._C.x+B*A.p),round(A._C.y-C*A.p))for(B,C)in zip(X,Y)if A.check(B,C)],B,C,_M)
	def plot(A,X,Y,color=Screen.palette[_F]):
		C=color
		if len(X)!=len(Y):raise TypeError(_N)
		if not{_B:X,_C:Y,_E:C}in A.liste_plot:A._liste_plot.append({_B:X,_C:Y,_E:C});A.liste_plot.append({_B:X,_C:Y,_E:C})
		else:
			H=[(Point(A.C.x-A.Lxd,A.C.y-A.Lyb),Point(A.C.x+A.Lxg,A.C.y-A.Lyb)),(Point(A.C.x-A.Lxd,A.C.y+A.Lyh),Point(A.C.x+A.Lxg,A.C.y+A.Lyh)),(Point(A.C.x-A.Lxd,A.C.y-A.Lyb),Point(A.C.x-A.Lxd,A.C.y+A.Lyh)),(Point(A.C.x+A.Lxg,A.C.y-A.Lyb),Point(A.C.x+A.Lxg,A.C.y+A.Lyh))];I=[Point(round(A._C.x+B*A.p),round(A._C.y-C*A.p))for(B,C)in zip(X,Y)if round(A._C.x+B*A.p)>A.C.x-A.Lxg and round(A._C.x+B*A.p)<A.C.x+A.Lxd and round(A._C.y-C*A.p)>A.C.y-A.Lyh and round(A._C.y-C*A.p)<A.C.y+A.Lyb]
			for(D,E)in connect_points([Point(round(A._C.x+B*A.p),round(A._C.y-C*A.p))for(B,C)in zip(X,Y)]):
				F=A.find_intersections(D,E,H);B=[Point(round(A.x),round(A.y))for A in F if A!=_D];G=len(B)
				if G==2:set_lines([(B[0],B[1])],C)
				elif G==1 and F[0]!=_D:set_lines([(D,B[0])],C)if D.y>=B[0].y else set_lines([(B[0],E)],C)
				elif G==1 and F[1]!=_D:set_lines([(D,B[0])],C)if D.y<=B[0].y else set_lines([(B[0],E)],C)
				elif G==1 and F[2]!=_D:set_lines([(D,B[0])],C)if D.x>=B[0].x else set_lines([(B[0],E)],C)
				elif G==1 and F[3]!=_D:set_lines([(D,B[0])],C)if D.x<=B[0].x else set_lines([(B[0],E)],C)
				elif D in I:set_lines([(D,E)],C)
			fill_rect(A.C.x-A.Lxg,A.C.y+A.Lyh,A.Lxd+A.Lxg,1,Screen.palette[_G]);fill_rect(A.C.x+A.Lxg,A.C.y-A.Lyb,1,A.Lyb+A.Lyh,Screen.palette[_G])
	def set_points(A,liste,color=Screen.palette[_F],style='O'):
		D=style;C=color;B=liste
		if not{_A:B,_E:C,_I:D}in A.liste_point:A._liste_point.append({_A:B,_E:C,_I:D});A.liste_point.append({_A:B,_E:C,_I:D})
		else:draw_points([Point(round(A._C.x+B.x*A.p),round(A._C.y-B.y*A.p))for B in B if A.check(B.x,B.y)],C,D,_M)
	def set_lines(A,liste,color=Screen.palette[_F]):
		F=liste;C=color
		if not{_A:F,_E:C}in A.liste_line:A._liste_line.append({_A:F,_E:C});A.liste_line.append({_A:F,_E:C})
		else:
			I=[(Point(A.C.x-A.Lxd,A.C.y-A.Lyb),Point(A.C.x+A.Lxg,A.C.y-A.Lyb)),(Point(A.C.x-A.Lxd,A.C.y+A.Lyh),Point(A.C.x+A.Lxg,A.C.y+A.Lyh)),(Point(A.C.x-A.Lxd,A.C.y-A.Lyb),Point(A.C.x-A.Lxd,A.C.y+A.Lyh)),(Point(A.C.x+A.Lxg,A.C.y-A.Lyb),Point(A.C.x+A.Lxg,A.C.y+A.Lyh))];J=connect_points([Point(round(A._C.x+B.x*A.p),round(A._C.y-B.y*A.p))for B in F if round(A._C.x+B.x*A.p)>A.C.x-A.Lxg and round(A._C.x+B.x*A.p)<A.C.x+A.Lxd and round(A._C.y-B.y*A.p)>A.C.y-A.Lyh and round(A._C.y-B.y*A.p)<A.C.y+A.Lyb])
			for(D,E)in connect_points([Point(round(A._C.x+B.x*A.p),round(A._C.y-B.y*A.p))for B in F]):
				G=A.find_intersections(D,E,I);B=[Point(round(A.x),round(A.y))for A in G if A!=_D];H=len(B)
				if H==2:set_lines([(B[0],B[1])],C)
				elif H==1 and G[0]!=_D:set_lines([(D,B[0])],C)if D.y>=B[0].y else set_lines([(B[0],E)],C)
				elif H==1 and G[1]!=_D:set_lines([(D,B[0])],C)if D.y<=B[0].y else set_lines([(B[0],E)],C)
				elif H==1 and G[2]!=_D:set_lines([(D,B[0])],C)if D.x>=B[0].x else set_lines([(B[0],E)],C)
				elif H==1 and G[3]!=_D:set_lines([(D,B[0])],C)if D.x<=B[0].x else set_lines([(B[0],E)],C)
				elif(D,E)in J:set_lines([(D,E)],C)
			fill_rect(A.C.x-A.Lxg,A.C.y+A.Lyh,A.Lxd+A.Lxg+1,1,Screen.palette[_G]);fill_rect(A.C.x+A.Lxg,A.C.y-A.Lyb,1,A.Lyb+A.Lyh,Screen.palette[_G])
	def set_vectors(A,P,V,color=Screen.palette[_F]):
		C=color
		if not{_A:[P,V+P],_E:C}in A.liste_vector:A._liste_vector.append({_A:[P,V+P],_E:C});A.liste_vector.append({_A:[P,V+P],_E:C})
		else:
			H=[(Point(A.C.x-A.Lxd,A.C.y-A.Lyb),Point(A.C.x+A.Lxg,A.C.y-A.Lyb)),(Point(A.C.x-A.Lxd,A.C.y+A.Lyh),Point(A.C.x+A.Lxg,A.C.y+A.Lyh)),(Point(A.C.x-A.Lxd,A.C.y-A.Lyb),Point(A.C.x-A.Lxd,A.C.y+A.Lyh)),(Point(A.C.x+A.Lxg,A.C.y-A.Lyb),Point(A.C.x+A.Lxg,A.C.y+A.Lyh))];I=connect_points([Point(round(A._C.x+B.x*A.p),round(A._C.y-B.y*A.p))for B in[P,V+P]if round(A._C.x+B.x*A.p)>A.C.x-A.Lxg and round(A._C.x+B.x*A.p)<A.C.x+A.Lxd and round(A._C.y-B.y*A.p)>A.C.y-A.Lyh and round(A._C.y-B.y*A.p)<A.C.y+A.Lyb])
			for(D,E)in connect_points([Point(round(A._C.x+B.x*A.p),round(A._C.y-B.y*A.p))for B in[P,V+P]]):
				F=A.find_intersections(D,E,H);B=[Point(round(A.x),round(A.y))for A in F if A!=_D];G=len(B)
				if G==2:set_lines([(B[0],B[1])],C)
				elif G==1 and F[0]!=_D:set_lines([(D,B[0])],C)if D.y>=B[0].y else draw_vector(B[0],Vector(x=E.x-B[0].x,y=E.y-B[0].y),C)
				elif G==1 and F[1]!=_D:set_lines([(D,B[0])],C)if D.y<=B[0].y else draw_vector(B[0],Vector(x=E.x-B[0].x,y=E.y-B[0].y),C)
				elif G==1 and F[2]!=_D:set_lines([(D,B[0])],C)if D.x>=B[0].x else draw_vector(B[0],Vector(x=E.x-B[0].x,y=E.y-B[0].y),C)
				elif G==1 and F[3]!=_D:set_lines([(D,B[0])],C)if D.x<=B[0].x else draw_vector(B[0],Vector(x=E.x-B[0].x,y=E.y-B[0].y),C)
				elif(D,E)in I:draw_vector(D,Vector(x=E.x-D.x,y=E.y-D.y),C)
			fill_rect(A.C.x-A.Lxg,A.C.y+A.Lyh,A.Lxd+A.Lxg+1,1,Screen.palette[_G]);fill_rect(A.C.x+A.Lxg,A.C.y-A.Lyb,1,A.Lyb+A.Lyh,Screen.palette[_G])
	def set_droite(C,A,B,color=Screen.palette[_F]):
		D=color
		if not{_A:[A,B],_E:D}in C.liste_droite:C._liste_droite.append({_A:[A,B],_E:D});C.liste_droite.append({_A:[A,B],_E:D})
		else:
			F=[(Point(C.C.x-C.Lxd,C.C.y-C.Lyb),Point(C.C.x+C.Lxg,C.C.y-C.Lyb)),(Point(C.C.x-C.Lxd,C.C.y+C.Lyh),Point(C.C.x+C.Lxg,C.C.y+C.Lyh)),(Point(C.C.x-C.Lxd,C.C.y-C.Lyb),Point(C.C.x-C.Lxd,C.C.y+C.Lyh)),(Point(C.C.x+C.Lxg,C.C.y-C.Lyb),Point(C.C.x+C.Lxg,C.C.y+C.Lyh))]
			for(G,H)in connect_points([Point(round(C._C.x+A.x*C.p),round(C._C.y-A.y*C.p))for A in[A,B]]):I=C.find_intersections(G,H,F,_L);E=[Point(round(A.x),round(A.y))for A in I if A!=_D];set_lines([(E[0],E[1])],D)if len(E)==2 else _D
			fill_rect(C.C.x-C.Lxg,C.C.y+C.Lyh,C.Lxd+C.Lxg+1,1,Screen.palette[_G]);fill_rect(C.C.x+C.Lxg,C.C.y-C.Lyb,1,C.Lyb+C.Lyh,Screen.palette[_G])
	def clean(A):A._liste_scatter,A._liste_plot,A._liste_point,A._liste_line,A._liste_droite,A._liste_vector,A.liste_scatter,A.liste_plot,A.liste_point,A.liste_line,A.liste_droite,A.liste_vector=[],[],[],[],[],[],[],[],[],[],[],[];fill_rect(A.C.x-A.Lxg,A.C.y-A.Lyh,A.Lxg+A.Lxd,A.Lyh+A.Lyb,Screen.palette[_G]);A.set_axes()
	def set_axes(A):
		if A.background:
			for D in range(A._Lyh,0,-A.p):fill_rect(A.C.x-A.Lxg,A._C.y-A._Lyh+round(D-A.p/2),A.Lxg+A.Lxd,1,Screen.palette[_J])if A.C.y-A._Lyh+round(D-A.p/2)>A.C.y-A._Lyh and A.C.y-A._Lyh+round(D-A.p/2)<A.C.y+A._Lyb else _D
			for C in range(0,A._Lyb,A.p):fill_rect(A.C.x-A.Lxg,A._C.y+round(C+A.p/2),A.Lxg+A.Lxd,1,Screen.palette[_J])if A.C.y+round(C+A.p/2)>A.C.y-A._Lyh and A.C.y+round(C+A.p/2)<A.C.y+A._Lyb else _D
			for D in range(A._Lxg,0,-A.p):fill_rect(A._C.x-A._Lxg+round(D-A.p/2),A.C.y-A.Lyh,1,A.Lyh+A.Lyb,Screen.palette[_J])if A.C.x-A._Lxg+round(D-A.p/2)>A.C.x-A._Lxg and A.C.x-A._Lxg+round(D-A.p/2)<A.C.x+A._Lxd else _D
			for C in range(0,A._Lxd,A.p):fill_rect(A._C.x+round(C+A.p/2),A.C.y-A.Lyh,1,A.Lyh+A.Lyb,Screen.palette[_J])if A.C.x+round(C+A.p/2)>A.C.x-A._Lxg and A.C.x+round(C+A.p/2)<A.C.x+A._Lxd else _D
		for(E,D)in enumerate(range(A._Lxg,0,-A.p)):
			if A.background and A.C.x-A._Lxg+D<A.C.x+A._Lxd:fill_rect(A.C.x-A.Lxg+D,A.C.y-A.Lyh,1,A.Lyh+A.Lyb,Screen.palette[_H])
			if A._C.x-A._Lxg+D<A.C.x+A.Lxd and A._C.y-2>A.C.y-A.Lyh and A._C.y+2<A.C.y+A.Lyb:fill_rect(A.C.x-A.Lxg+D,A._C.y-2,1,5,Screen.palette[_F])
			if A.text and E!=0:draw_string(str(-E),A.C.x-A.Lxg+D-5,A._C.y+10,Screen.palette[_F],Screen.palette[_K])
		for(E,C)in enumerate(range(0,A._Lxd,A.p)):
			if A.background and A._C.x+C<A.C.x+A.Lxd and A._C.x+C>A.C.x-A.Lxg:fill_rect(A._C.x+C,A.C.y-A.Lyh,1,A.Lyh+A.Lyb,Screen.palette[_H])
			if A._C.x+C<A.C.x+A.Lxd and A._C.x+C>A.C.x-A.Lxg and A._C.y-2>A.C.y-A.Lyh and A._C.y+2<A.C.y+A.Lyb:fill_rect(A._C.x+C,A._C.y-2,1,5,Screen.palette[_F])
			if A.text and E!=0:draw_string(str(E),A._C.x+C-5,A._C.y+10,Screen.palette[_F],Screen.palette[_K])
		for(E,D)in enumerate(range(A._Lyh,0,-A.p)):
			if A.background and A.C.y-A._Lyh+D<A.C.y+A._Lyb:fill_rect(A.C.x-A.Lxg,A._C.y-A._Lyh+D,A.Lxg+A.Lxd,1,Screen.palette[_H])
			if A._C.y-A._Lyh+D>A.C.y-A.Lyh and A._C.x-2>A.C.x-A.Lxg and A._C.x+2<A.C.x+A.Lxd and A._C.y-A._Lyh+D<A.C.y+A.Lyb:fill_rect(A._C.x-2,A.C.y-A.Lyh+D,5,1,Screen.palette[_F])
			if A.text and E!=0:draw_string(str(E),A._C.x+10,A.C.y-A.Lyh+D-5,Screen.palette[_F],Screen.palette[_K])
		for(E,C)in enumerate(range(0,A._Lyb,A.p)):
			if A.background and A.C.y+C>A.C.y-A._Lyh and A.C.y+C<A.C.y+A._Lyb:fill_rect(A.C.x-A.Lxg,A._C.y+C,A.Lxg+A.Lxd,1,Screen.palette[_H])
			if A._C.y+C<A.C.y+A.Lyb and A._C.x-2>A.C.x-A.Lxg and A._C.x+2<A.C.x+A.Lxd and A._C.y+C>A.C.y-A.Lyh:fill_rect(A._C.x-2,A._C.y+C,5,1,Screen.palette[_F])
			if A.text and E!=0:draw_string(str(-E),A._C.x+10,A._C.y+C-5,Screen.palette[_F],Screen.palette[_K])
		fill_rect(A._C.x,A.C.y-A.Lyh,1,A.Lyh+A.Lyb,Screen.palette[_F])if A._C.x>=A.C.x-A.Lxg and A._C.x<A.C.x+A.Lxd else _D;fill_rect(A.C.x-A.Lxg,A._C.y,A.Lxg+A.Lxd,1,Screen.palette[_F])if A._C.y>=A.C.y-A.Lyh and A._C.y<A.C.y+A.Lyb else _D
		for B in A.liste_scatter:A.scatter(X=B[_B],Y=B[_C],color=B[_E],style=B[_I])
		for B in A.liste_plot:A.plot(X=B[_B],Y=B[_C],color=B[_E])
		for B in A.liste_point:A.set_points(liste=B[_A],color=B[_E],style=B[_I])
		for B in A.liste_line:A.set_lines(liste=B[_A],color=B[_E])
		for B in A.liste_vector:A.set_vectors(P=B[_A][0],V=Vector(x=B[_A][1].x-B[_A][0].x,y=B[_A][1].y-B[_A][0].y),color=B[_E])
		for B in A.liste_droite:A.set_droite(A=B[_A][0],B=B[_A][1],color=B[_E])
	def zoom(A):
		if keydown(KEY_PLUS):
			for B in A.liste_scatter:C=expend([Point(A,B)for(A,B)in zip(B[_B],B[_C])],-(A.pas/A.p)/100);B[_B]=[A.x for A in C];B[_C]=[A.y for A in C]
			for B in A.liste_plot:C=expend([Point(A,B)for(A,B)in zip(B[_B],B[_C])],-(A.pas/A.p)/100);B[_B]=[A.x for A in C];B[_C]=[A.y for A in C]
			for B in A.liste_point:B[_A]=expend(B[_A],-(A.pas/A.p)/100)
			for B in A.liste_line:B[_A]=expend(B[_A],-(A.pas/A.p)/100)
			for B in A.liste_vector:B[_A]=expend(B[_A],-(A.pas/A.p)/100)
			for B in A.liste_droite:B[_A]=expend(B[_A],-(A.pas/A.p)/100)
			A.p+=A.pas;fill_rect(A.C.x-A.Lxg,A.C.y-A.Lyh,A.Lxg+A.Lxd,A.Lyh+A.Lyb,Screen.palette[_G]);A.set_axes();sleep(.2)
		if keydown(KEY_MINUS):
			for B in A.liste_scatter:C=expend([Point(A,B)for(A,B)in zip(B[_B],B[_C])],A.pas/A.p/100);B[_B]=[A.x for A in C]if A.p-A.pas>1 else B[_B];B[_C]=[A.y for A in C]if A.p-A.pas>1 else B[_C]
			for B in A.liste_plot:C=expend([Point(A,B)for(A,B)in zip(B[_B],B[_C])],A.pas/A.p/100);B[_B]=[A.x for A in C]if A.p-A.pas>1 else B[_B];B[_C]=[A.y for A in C]if A.p-A.pas>1 else B[_C]
			for B in A.liste_point:B[_A]=expend(B[_A],A.pas/A.p/100)if A.p-A.pas>1 else B[_A]
			for B in A.liste_line:B[_A]=expend(B[_A],A.pas/A.p/100)
			for B in A.liste_vector:B[_A]=expend(B[_A],A.pas/A.p/100)
			for B in A.liste_droite:B[_A]=expend(B[_A],A.pas/A.p/100)
			A.p-=A.pas if A.p-A.pas>1 else 0;fill_rect(A.C.x-A.Lxg,A.C.y-A.Lyh,A.Lxg+A.Lxd,A.Lyh+A.Lyb,Screen.palette[_G]);A.set_axes();sleep(.2)
	def scroll(A):
		if keydown(KEY_UP):
			for B in A._liste_scatter:B[_C]=[B+A.pas/A.p for B in B[_C]]
			for B in A._liste_plot:B[_C]=[B+A.pas/A.p for B in B[_C]]
			for B in A._liste_point:B[_A]=[Point(B.x,B.y+A.pas/A.p)for B in B[_A]]
			for B in A._liste_line:B[_A]=[Point(B.x,B.y+A.pas/A.p)for B in B[_A]]
			for B in A._liste_vector:B[_A]=[Point(B.x,B.y+A.pas/A.p)for B in B[_A]]
			for B in A._liste_droite:B[_A]=[Point(B.x,B.y+A.pas/A.p)for B in B[_A]]
			A._C.y+=A.pas;A._Lyh+=A.pas;A._Lyb-=A.pas;fill_rect(A.C.x-A.Lxg,A.C.y-A.Lyh,A.Lxg+A.Lxd,A.Lyh+A.Lyb,Screen.palette[_G]);A.set_axes()
		if keydown(KEY_DOWN):
			for B in A._liste_scatter:B[_C]=[B-A.pas/A.p for B in B[_C]]
			for B in A._liste_plot:B[_C]=[B-A.pas/A.p for B in B[_C]]
			for B in A._liste_point:B[_A]=[Point(B.x,B.y-A.pas/A.p)for B in B[_A]]
			for B in A._liste_line:B[_A]=[Point(B.x,B.y-A.pas/A.p)for B in B[_A]]
			for B in A._liste_vector:B[_A]=[Point(B.x,B.y-A.pas/A.p)for B in B[_A]]
			for B in A._liste_droite:B[_A]=[Point(B.x,B.y-A.pas/A.p)for B in B[_A]]
			A._C.y-=A.pas;A._Lyh-=A.pas;A._Lyb+=A.pas;fill_rect(A.C.x-A.Lxg,A.C.y-A.Lyh,A.Lxg+A.Lxd,A.Lyh+A.Lyb,Screen.palette[_G]);A.set_axes()
		if keydown(KEY_LEFT):
			for B in A._liste_scatter:B[_B]=[B+A.pas/A.p for B in B[_B]]
			for B in A._liste_plot:B[_B]=[B+A.pas/A.p for B in B[_B]]
			for B in A._liste_point:B[_A]=[Point(B.x+A.pas/A.p,B.y)for B in B[_A]]
			for B in A._liste_line:B[_A]=[Point(B.x+A.pas/A.p,B.y)for B in B[_A]]
			for B in A._liste_vector:B[_A]=[Point(B.x+A.pas/A.p,B.y)for B in B[_A]]
			for B in A._liste_droite:B[_A]=[Point(B.x+A.pas/A.p,B.y)for B in B[_A]]
			A._C.x+=A.pas;A._Lxg+=A.pas;A._Lxd-=A.pas;fill_rect(A.C.x-A.Lxg,A.C.y-A.Lyh,A.Lxg+A.Lxd,A.Lyh+A.Lyb,Screen.palette[_G]);A.set_axes()
		if keydown(KEY_RIGHT):
			for B in A._liste_scatter:B[_B]=[B-A.pas/A.p for B in B[_B]]
			for B in A._liste_plot:B[_B]=[B-A.pas/A.p for B in B[_B]]
			for B in A._liste_point:B[_A]=[Point(B.x-A.pas/A.p,B.y)for B in B[_A]]
			for B in A._liste_line:B[_A]=[Point(B.x-A.pas/A.p,B.y)for B in B[_A]]
			for B in A._liste_vector:B[_A]=[Point(B.x-A.pas/A.p,B.y)for B in B[_A]]
			for B in A._liste_droite:B[_A]=[Point(B.x-A.pas/A.p,B.y)for B in B[_A]]
			A._C.x-=A.pas;A._Lxg-=A.pas;A._Lxd+=A.pas;fill_rect(A.C.x-A.Lxg,A.C.y-A.Lyh,A.Lxg+A.Lxd,A.Lyh+A.Lyb,Screen.palette[_G]);A.set_axes()
	def main(A):
		A.set_axes()
		while _L:
			A.zoom();A.scroll()
			if keydown(KEY_BACKSPACE):sleep(.1);break
			if keydown(KEY_ZERO):
				for(B,C)in zip(A._liste_scatter,A.liste_scatter):B[_B]=C[_B].copy();B[_C]=C[_C].copy()
				for(B,C)in zip(A._liste_plot,A.liste_plot):B[_B]=C[_B].copy();B[_C]=C[_C].copy()
				for(B,C)in zip(A._liste_point,A.liste_point):B[_A]=C[_A].copy()
				for(B,C)in zip(A._liste_line,A.liste_line):B[_A]=C[_A].copy()
				for(B,C)in zip(A._liste_vector,A.liste_vector):B[_A]=C[_A].copy()
				for(B,C)in zip(A._liste_droite,A.liste_droite):B[_A]=C[_A].copy()
				A._Lxg,A._Lxd,A._Lyh,A._Lyb=A.Lxg,A.Lxd,A.Lyh,A.Lyb;A._C=Point(A.C.x,A.C.y);fill_rect(A.C.x-A.Lxg,A.C.y-A.Lyh,A.Lxg+A.Lxd,A.Lyh+A.Lyb,Screen.palette[_G]);sleep(.1);A.set_axes()
DefaultGrapher=Grapher(text=_M)
def axes(grapher=DefaultGrapher):grapher.set_axes()
def show(grapher=DefaultGrapher):grapher.main()
def clean(grapher=DefaultGrapher):grapher.clean()
def scatter(*A,grapher=DefaultGrapher,**B):grapher.scatter(*A,**B)
def plot(*A,grapher=DefaultGrapher,**B):grapher.plot(*A,**B)
def points(*A,grapher=DefaultGrapher,**B):grapher.set_points(*A,**B)
def lines(*A,grapher=DefaultGrapher,**B):grapher.set_lines(*A,**B)
def droite(*A,grapher=DefaultGrapher,**B):grapher.set_droite(*A,**B)
def vector(*A,grapher=DefaultGrapher,**B):grapher.set_vectors(*A,**B)