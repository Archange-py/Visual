from visual import Point, Vector, draw_vector

A = Point(50, 50, "A")
B = Point(150, 50, "B")
C = Point(250, 50, "C")
D = Point(50, 120, "D")
E = Point(150, 120, "E")
F = Point(250, 120, "F")
G = Point(50, 185, "G")
H = Point(250, 185, "H")

BA = Vector(B, A, name="BA")
DE = Vector(D, E, name="DE")
CF = Vector(C, F, name="CF")
GD = Vector(G, D, name="GD")
AH = Vector(A, H, name="AH")

BD = BA - GD
BD.name = "BD"

for P,V in zip([B, D, C, G, A, E],[BA, DE, CF, GD, AH, BD]):
  draw_vector(P, V, color='purple')
