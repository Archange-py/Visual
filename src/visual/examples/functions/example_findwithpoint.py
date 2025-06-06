from visual import Point, findWithPoint, set_lines, fill_rect
from ion import keydown, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

#   Example 1
A = Point(160,111)
x,y = 260,111
l,t = 25,3

def update():
  fill_rect(0,0,320,222,"white")
  B = findWithPoint(A,Point(x,y),l)
  B.round()
  set_lines([(A,B)],"red")
  fill_rect(A.x-1,A.y-1,3,3,"black")
  fill_rect(x-1,y-1,3,3,"black")

print("Move the line with the arrow !")

update()

while True:
  if keydown(KEY_UP): y -= t ; update()
  if keydown(KEY_DOWN): y += t ; update()
  if keydown(KEY_RIGHT): x += t ; update()
  if keydown(KEY_LEFT): x -= t ; update()