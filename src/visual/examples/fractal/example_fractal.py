from fractal import Point, tree, pi
from kandinsky import fill_rect
from time import sleep

# Basic example

#tree(position=Point(160,170),length=50,angle=pi/2,iteration=12,thickness=0,color=[(88,41,0), (0,255,0)],left_angle=pi/4,right_angle=pi/4,ratio=0.7)
#tree(position=Point(160,170),length=50,angle=pi/2,iteration=12,thickness=0,color="black",left_angle=pi/4,right_angle=pi/4,ratio=0.7)
#tree(position=Point(160,170),length=50,angle=pi/2,iteration=12,thickness=0,color=(0,0,0),left_angle=pi/4,right_angle=pi/4,ratio=0.7)
#tree(position=Point(160,170),length=50,angle=pi/2,iteration=12,thickness=0,color=["black","green"],left_angle=pi/4,right_angle=pi/4,ratio=0.7)

# Animation example

def animation():
  a1, a2 = pi/4, pi/4
  while True:
    tree(position=Point(160,170),length=50,angle=pi/2,iteration=12,thickness=0,color=["black","cyan"],left_angle=a1,right_angle=a2,ratio=0.7)
    sleep(1)
    fill_rect(0,0,320,222,"white")
    a1 += 1 ; a2 -= 1

animation()

# Most popular tree

#tree(position=Point(160,210),length=50,angle=pi/2,iteration=12,thickness=3,color=["red","yellow"],left_angle=2*pi/20,right_angle=2*pi/20,ratio=0.75)
#tree(position=Point(160,170),length=40,angle=pi/2,iteration=15,thickness=5,color=[(0,0,0), (255,0,255)],left_angle=2*pi/11,right_angle=2*pi/11,ratio=0.75)
#tree(position=Point(160,210),length=100,angle=pi/2,iteration=12,thickness=0,color=["magenta","purple"],left_angle=pi/2,right_angle=pi/2,ratio=0.7)

# Other tree

#tree(position=Point(100,200),length=100,angle=pi/2,iteration=12,thickness=4,color=["black","magenta"],left_angle=pi/4+5,right_angle=pi/4,ratio=0.7)
#tree(position=Point(160,210),length=65,angle=pi/2,iteration=12,thickness=5,color=["black","magenta"],left_angle=pi/4+12,right_angle=pi/4,ratio=0.7)
#tree(position=Point(160,210),length=65,angle=pi/2,iteration=12,thickness=5,color=["black","magenta"],left_angle=pi/4+6,right_angle=pi/4,ratio=0.7)
#tree(position=Point(160,210),length=70,angle=pi/2,iteration=12,thickness=6,color=["black","magenta"],left_angle=pi/4+13,right_angle=pi/4,ratio=0.7)
