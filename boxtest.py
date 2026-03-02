#A tool script for Trigger,MouseBox funcs.
#it is not like fill_rect,minx miny and maxx maxy.
#maxx and maxy can be found as minx+width.
#for example, 125 is minx,width is 100,then
#just add minx and width together, which is 225.
#same for miny and maxy, just add the height.
from ti_system import *
x1=0
x2=0
y1=0
y2=0
def MouseBox():
  x, y=get_mouse()
  if x>=x1 and x<=x2 and y>=y1 and y<=y2:return True
  else:return False
def BoxHandler(ipt):
  global x1,y1,x2,y2
  k=get_key()
  if ipt==False:set_color(20,20,20)
  else:
    if k=="center" or k=="enter":
      set_color(20,255,20)
    else:set_color(255,20,20)
    if k=="esc":raise SystemExit(0)
  fill_rect(x1,y1,x2-x1,y2-y1)
def main():
  global x1,x2,y1,y2
  print("Box test, hold esc to stop.")
  x1=int(input("minx"))
  x2=int(input("maxx"))
  y1=int(input("miny"))
  y2=int(input("maxy"))
  use_buffer()
  while True:
    clear()
    BoxHandler(MouseBox())
    set_color(0,0,0);draw_text(80,80,str(get_mouse()));paint_buffer()
if __name__=="__main__":main()