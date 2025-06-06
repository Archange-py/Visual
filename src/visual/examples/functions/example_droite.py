from ion import keydown, KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT
from visual import Point, draw_droite, fill_rect

#   Example 1
A, B, C, D = Point(120, 70, "A"), Point(180, 30, "B"), Point(100, 150, "C"), Point(230, 140, "D")

def example_1(color):
  draw_droite(A, B, color, "D1")
  draw_droite(A, C, color, "D2")
  draw_droite(C, D, color, "D3")
  draw_droite(B, D, color, "D4")

example_1("red")

#   Example 2
A, B, C, D = Point(100, 50, "A"), Point(200, 50, "B"), Point(100, 150, "C"), Point(200, 150, "D")

def example_2(color):
  draw_droite(A, B, color, "D1")
  draw_droite(A, C, color, "D2")
  draw_droite(C, D, color, "D3")
  draw_droite(B, D, color, "D4")

#example_2("red")

#   Example 3

def animation_3(color):
  print("Move the line with the arrow !")
  A = Point(150, 50)
  x, y = 200, 200
  t = 5
  def update():
      fill_rect(0, 0, 320, 222, "white")
      draw_droite(A, Point(x, y), color)
      fill_rect(x-1, y-1, 3, 3, "black")
      fill_rect(A.x-1, A.y-1, 3, 3, "black")
  update()
  while True:
    if keydown(KEY_UP): y -= t ; update()
    if keydown(KEY_DOWN): y += t ; update()
    if keydown(KEY_RIGHT): x += t ; update()
    if keydown(KEY_LEFT): x -= t ; update()

#animation_3("red")
