#Copyright (C) Haoriwa 2024-2025
#All rights reserved.
#Using GPL3.0 License.
import sys
from ti_draw import *
from time import *
from ti_system import *
from random import *
def mod_info(draw=1):
  aover=str("TicksCodeLib v:1")
  aocrd=str("By axnut123")
  if draw==1:
    draw_text(5,15,aover)
    draw_text(5,25,aocrd)
  else:
    return aover+" "+aocrd
def mod_main():#your addon main program should start from here.
  set_color(0,0,0)
  mod_info(1)
  paint_buffer()