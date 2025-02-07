#Grid for ti_draw
from ti_draw import *
set_pen("thin","solid")
a=0;x=0;y=0
set_color(210,210,210)
fill_rect(0,0,500,300)
set_color(100,100,100)
draw_line(0,0,317,0)
draw_line(0,0,0,211)
while a!=32:
  draw_rect(x,y,1,500)
  x+=10
  a+=1
x=0
while a!=0:
  draw_rect(x,y,500,1)
  y+=10
  a-=1