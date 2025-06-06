from visual import Point
from ext_ellipses import draw_ellipses, fill_ellipses

#   Example 1
A = Point(50, 50)
B = Point(320 - 50, 222 - 50)

def example_1():
  fill_ellipses(A, B, 'red', alpha=0.5)
  draw_ellipses(A, B, 'black')

example_1()

#   Example 2
A = Point(125, 50)
B = Point(320 - 125, 222 - 50)

def example_2():
  fill_ellipses(A, B, 'red', alpha=0.5)
  draw_ellipses(A, B, 'black')

#example_2()