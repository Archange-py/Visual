from visual import *

A,B,C,D,E = Point(20,20,'A'),Point(160,111,'B'),Point(20,202,'C'),Point(300,20,'D'),Point(300,202,'E')
F = milieu(D,E);F.round();F.name = 'F'
V,W,Y,X = Vector(A,B,name="V"),Vector(B,C,name="W"),Vector(F,D,name="Y"),Vector(F,E,name="X");U = V+W;U.name = "U"

def example():
  draw_points([A,B,C,D,E,F],"r",style=".")
  draw_rectangle(A,E)
  draw_croix(B,320)
  bezier_curve([A,B,C,E],"orange")
  bezier_curve([E,B,D,A],"orange")
  draw_circle(B,50,"r")
  fill_circle(B,10,"r")
  draw_droite(D,E,"cyan","d'");draw_droite(D,B,"cyan","d''");draw_droite(E,B,"cyan","d'''")
  draw_vector(A,V,"g");draw_vector(B,W,"g");draw_vector(A,U,"g")
  draw_arrows([(F,D)],"blue",fill=True);draw_arrows([(F,E)],"blue",fill=True)
  draw_polygone(6,50,B)
  fill_polygone(6,50,B,"yellow",alpha=0.5)

example()