from visual import Point, scatter, DrawWithStyle
from random import randint
from math import sin

print(list(DrawWithStyle.keys()))

#   Example 1
X = [3, 29, 55, 81, 108, 133, 160]
Y = [109, 144, 160, 161, 148, 122, 78]

scatter(X, Y, "red", "O", C=Point(50,200))

#   Example 2
X = [x for x in range(-100, 100, 5)]
Y = [sin(y*25)*30 for y in range(-100, 100, 5)]

#scatter(X, Y, "red", "*", C=Point(160,111))

#   Example 3
X = [randint(-100, 80) for _ in range(-100, 100, 10)]
Y = [randint(-100, 80) for _ in range(-100, 100, 10)]

#scatter(X, Y, "red", "+", C=Point(160,111))

#   Example 4
X = [x for x in range(-100, 100, 3)]
Y = [sin(y*25)*30 for y in range(-100, 100, 3)]

#scatter(X, Y, "red", ".", C=Point(160,111))