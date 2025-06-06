from visual import Point, expend, fill_rect, bezier_curve
from random import randint
from time import sleep

#   Example 1
A,B,C,D = Point(0,0),Point(320,0),Point(320,222),Point(0,222)

def animation_1(color):
  n = 0
  while n > -0.8:
    fill_rect(0, 0, 320, 222, "white")
    bezier_curve(expend([A,B,C,D,A,B], n), color)
    sleep(0.1)
    n -= 0.1

animation_1("green")

#   Example 2
A,B,C,D,E = Point(50,50),Point(100,200),Point(150,50),Point(200,200),Point(250,50)

def animation_2(color):
  n = 0
  while n > -1:
    fill_rect(0, 0, 320, 222, "white")
    bezier_curve(expend([A,B,C,D,E], n), color)
    sleep(0.1)
    n -= 0.1

#animation_2("green")

#   Example 3

def animation_3(color):
  while True:
    liste = [Point(randint(0, 320), randint(0, 222)) for _ in range(10)]
    n = 0
    while n > -1:
      fill_rect(0, 0, 320, 222, "white")
      bezier_curve(expend(liste, n), color)
      sleep(0.1)
      n -= 0.1

#animation_3("green")