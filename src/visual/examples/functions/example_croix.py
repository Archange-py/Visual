from visual import Point, draw_croix, draw_circle

#   Example 1
O = Point(160, 111)

draw_circle(O, 100, "black")

a = 0
while True:
  draw_croix(O, 99, 45+a, 'red')
  draw_croix(O, 99, 90+a, 'orange')

  draw_croix(O, 99, 45+a, 'white')
  draw_croix(O, 99, 90+a, 'white')

  a += 5