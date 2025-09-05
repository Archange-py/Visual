from visual import Point
from ext_ellipses import draw_ellipses,fill_ellipses
A=Point(50,50)
B=Point(270,172)
def example_1():fill_ellipses(A,B,'red',alpha=.5);draw_ellipses(A,B,'black')
example_1()
A=Point(125,50)
B=Point(195,172)
def example_2():fill_ellipses(A,B,'red',alpha=.5);draw_ellipses(A,B,'black')