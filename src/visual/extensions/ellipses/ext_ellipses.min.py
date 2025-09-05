from visual import Point,set_pixel,alpha_pixel
def draw_ellipses(P1,P2,color='0'):
	D=color;B=P2;A=P1;C,E=abs(B.x-A.x),abs(B.y-A.y);F=E&1;H,G=4*(1-C)*E*E,4*(F+1)*C*C;I=H+G+F*C*C
	if A.x>B.x:A.x,B.x=B.x,A.x+C
	if A.y>B.y:A.y=B.y
	A.y+=(E+1)//2;B.y=A.y-F;C*=8*C;F=8*E*E
	while A.x<=B.x:
		set_pixel(B.x,A.y,D);set_pixel(A.x,A.y,D);set_pixel(A.x,B.y,D);set_pixel(B.x,B.y,D);J=2*I
		if J<=G:A.y+=1;B.y-=1;I+=G;G+=C
		if J>=H or 2*I>G:A.x+=1;B.x-=1;I+=H;H+=F
	while A.y-B.y<E:set_pixel(A.x-1,A.y,D);set_pixel(B.x+1,A.y,D);set_pixel(A.x-1,B.y,D);set_pixel(B.x+1,B.y,D);A.y+=1;B.y-=1
def fill_ellipses(P1,P2,color='0',alpha=1.):
	A,B,C=abs(P2.x-P1.x)//2,abs(P2.y-P1.y)//2,Point((P1.x+P2.x)//2,(P1.y+P2.y)//2)
	for(D,E)in[(A,C)for A in range(-A,A+1)for C in range(-B,B+1)]:alpha_pixel(C.x+D,C.y+E,color,alpha)if D**2/A**2+E**2/B**2<=1 else None