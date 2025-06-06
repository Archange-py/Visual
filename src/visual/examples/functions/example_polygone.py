from visual import Point, draw_polygone, fill_polygone

C = Point(160,110)

c_map = [
    (50,  50,  100),
    (120, 120, 170),
    (170, 170, 220),
    (190, 190, 240),
    (200, 200, 250)
]

fill_polygone(5, 100, C, color="green")
fill_polygone(5, 100, C, c_map=c_map)
draw_polygone(5, 100, C)