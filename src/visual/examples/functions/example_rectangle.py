from visual import Point, fill_rect, fill_rectangle, draw_rectangle

#   Example 1
A = Point(50, 50)
B = Point(50 + 100, 50 + 100)
C = Point(100, 100)

def example_1():
  fill_rect(50, 50, 100, 100, "green")
  fill_rectangle(A, C, "blue", alpha=0.5)
  fill_rectangle(C, B, "orange", alpha=0.5)
  draw_rectangle(A, B, "black")

example_1()