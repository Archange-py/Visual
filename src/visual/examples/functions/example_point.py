from visual import Point, draw_points, DrawWithStyle

#   Example 1
print(list(DrawWithStyle.keys()))

def exemple(P: Point, color: tuple | str):
  for s in DrawWithStyle.keys(): 
    draw_points([P], color, style=s)
    P.x += 20

exemple(Point(135,80),"green")
exemple(Point(135,110),"red")
exemple(Point(135,140),"blue")