from visual import Point, fill_triangles

A = Point(150,50,"A")
B = Point(50,120,"B")
C = Point(150,120,"C")
D = Point(250,120,"D")
E = Point(150,185,"E")

fill_triangles([(A, B, C)], (50,50,100))
fill_triangles([(B, C ,E)], (150,150,200))
fill_triangles([(A, C, D)], (100,100,150))
fill_triangles([(C, E, D)], (200,200,250))
