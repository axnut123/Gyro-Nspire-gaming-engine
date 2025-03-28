#Copyright (C) Haoriwa 2024-2025
#All rights reserved.
#Using GPL3.0 License.
from ti_draw import *
from time import *
from ti_system import *
from random import *
def mod_info(draw=1):#Your addon info should be here.
  aover=str("GyroModLoader v:1.1")
  aocrd=str("By axnut123")
  if draw==1:
    draw_text(5,15,aover)
    draw_text(5,25,aocrd)
  else:
    return aover+"|"+aocrd
def mod_main():#your addon main program should start from here.
  set_color(0,0,0)
  use_buffer()
  while True:
    clear()
    mod_info(1)
    draw_text(200,200,"Press esc to quit")
    paint_buffer()
    keysi=get_key()
    if keysi=="esc":raise SystemExit(0);print("[INFO]Mod stopped.")
  return 0
if __name__=="__main__":mod_main()