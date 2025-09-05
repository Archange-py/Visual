_A=True
from visual import Point,set_pixel,fill_circle,interpolate,distance
def draw_lines(line,color='0',thickness=1):
	L=thickness;K=color;J=False
	if isinstance(K,list):
		for((A,C),(M,N))in zip(line,K):
			H,I=_A if C.y>A.y else J,_A if C.x>A.x else J;D,E=C.y-A.y if H else A.y-C.y,C.x-A.x if I else A.x-C.x;F=_A if D<=E else J;G=D/E if F and(E!=0 or D!=0)else E/D;O=interpolate(M,N,round(distance(A,C)))
			for B in range(E if F else D):fill_circle(Point(int(round(A.x+B)if I else round(A.x-B))if F else int(round(A.x+G*B)if I else round(A.x-G*B)),int(round(A.y+G*B)if H else round(A.y-G*B))if F else int(round(A.y+B)if H else round(A.y-B))),L,O[B])
	else:
		for(A,C)in line:
			H,I=_A if C.y>A.y else J,_A if C.x>A.x else J;D,E=C.y-A.y if H else A.y-C.y,C.x-A.x if I else A.x-C.x;F=_A if D<=E else J;G=D/E if F and(E!=0 or D!=0)else E/D
			for B in range(E if F else D):fill_circle(Point(int(round(A.x+B)if I else round(A.x-B))if F else int(round(A.x+G*B)if I else round(A.x-G*B)),int(round(A.y+G*B)if H else round(A.y-G*B))if F else int(round(A.y+B)if H else round(A.y-B))),L,K)
def draw_lines_AA(line):
	for(A,E)in line:
		B,C,H,I=abs(E.x-A.x),abs(E.y-A.y),1 if A.x<E.x else-1,1 if A.y<E.y else-1;G,D,J,F=B-C,0,0,1 if B+C==0 else(B*B+C*C)**.5
		while _A:
			set_pixel(A.x,A.y,tuple(int(255*abs(G-B+C)/F)for A in range(3)));D,J=G,A.x
			if 2*D>=-B:
				if A.x==E.x:break
				if D+C<F:set_pixel(A.x,A.y+I,tuple(int(255*(D+C)/F)for A in range(3)))
				G-=C;A.x+=H
			if 2*D<=C:
				if A.y==E.y:break
				if B-D<F:set_pixel(J+H,A.y,tuple(int(255*(B-D)/F)for A in range(3)))
				G+=B;A.y+=I