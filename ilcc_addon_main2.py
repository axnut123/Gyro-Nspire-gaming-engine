#Copyright (C) Haoriwa 2024-2025
#All rights reserved.
#Using GPL3.0 License.
#Example for in game mod
#in game mod is a type of mod that loaded with
#"run" command. multi mods at a time.
from ti_system import *
import __main__ as k
def mod_type():#mod type here.
  return "ingamemod"
def mod_info(draw=False):#Your addon info should be here.
  aover=str("ILCCModLoader v:1.2|In game mod example")
  aocrd=str("By axnut123")
  if draw:
    draw_text(5,15,aover)
    draw_text(5,25,aocrd)
  else:
    return aover+"|"+aocrd
def mod_main(ignoreeverchk):#your addon main program should start from here.
  if k.VERINT<158 and not ignoreeverchk:
    k.Kernel.Cout.Error("Engine is too old for this mod. Update your engine and try again.")
    raise OSError("Engine verion is too old.")
  set_color(0,0,0)
#in game mod do not need loop, we already have
#loop in main()
  set_pen("thick","solid")
  draw_rect(0,0,317,211)
  draw_text(20,20,"in game mod example")
  set_pen("thin","solid")
  return 0
if __name__=="__main__":mod_main()