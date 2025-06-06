from visual import Point, plot
from random import randint
from math import sin

#   Example 1
X = [x for x in range(320)]
Y = [sin(y*25)*30 for y in range(320)]

plot(X, Y, 'red', Point(0,111))

#   Example 2
X = [x for x in range(-160, 160)]
Y = [randint(-100, 100) for _ in range(-160, 160)]

#plot(X, Y, 'green')

#   Example 3
X = [x for x in range(-160, 160)]
Y = [(1*y**2+1*y)/80 for y in range(-160, 160)]

#plot(X, Y, 'blue', C=Point(160, 200))