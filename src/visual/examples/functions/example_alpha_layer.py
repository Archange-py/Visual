from visual import Point, fill_rect, fill_rectangle, fill_circle, fill_polygone

#   Exemple 1
down_color = "red"
up_color = "blue"

def example_1():
  fill_rect(15, 50, 70, 80, down_color)
  fill_rectangle(Point(30, 80), Point(100, 160), up_color, 1)
  fill_rect(15+100, 50, 70, 80, down_color)
  fill_rectangle(Point(130, 80), Point(200, 160), up_color, 0.5)
  fill_rect(15+200, 50, 70, 80, down_color)
  fill_rectangle(Point(230, 80), Point(300, 160), up_color, 0.1)

example_1()

#   Exemple 2
alpha = 0.5

def example_2():
  C1, C2, C3 = Point(100,100), Point(130,100), Point(115,130)
  fill_circle(C1, 30, "magenta", alpha)
  fill_circle(C2, 30, "yellow", alpha)
  fill_circle(C3, 30, "cyan", alpha)

  C1, C2, C3 = Point(200,100), Point(230,100), Point(215,130)
  fill_circle(C3, 30, "blue", alpha)
  fill_circle(C1, 30, "red", alpha)
  fill_circle(C2, 30, "green", alpha)

#example_2()

#   Example 3
alpha = 0

C = Point(160,110)

def animation():
    global alpha
    while alpha <= 1:
      fill_rect(0,0,320,222,"white")
      fill_polygone(5, 100, C, color="red", alpha=alpha)
      alpha += 0.1

#animation()