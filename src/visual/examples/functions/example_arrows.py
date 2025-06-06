from ion import keydown, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from visual import Point, Vector, draw_arrows, fill_rect

#   Example 1
A = Point(20, 25)
B = Point(150, 200)
C = Point(120, 25)
D = Point(250, 200)

#draw_arrows([(A, B)], 'orange', fill=False)
#draw_arrows([(C, D)], 'blue', fill=True)

#   Example 2
def animation():
  x, y = 100, 0
  p = 1
  def update():
    fill_rect(0, 0, 320, 222, "w")
    C = Point(160, 111)
    draw_arrows([(C, Vector(x=x, y=y) + C)], "red", 6, 45, True)
  while True: 
    if keydown(KEY_UP): y -= p ; update()
    if keydown(KEY_DOWN): y += p ; update()
    if keydown(KEY_RIGHT): x += p ; update()
    if keydown(KEY_LEFT): x -= p ; update()

print("Move the vector with the arrow !")
animation()