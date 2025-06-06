from visual import Point, interpolate
from visual.extensions.lines import draw_lines
from math import pi, cos, sin
import kandinsky as kd

def tree(position: Point = Point(160,170), length: int = 40, angle: float | int = pi/2, iteration: int = 15, thickness: int = 1, color: list[str | tuple[int]] | tuple | str = '0', left_angle: int | float = pi/4, right_angle: int | float = pi/4, ratio: int | float = 0.7):
  degrad = True if isinstance(color, (list)) else False
  if degrad: liste_color = interpolate(kd.color(color[0]), kd.color(color[1]), iteration+1)
  N, e = 0, thickness/iteration
  def _tree(position,length,angle,iteration,thickness,color,_n):
    if iteration == 0: return
    P2 = Point(position.x-cos(angle)*length,position.y-sin(angle)*length) ; P2.round() ; position.round()
    if degrad: draw_lines([(position,P2)],[(kd.color(liste_color[_n]),kd.color(liste_color[_n+1]))],thickness)
    else: draw_lines([(position,P2)],color,thickness)
    _tree(P2,length*ratio,angle+right_angle,iteration-1,thickness-e if thickness!=1 else thickness,color,_n+1)
    _tree(P2,length*ratio,angle-left_angle,iteration-1,thickness-e if thickness!=1 else thickness,color,_n+1)
  return _tree(position,length,angle,iteration,thickness,color,N)
