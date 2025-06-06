from visual import Point, set_pixel, alpha_pixel
def draw_ellipses(P1,P2,color='0'):
    a,b=abs(P2.x-P1.x),abs(P2.y-P1.y);b1=b&1;dx,dy=4*(1-a)*b*b,4*(b1+1)*a*a;err=dx+dy+b1*a*a
    if P1.x>P2.x:P1.x,P2.x=P2.x,P1.x+a
    if P1.y>P2.y:P1.y=P2.y
    P1.y+=(b+1)//2;P2.y=P1.y-b1;a*=8*a;b1=8*b*b
    while P1.x<=P2.x:
      set_pixel(P2.x,P1.y,color);set_pixel(P1.x,P1.y,color);set_pixel(P1.x,P2.y,color);set_pixel(P2.x,P2.y,color);e2=2*err
      if e2<=dy:P1.y+=1;P2.y-=1;err+=dy;dy+=a
      if e2>=dx or 2*err>dy:P1.x+=1;P2.x-=1;err+=dx;dx+=b1
    while P1.y-P2.y<b:set_pixel(P1.x-1,P1.y,color);set_pixel(P2.x+1,P1.y,color);set_pixel(P1.x-1,P2.y,color);set_pixel(P2.x+1,P2.y,color);P1.y+=1;P2.y-=1
def fill_ellipses(P1,P2,color='0',alpha=1.0):
  a,b,C=abs(P2.x-P1.x)//2,abs(P2.y-P1.y)//2,Point((P1.x+P2.x)//2,(P1.y+P2.y)//2)
  for x,y in [(x,y) for x in range(-a,a+1) for y in range(-b,b+1)]:alpha_pixel(C.x+x,C.y+y,color,alpha) if (x**2/a**2)+(y**2/b**2)<=1 else None