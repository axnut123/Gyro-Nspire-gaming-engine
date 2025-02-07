#cpu tick,clock
from time import *
import sys
from ti_system import *
from ti_draw import *
set_pen("thin","solid")
lct=0;clk=0;cputk=0
while True:
  paint_buffer()
  if get_key()=="enter":
    sys.exit(0)
  lct=str(localtime())
  clk=str(clock())
  cputk=str(ticks_cpu())
  ms=str(get_mouse())
  k=str(get_key())
  clear()
  draw_text(20,40,lct)
  draw_text(20,60,clk)
  draw_text(20,80,cputk)
  draw_text(20,100,ms)
  draw_text(20,120,k)
  draw_text(220,200,"enter to quit")
  use_buffer()