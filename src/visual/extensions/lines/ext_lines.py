from visual import Point, set_pixel, fill_circle, interpolate, distance
def draw_lines(line,color='0',thickness=1):
  if isinstance(color,list):
    for (P1,P2),(C1,C2) in zip(line,color):
      up,right=True if P2.y>P1.y else False,True if P2.x>P1.x else False;h,b=P2.y-P1.y if up else P1.y-P2.y,P2.x-P1.x if right else P1.x-P2.x;n=True if h<=b else False;e=h/b if n and (b!=0 or h!=0) else b/h;colors=interpolate(C1,C2,round(distance(P1,P2)))
      for i in range(b if n else h):fill_circle(Point(int(round(P1.x+i) if right else round(P1.x-i))if n else int(round(P1.x+e*i) if right else round(P1.x-e*i)),int(round(P1.y+e*i) if up else round(P1.y-e*i))if n else int(round(P1.y+i) if up else round(P1.y-i))),thickness,colors[i])
  else:
    for (P1,P2) in line:
      up,right=True if P2.y>P1.y else False,True if P2.x>P1.x else False;h,b=P2.y-P1.y if up else P1.y-P2.y,P2.x-P1.x if right else P1.x-P2.x;n=True if h<=b else False;e=h/b if n and (b!=0 or h!=0) else b/h
      for i in range(b if n else h):fill_circle(Point(int(round(P1.x+i) if right else round(P1.x-i))if n else int(round(P1.x+e*i) if right else round(P1.x-e*i)),int(round(P1.y+e*i) if up else round(P1.y-e*i))if n else int(round(P1.y+i) if up else round(P1.y-i))),thickness,color)
def draw_lines_AA(line):
    for P1,P2 in line:
      dx,dy,sx,sy=abs(P2.x-P1.x),abs(P2.y-P1.y),1 if P1.x<P2.x else -1,1 if P1.y<P2.y else -1;err,e2,x2,ed=dx-dy,0,0,1 if dx+dy==0 else (dx*dx+dy*dy)**0.5
      while True:
        set_pixel(P1.x,P1.y,tuple(int(255*abs(err-dx+dy)/ed) for _ in range(3)));e2,x2=err,P1.x
        if 2*e2>=-dx:
          if P1.x==P2.x:break
          if e2+dy<ed:set_pixel(P1.x,P1.y+sy,tuple(int(255*(e2+dy)/ed) for _ in range(3)))
          err-=dy;P1.x+=sx
        if 2*e2<=dy:
          if P1.y==P2.y:break
          if dx-e2<ed:set_pixel(x2+sx,P1.y,tuple(int(255*(dx-e2)/ed) for _ in range(3)))
          err+=dx;P1.y+=sy