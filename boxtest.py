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
def MouseBox(minx,miny,maxx,maxy):
  x, y=get_mouse()
  if x>=x1 and x<=x2 and y>=y1 and y<=y2:return True
  else:return False
def BoxHandler(ipt):
  global x1,y1,x2,y2
  if ipt==False:set_color(20,20,20)
  else:set_color(255,20,20)
  fill_rect(x1,y1,x2,y2)
def main():
  global x1,x2,y1,y2
  print("Box test, hold ecs to stop.")
  x1=int(input("minx"))
  x2=int(input("maxx"))
  y1=int(input("miny"))
  y2=int(input("maxy"))
  while get_key()!="esc":
    BoxHandler(MouseBox(x1,y1,x2,y2))
if __name__=="__main__":main()