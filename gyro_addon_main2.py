#Copyright (C) Haoriwa 2024-2025
#All rights reserved.
#Using GPL3.0 License.
#Example for in game mod
#in game mod is a type of mod that loaded with
#"run" command. multi mods at a time.
from ti_draw import *
from time import *
from ti_system import *
from random import *
def mod_info(draw=1):#Your addon info should be here.
  aover=str("GyroModLoader v:1.1|Out game mod example")
  aocrd=str("By axnut123")
  returnmod="ingamemod"
  if returnmod=="ingamemod":
    return "ingamemod"
  if draw==1:
    draw_text(5,15,aover)
    draw_text(5,25,aocrd)
  else:
    return aover+"|"+aocrd
def mod_main():#your addon main program should start from here.
  set_color(0,0,0)
#in game mod do not need loop, we already have
#loop in main()
  set_pen("thick","solid")
  draw_rect(0,0,317,211)
  draw_text(20,20,"in game mod example")
  set_pen("thin","solid")
  return 0
if __name__=="__main__":mod_main()