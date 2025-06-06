from visual import Point,Vector,fill_rect,draw_string,draw_points,set_lines,draw_vector,expend,connect_points
from ion import keydown,KEY_UP,KEY_DOWN,KEY_RIGHT,KEY_LEFT,KEY_MINUS,KEY_PLUS,KEY_BACKSPACE,KEY_ZERO
from time import sleep

class Screen: p,center,width,height,palette = 3,Point(160, 111),320,222,{"Background":(248,252,248),"PrimaryColor":(0,0,0),"SecondaryColor":(200,200,200),"PrimaryText":(0,0,0),"SecondaryText":(248,252,248),"PrimaryColor":(0,0,0),"SecondaryColor":(200,200,200),"ThirdColor":(235,235,235)}

class Grapher:
  def __init__(self, p: int = 45, Lxg: int = round(Screen.width/2), Lxd: int = round(Screen.width/2), Lyh: int = round(Screen.height/2), Lyb: int = round(Screen.height/2), C: Point = Screen.center, text: bool = True, background: bool = True, color1 : str | tuple = Screen.palette["PrimaryColor"], color2 : str | tuple = Screen.palette["SecondaryColor"], color3 : str | tuple = Screen.palette["ThirdColor"], pas: int = None):
    Screen.palette["PrimaryColor"],Screen.palette["SecondaryColor"],Screen.palette["ThirdColor"] = color1,color2,color3
    self.p,self.Lxg,self.Lxd,self.Lyh,self.Lyb,self._Lxg,self._Lxd,self._Lyh,self._Lyb,self.C,self._C,self.text,self.background,self.pas = p,Lxg,Lxd,Lyh,Lyb,Lxg,Lxd,Lyh,Lyb,Point(C.x,C.y),Point(C.x,C.y),text,background,round(p/5) if pas == None else pas
    self._liste_scatter,self._liste_plot,self._liste_point,self._liste_line,self._liste_droite,self._liste_vector,self.liste_scatter,self.liste_plot,self.liste_point,self.liste_line,self.liste_droite,self.liste_vector = [],[],[],[],[],[],[],[],[],[],[],[]

  def check(self, x: int, y: int) -> bool: return round(self._C.x+x*self.p) > self.C.x-self.Lxg+Screen.p and round(self._C.x+x*self.p) < self.C.x+self.Lxd-Screen.p and round(self._C.y-y*self.p) > self.C.y-self.Lyh+Screen.p and round(self._C.y-y*self.p) < self.C.y+self.Lyb-Screen.p

  def find_intersections(self, P0: Point, P1: Point, segments: list[tuple[Point,Point]], droite: bool = False) -> list[Point | None]:
    def intersect_segments(P0: Point, P1: Point, A: Point, B: Point) -> Point | None:
      d,AB = Point(P1.x-P0.x,P1.y-P0.y),Point(B.x-A.x,B.y-A.y);denominator = d.x*AB.y-d.y*AB.x
      if denominator == 0: return None
      t,u = ((A.x-P0.x)*AB.y-(A.y-P0.y)*AB.x)/denominator,((A.x-P0.x)*d.y-(A.y-P0.y)*d.x)/denominator
      if not droite and 0 <= t <= 1 and 0 <= u <= 1: intersection_point = Point(P0.x+t*d.x,P0.y+t*d.y);return intersection_point
      elif droite and 0 <= u <= 1: intersection_point = Point(P0.x+t*d.x,P0.y+t*d.y);return intersection_point
      return None
    return [intersect_segments(P0,P1,A,B) for A,B in segments]

  def scatter(self, X: list[Point], Y: list[Point], color: str | tuple = Screen.palette["PrimaryColor"], style: str = "O"):
    if len(X) != len(Y): raise TypeError("Liste X an Y must have the same size")
    if not {"X":X,"Y":Y,"color":color,"style":style} in self.liste_scatter: self._liste_scatter.append({"X":X,"Y":Y,"color":color,"style":style});self.liste_scatter.append({"X":X,"Y":Y,"color":color,"style":style})
    else: draw_points([Point(round(self._C.x+x*self.p), round(self._C.y-y*self.p)) for x, y in zip(X, Y) if self.check(x,y)], color, style, False)

  def plot(self, X: list[Point], Y: list[Point], color: str | tuple = Screen.palette["PrimaryColor"]):
    if len(X) != len(Y): raise TypeError("Liste X an Y must have the same size")
    if not {"X":X,"Y":Y,"color":color} in self.liste_plot: self._liste_plot.append({"X":X,"Y":Y,"color":color});self.liste_plot.append({"X":X,"Y":Y,"color":color})
    else:
      SEGMENTS = [(Point(self.C.x-self.Lxd,self.C.y-self.Lyb),Point(self.C.x+self.Lxg,self.C.y-self.Lyb)),(Point(self.C.x-self.Lxd,self.C.y+self.Lyh),Point(self.C.x+self.Lxg,self.C.y+self.Lyh)),(Point(self.C.x-self.Lxd,self.C.y-self.Lyb),Point(self.C.x-self.Lxd,self.C.y+self.Lyh)),(Point(self.C.x+self.Lxg,self.C.y-self.Lyb),Point(self.C.x+self.Lxg,self.C.y+self.Lyh))]
      POINTS = [Point(round(self._C.x+x*self.p), round(self._C.y-y*self.p)) for x, y in zip(X, Y) if round(self._C.x+x*self.p) > self.C.x-self.Lxg and round(self._C.x+x*self.p) < self.C.x+self.Lxd and round(self._C.y-y*self.p) > self.C.y-self.Lyh and round(self._C.y-y*self.p) < self.C.y+self.Lyb]
      for (P1,P2) in connect_points([Point(round(self._C.x+x*self.p),round(self._C.y-y*self.p)) for x,y in zip(X, Y)]):
        intersections = self.find_intersections(P1,P2,SEGMENTS);intersec = [Point(round(P.x),round(P.y)) for P in intersections if P != None];l = len(intersec)
        if l == 2: set_lines([(intersec[0],intersec[1])],color)
        elif l == 1 and intersections[0] != None: set_lines([(P1,intersec[0])],color) if P1.y >= intersec[0].y else set_lines([(intersec[0],P2)],color)
        elif l == 1 and intersections[1] != None: set_lines([(P1,intersec[0])],color) if P1.y <= intersec[0].y else set_lines([(intersec[0],P2)],color)
        elif l == 1 and intersections[2] != None: set_lines([(P1,intersec[0])],color) if P1.x >= intersec[0].x else set_lines([(intersec[0],P2)],color)
        elif l == 1 and intersections[3] != None: set_lines([(P1,intersec[0])],color) if P1.x <= intersec[0].x else set_lines([(intersec[0],P2)],color)
        elif P1 in POINTS: set_lines([(P1,P2)],color)
      fill_rect(self.C.x-self.Lxg,self.C.y+self.Lyh,self.Lxd+self.Lxg,1,Screen.palette["Background"]);fill_rect(self.C.x+self.Lxg,self.C.y-self.Lyb,1,self.Lyb+self.Lyh,Screen.palette["Background"])

  def set_points(self, liste: list[Point], color: str | tuple = Screen.palette["PrimaryColor"], style: str = "O"):
    if not {"liste":liste,"color":color,"style":style} in self.liste_point: self._liste_point.append({"liste":liste,"color":color,"style":style});self.liste_point.append({"liste":liste,"color":color,"style":style})
    else: draw_points([Point(round(self._C.x+P.x*self.p), round(self._C.y-P.y*self.p)) for P in liste if self.check(P.x,P.y)], color, style, False)

  def set_lines(self, liste: list[Point], color: str | tuple = Screen.palette["PrimaryColor"]):
    if not {"liste":liste,"color":color} in self.liste_line: self._liste_line.append({"liste":liste,"color":color});self.liste_line.append({"liste":liste,"color":color})
    else:
      SEGMENTS = [(Point(self.C.x-self.Lxd,self.C.y-self.Lyb),Point(self.C.x+self.Lxg,self.C.y-self.Lyb)),(Point(self.C.x-self.Lxd,self.C.y+self.Lyh),Point(self.C.x+self.Lxg,self.C.y+self.Lyh)),(Point(self.C.x-self.Lxd,self.C.y-self.Lyb),Point(self.C.x-self.Lxd,self.C.y+self.Lyh)),(Point(self.C.x+self.Lxg,self.C.y-self.Lyb),Point(self.C.x+self.Lxg,self.C.y+self.Lyh))]
      LINES = connect_points([Point(round(self._C.x+P.x*self.p), round(self._C.y-P.y*self.p)) for P in liste if round(self._C.x+P.x*self.p) > self.C.x-self.Lxg and round(self._C.x+P.x*self.p) < self.C.x+self.Lxd and round(self._C.y-P.y*self.p) > self.C.y-self.Lyh and round(self._C.y-P.y*self.p) < self.C.y+self.Lyb])
      for (P1,P2) in connect_points([Point(round(self._C.x+P.x*self.p),round(self._C.y-P.y*self.p)) for P in liste]):
        intersections = self.find_intersections(P1,P2,SEGMENTS);intersec = [Point(round(P.x),round(P.y)) for P in intersections if P != None];l = len(intersec)
        if l == 2: set_lines([(intersec[0],intersec[1])],color)
        elif l == 1 and intersections[0] != None: set_lines([(P1,intersec[0])],color) if P1.y >= intersec[0].y else set_lines([(intersec[0],P2)],color)
        elif l == 1 and intersections[1] != None: set_lines([(P1,intersec[0])],color) if P1.y <= intersec[0].y else set_lines([(intersec[0],P2)],color)
        elif l == 1 and intersections[2] != None: set_lines([(P1,intersec[0])],color) if P1.x >= intersec[0].x else set_lines([(intersec[0],P2)],color)
        elif l == 1 and intersections[3] != None: set_lines([(P1,intersec[0])],color) if P1.x <= intersec[0].x else set_lines([(intersec[0],P2)],color)
        elif (P1,P2) in LINES: set_lines([(P1,P2)],color)
      fill_rect(self.C.x-self.Lxg,self.C.y+self.Lyh,self.Lxd+self.Lxg+1,1,Screen.palette["Background"]);fill_rect(self.C.x+self.Lxg,self.C.y-self.Lyb,1,self.Lyb+self.Lyh,Screen.palette["Background"])

  def set_vectors(self, P: Point, V: Vector, color: str | tuple = Screen.palette["PrimaryColor"]):
    if not {"liste":[P,V+P],"color":color} in self.liste_vector: self._liste_vector.append({"liste":[P,V+P],"color":color});self.liste_vector.append({"liste":[P,V+P],"color":color})
    else:
      SEGMENTS = [(Point(self.C.x-self.Lxd,self.C.y-self.Lyb),Point(self.C.x+self.Lxg,self.C.y-self.Lyb)),(Point(self.C.x-self.Lxd,self.C.y+self.Lyh),Point(self.C.x+self.Lxg,self.C.y+self.Lyh)),(Point(self.C.x-self.Lxd,self.C.y-self.Lyb),Point(self.C.x-self.Lxd,self.C.y+self.Lyh)),(Point(self.C.x+self.Lxg,self.C.y-self.Lyb),Point(self.C.x+self.Lxg,self.C.y+self.Lyh))]
      LINES = connect_points([Point(round(self._C.x+P.x*self.p), round(self._C.y-P.y*self.p)) for P in [P,V+P] if round(self._C.x+P.x*self.p) > self.C.x-self.Lxg and round(self._C.x+P.x*self.p) < self.C.x+self.Lxd and round(self._C.y-P.y*self.p) > self.C.y-self.Lyh and round(self._C.y-P.y*self.p) < self.C.y+self.Lyb])
      for (P1,P2) in connect_points([Point(round(self._C.x+P.x*self.p),round(self._C.y-P.y*self.p)) for P in [P,V+P]]):
        intersections = self.find_intersections(P1,P2,SEGMENTS);intersec = [Point(round(P.x),round(P.y)) for P in intersections if P != None];l = len(intersec)
        if l == 2: set_lines([(intersec[0],intersec[1])],color)
        elif l == 1 and intersections[0] != None: set_lines([(P1,intersec[0])],color) if P1.y >= intersec[0].y else draw_vector(intersec[0],Vector(x=P2.x-intersec[0].x,y=P2.y-intersec[0].y),color)
        elif l == 1 and intersections[1] != None: set_lines([(P1,intersec[0])],color) if P1.y <= intersec[0].y else draw_vector(intersec[0],Vector(x=P2.x-intersec[0].x,y=P2.y-intersec[0].y),color)
        elif l == 1 and intersections[2] != None: set_lines([(P1,intersec[0])],color) if P1.x >= intersec[0].x else draw_vector(intersec[0],Vector(x=P2.x-intersec[0].x,y=P2.y-intersec[0].y),color)
        elif l == 1 and intersections[3] != None: set_lines([(P1,intersec[0])],color) if P1.x <= intersec[0].x else draw_vector(intersec[0],Vector(x=P2.x-intersec[0].x,y=P2.y-intersec[0].y),color)
        elif (P1,P2) in LINES: draw_vector(P1,Vector(x=P2.x-P1.x,y=P2.y-P1.y),color)
      fill_rect(self.C.x-self.Lxg,self.C.y+self.Lyh,self.Lxd+self.Lxg+1,1,Screen.palette["Background"]);fill_rect(self.C.x+self.Lxg,self.C.y-self.Lyb,1,self.Lyb+self.Lyh,Screen.palette["Background"])

  def set_droite(self, A: Point, B: Point, color: str | tuple = Screen.palette["PrimaryColor"]):
    if not {"liste":[A,B],"color":color} in self.liste_droite: self._liste_droite.append({"liste":[A,B],"color":color});self.liste_droite.append({"liste":[A,B],"color":color})
    else:
      SEGMENTS = [(Point(self.C.x-self.Lxd,self.C.y-self.Lyb),Point(self.C.x+self.Lxg,self.C.y-self.Lyb)),(Point(self.C.x-self.Lxd,self.C.y+self.Lyh),Point(self.C.x+self.Lxg,self.C.y+self.Lyh)),(Point(self.C.x-self.Lxd,self.C.y-self.Lyb),Point(self.C.x-self.Lxd,self.C.y+self.Lyh)),(Point(self.C.x+self.Lxg,self.C.y-self.Lyb),Point(self.C.x+self.Lxg,self.C.y+self.Lyh))]
      for (P1,P2) in connect_points([Point(round(self._C.x+P.x*self.p),round(self._C.y-P.y*self.p)) for P in [A,B]]):
        intersections = self.find_intersections(P1,P2,SEGMENTS,True);intersec = [Point(round(P.x),round(P.y)) for P in intersections if P != None];set_lines([(intersec[0],intersec[1])],color) if len(intersec) == 2 else None
      fill_rect(self.C.x-self.Lxg,self.C.y+self.Lyh,self.Lxd+self.Lxg+1,1,Screen.palette["Background"]);fill_rect(self.C.x+self.Lxg,self.C.y-self.Lyb,1,self.Lyb+self.Lyh,Screen.palette["Background"])

  def clean(self): self._liste_scatter,self._liste_plot,self._liste_point,self._liste_line,self._liste_droite,self._liste_vector,self.liste_scatter,self.liste_plot,self.liste_point,self.liste_line,self.liste_droite,self.liste_vector = [],[],[],[],[],[],[],[],[],[],[],[] ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()

  def set_axes(self):
    if self.background:
      for i in range(self._Lyh,0,-self.p): fill_rect(self.C.x-self.Lxg,self._C.y-self._Lyh+round(i-self.p/2),self.Lxg+self.Lxd,1,Screen.palette["ThirdColor"]) if self.C.y-self._Lyh+round(i-self.p/2) > self.C.y-self._Lyh and self.C.y-self._Lyh+round(i-self.p/2) < self.C.y+self._Lyb else None
      for j in range(0,self._Lyb,self.p): fill_rect(self.C.x-self.Lxg,self._C.y+round(j+self.p/2),self.Lxg+self.Lxd,1,Screen.palette["ThirdColor"]) if self.C.y+round(j+self.p/2) > self.C.y-self._Lyh and self.C.y+round(j+self.p/2) < self.C.y+self._Lyb else None
      for i in range(self._Lxg,0,-self.p): fill_rect(self._C.x-self._Lxg+round(i-self.p/2),self.C.y-self.Lyh,1,self.Lyh+self.Lyb,Screen.palette["ThirdColor"]) if self.C.x-self._Lxg+round(i-self.p/2) > self.C.x-self._Lxg and self.C.x-self._Lxg+round(i-self.p/2) < self.C.x+self._Lxd else None
      for j in range(0,self._Lxd,self.p): fill_rect(self._C.x+round(j+self.p/2),self.C.y-self.Lyh,1,self.Lyh+self.Lyb,Screen.palette["ThirdColor"]) if self.C.x+round(j+self.p/2) > self.C.x-self._Lxg and self.C.x+round(j+self.p/2) < self.C.x+self._Lxd else None
    for n,i in enumerate(range(self._Lxg,0,-self.p)):
      if self.background and self.C.x-self._Lxg+i < self.C.x+self._Lxd: fill_rect(self.C.x-self.Lxg+i,self.C.y-self.Lyh,1,self.Lyh+self.Lyb,Screen.palette["SecondaryColor"])
      if self._C.x-self._Lxg+i < self.C.x+self.Lxd and self._C.y-2 > self.C.y-self.Lyh and self._C.y+2 < self.C.y+self.Lyb: fill_rect(self.C.x-self.Lxg+i,self._C.y-2,1,5,Screen.palette["PrimaryColor"])
      if self.text and n != 0: draw_string(str(-n),self.C.x-self.Lxg+i-5,self._C.y+10,Screen.palette["PrimaryColor"],Screen.palette["SecondaryText"])
    for n,j in enumerate(range(0,self._Lxd,self.p)):
      if self.background and self._C.x+j < self.C.x+self.Lxd and self._C.x+j > self.C.x-self.Lxg: fill_rect(self._C.x+j,self.C.y-self.Lyh,1,self.Lyh+self.Lyb,Screen.palette["SecondaryColor"])
      if self._C.x+j < self.C.x+self.Lxd and self._C.x+j > self.C.x-self.Lxg and self._C.y-2 > self.C.y-self.Lyh and self._C.y+2 < self.C.y+self.Lyb: fill_rect(self._C.x+j,self._C.y-2,1,5,Screen.palette["PrimaryColor"])
      if self.text and n != 0: draw_string(str(n),self._C.x+j-5,self._C.y+10,Screen.palette["PrimaryColor"],Screen.palette["SecondaryText"])
    for n,i in enumerate(range(self._Lyh,0,-self.p)):
      if self.background and self.C.y-self._Lyh+i < self.C.y+self._Lyb: fill_rect(self.C.x-self.Lxg,self._C.y-self._Lyh+i,self.Lxg+self.Lxd,1,Screen.palette["SecondaryColor"])
      if self._C.y-self._Lyh+i > self.C.y-self.Lyh and self._C.x-2 > self.C.x-self.Lxg and self._C.x+2 < self.C.x+self.Lxd and self._C.y-self._Lyh+i < self.C.y+self.Lyb: fill_rect(self._C.x-2,self.C.y-self.Lyh+i,5,1,Screen.palette["PrimaryColor"])
      if self.text and n != 0: draw_string(str(n),self._C.x+10,self.C.y-self.Lyh+i-5,Screen.palette["PrimaryColor"],Screen.palette["SecondaryText"])
    for n,j in enumerate(range(0,self._Lyb,self.p)):
      if self.background and self.C.y+j > self.C.y-self._Lyh and self.C.y+j < self.C.y+self._Lyb: fill_rect(self.C.x-self.Lxg,self._C.y+j,self.Lxg+self.Lxd,1,Screen.palette["SecondaryColor"])
      if self._C.y+j < self.C.y+self.Lyb and self._C.x-2 > self.C.x-self.Lxg and self._C.x+2 < self.C.x+self.Lxd and self._C.y+j > self.C.y-self.Lyh: fill_rect(self._C.x-2,self._C.y+j,5,1,Screen.palette["PrimaryColor"])
      if self.text and n != 0: draw_string(str(-n),self._C.x+10,self._C.y+j-5,Screen.palette["PrimaryColor"],Screen.palette["SecondaryText"])
    fill_rect(self._C.x,self.C.y-self.Lyh,1,self.Lyh+self.Lyb,Screen.palette["PrimaryColor"]) if self._C.x >= self.C.x-self.Lxg and self._C.x < self.C.x+self.Lxd else None;fill_rect(self.C.x-self.Lxg,self._C.y,self.Lxg+self.Lxd,1,Screen.palette["PrimaryColor"]) if self._C.y >= self.C.y-self.Lyh and self._C.y < self.C.y+self.Lyb else None
    for dico in self.liste_scatter: self.scatter(X=dico["X"],Y=dico["Y"],color=dico["color"],style=dico["style"])
    for dico in self.liste_plot: self.plot(X=dico["X"],Y=dico["Y"],color=dico["color"])
    for dico in self.liste_point: self.set_points(liste=dico["liste"],color=dico["color"],style=dico["style"])
    for dico in self.liste_line: self.set_lines(liste=dico["liste"],color=dico["color"])
    for dico in self.liste_vector: self.set_vectors(P=dico["liste"][0],V=Vector(x=dico["liste"][1].x-dico["liste"][0].x,y=dico["liste"][1].y-dico["liste"][0].y),color=dico["color"])
    for dico in self.liste_droite: self.set_droite(A=dico["liste"][0],B=dico["liste"][1],color=dico["color"])

  def zoom(self):
    if keydown(KEY_PLUS):
      for dico in self.liste_scatter: liste = expend([Point(x,y) for x,y in zip(dico["X"],dico["Y"])], -(self.pas/self.p)/100) ; dico["X"] = [P.x for P in liste] ; dico["Y"] = [P.y for P in liste]
      for dico in self.liste_plot: liste = expend([Point(x,y) for x,y in zip(dico["X"],dico["Y"])], -(self.pas/self.p)/100) ; dico["X"] = [P.x for P in liste] ; dico["Y"] = [P.y for P in liste]
      for dico in self.liste_point: dico["liste"] = expend(dico["liste"], -(self.pas/self.p)/100)
      for dico in self.liste_line: dico["liste"] = expend(dico["liste"], -(self.pas/self.p)/100)
      for dico in self.liste_vector: dico["liste"] = expend(dico["liste"], -(self.pas/self.p)/100)
      for dico in self.liste_droite: dico["liste"] = expend(dico["liste"], -(self.pas/self.p)/100)
      self.p += self.pas ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes() ; sleep(0.2)
    if keydown(KEY_MINUS):
      for dico in self.liste_scatter: liste = expend([Point(x,y) for x,y in zip(dico["X"],dico["Y"])], (self.pas/self.p)/100) ; dico["X"] = [P.x for P in liste] if self.p-self.pas > 1 else dico["X"] ; dico["Y"] = [P.y for P in liste] if self.p-self.pas > 1 else dico["Y"]
      for dico in self.liste_plot: liste = expend([Point(x,y) for x,y in zip(dico["X"],dico["Y"])], (self.pas/self.p)/100) ; dico["X"] = [P.x for P in liste] if self.p-self.pas > 1 else dico["X"] ; dico["Y"] = [P.y for P in liste] if self.p-self.pas > 1 else dico["Y"]
      for dico in self.liste_point: dico["liste"] = expend(dico["liste"], (self.pas/self.p)/100) if self.p-self.pas > 1 else dico["liste"]
      for dico in self.liste_line: dico["liste"] = expend(dico["liste"], (self.pas/self.p)/100)
      for dico in self.liste_vector: dico["liste"] = expend(dico["liste"], (self.pas/self.p)/100)
      for dico in self.liste_droite: dico["liste"] = expend(dico["liste"], (self.pas/self.p)/100)
      self.p -= self.pas if self.p-self.pas > 1 else 0 ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes() ; sleep(0.2)

  def scroll(self):
    if keydown(KEY_UP):
      for dico in self._liste_scatter: dico["Y"] = [y+self.pas/self.p for y in dico["Y"]]
      for dico in self._liste_plot: dico["Y"] = [y+self.pas/self.p for y in dico["Y"]]
      for dico in self._liste_point: dico["liste"] = [Point(P.x,P.y+self.pas/self.p) for P in dico["liste"]]
      for dico in self._liste_line: dico["liste"] = [Point(P.x,P.y+self.pas/self.p) for P in dico["liste"]]
      for dico in self._liste_vector: dico["liste"] = [Point(P.x,P.y+self.pas/self.p) for P in dico["liste"]]
      for dico in self._liste_droite: dico["liste"] = [Point(P.x,P.y+self.pas/self.p) for P in dico["liste"]]
      self._C.y += self.pas ; self._Lyh += self.pas ; self._Lyb -= self.pas ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()
    if keydown(KEY_DOWN):
      for dico in self._liste_scatter: dico["Y"] = [y-self.pas/self.p for y in dico["Y"]]
      for dico in self._liste_plot: dico["Y"] = [y-self.pas/self.p for y in dico["Y"]]
      for dico in self._liste_point: dico["liste"] = [Point(P.x,P.y-self.pas/self.p) for P in dico["liste"]]
      for dico in self._liste_line: dico["liste"] = [Point(P.x,P.y-self.pas/self.p) for P in dico["liste"]]
      for dico in self._liste_vector: dico["liste"] = [Point(P.x,P.y-self.pas/self.p) for P in dico["liste"]]
      for dico in self._liste_droite: dico["liste"] = [Point(P.x,P.y-self.pas/self.p) for P in dico["liste"]]
      self._C.y -= self.pas ; self._Lyh -= self.pas ; self._Lyb += self.pas ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()
    if keydown(KEY_LEFT):
      for dico in self._liste_scatter: dico["X"] = [x+self.pas/self.p for x in dico["X"]]
      for dico in self._liste_plot: dico["X"] = [x+self.pas/self.p for x in dico["X"]]
      for dico in self._liste_point: dico["liste"] = [Point(P.x+self.pas/self.p,P.y) for P in dico["liste"]]
      for dico in self._liste_line: dico["liste"] = [Point(P.x+self.pas/self.p,P.y) for P in dico["liste"]]
      for dico in self._liste_vector: dico["liste"] = [Point(P.x+self.pas/self.p,P.y) for P in dico["liste"]]
      for dico in self._liste_droite: dico["liste"] = [Point(P.x+self.pas/self.p,P.y) for P in dico["liste"]]
      self._C.x += self.pas ; self._Lxg += self.pas ; self._Lxd -= self.pas ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()
    if keydown(KEY_RIGHT):
      for dico in self._liste_scatter: dico["X"] = [x-self.pas/self.p for x in dico["X"]]
      for dico in self._liste_plot: dico["X"] = [x-self.pas/self.p for x in dico["X"]]
      for dico in self._liste_point: dico["liste"] = [Point(P.x-self.pas/self.p,P.y) for P in dico["liste"]]
      for dico in self._liste_line: dico["liste"] = [Point(P.x-self.pas/self.p,P.y) for P in dico["liste"]]
      for dico in self._liste_vector: dico["liste"] = [Point(P.x-self.pas/self.p,P.y) for P in dico["liste"]]
      for dico in self._liste_droite: dico["liste"] = [Point(P.x-self.pas/self.p,P.y) for P in dico["liste"]]
      self._C.x -= self.pas ; self._Lxg -= self.pas ; self._Lxd += self.pas ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; self.set_axes()

  def main(self):
    self.set_axes()
    while True: 
      self.zoom() ; self.scroll()
      if keydown(KEY_BACKSPACE): sleep(0.1) ; break
      if keydown(KEY_ZERO):
        for dico,dico_copy in zip(self._liste_scatter,self.liste_scatter): dico["X"] = dico_copy["X"].copy() ; dico["Y"] = dico_copy["Y"].copy()
        for dico,dico_copy in zip(self._liste_plot,self.liste_plot): dico["X"] = dico_copy["X"].copy() ; dico["Y"] = dico_copy["Y"].copy()
        for dico,dico_copy in zip(self._liste_point,self.liste_point): dico["liste"] = dico_copy["liste"].copy()
        for dico,dico_copy in zip(self._liste_line,self.liste_line): dico["liste"] = dico_copy["liste"].copy()
        for dico,dico_copy in zip(self._liste_vector,self.liste_vector): dico["liste"] = dico_copy["liste"].copy()
        for dico,dico_copy in zip(self._liste_droite,self.liste_droite): dico["liste"] = dico_copy["liste"].copy()
        self._Lxg,self._Lxd,self._Lyh,self._Lyb = self.Lxg,self.Lxd,self.Lyh,self.Lyb ; self._C = Point(self.C.x,self.C.y) ; fill_rect(self.C.x-self.Lxg,self.C.y-self.Lyh,self.Lxg+self.Lxd,self.Lyh+self.Lyb,Screen.palette["Background"]) ; sleep(0.1) ; self.set_axes()

DefaultGrapher = Grapher(text=False)
def axes(grapher: Grapher = DefaultGrapher): grapher.set_axes()
def show(grapher: Grapher = DefaultGrapher): grapher.main()
def clean(grapher: Grapher = DefaultGrapher): grapher.clean()
def scatter(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.scatter(*args, **kwds)
def plot(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.plot(*args, **kwds)
def points(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.set_points(*args, **kwds)
def lines(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.set_lines(*args, **kwds)
def droite(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.set_droite(*args, **kwds)
def vector(*args, grapher: Grapher = DefaultGrapher, **kwds): grapher.set_vectors(*args, **kwds)