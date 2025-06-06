from visual import Point, bezier_curve, fill_rect
from random import randint
from time import sleep

#   Example 1
A,B,C,D = Point(50,50),Point(100,172),Point(220,50),Point(270,172)

bezier_curve([A,B,C,D], "red", 1, 1500)

#   Example 2
def random_curves(N, color, thickness):
  bezier_curve([Point(randint(10, 310), randint(10, 202)) for _ in range(N)], color, thickness, 2000)

def animation(N, color, thickness):
  while True:
    random_curves(N, color, thickness)
    sleep(0.5)
    fill_rect(0, 0, 320, 222, "white")

#animation(15, "purple", 1)