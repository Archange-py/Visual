from visual import interpolate, fill_rect
from kandinsky import color

def draw_interpolate(C1: tuple | str, C2: tuple | str, N: int, position: tuple = (0, 0), taille: int = 1):
  colors_interpolate = interpolate(C1, C2, N)
  for n, col in enumerate(colors_interpolate):
    fill_rect(position[0]+n*taille, position[1], taille, taille, color(col))
  del colors_interpolate

#   Exemple 1

def example_1():
  for y in range(222):
    draw_interpolate((255,255,0), (255,0,0), N=320, position=(0, y), taille=1)

example_1()

#   Exemple 2

def example_2():
  for y in range(222):
    draw_interpolate((255,255,0), (0,255,255), N=320, position=(0, y), taille=1)

#example_2()

#   Exemple 3

def example_3():
  for y in range(0, 111):
    draw_interpolate((255,255,255), (0,255,255), N=320, position=(0, y), taille=1)
  for y in range(111, 222):
    draw_interpolate((0,255,255), (255,255,255), N=320, position=(0, y), taille=1)

#example_3()

#   Exemple 4

def example_4():
  for y in range(222):
    C1 = (255 - y, 255 - y, 255 - y)
    C2 = (255 - y, 0 + y, 0 + y)
    draw_interpolate(C1, C2, N=320, position=(0, y), taille=1)

#example_4()