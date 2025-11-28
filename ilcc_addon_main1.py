#Copyright (C) Haoriwa 2024-2025
#All rights reserved.
#Using GPL3.0 License.
#Example for out game mod
#out game mod is a type of mod that loaded with
#"runmod" command. one mod at a time.
from ti_system import *
import __main__ as k
def mod_type():#mod type here.
  return "outgamemod"
def mod_info(draw=False):#Your addon info should be here.
  aover=str("ILCCModLoader v:1.2|Out game mod example")
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
  use_buffer()
  while True:
    clear()
    mod_info(1)
    draw_text(200,200,"Press esc to quit")
    paint_buffer()
    keysi=get_key()
    if keysi=="esc":k.Kernel.Cout.Info("Mod stopped.");k.Kernel.quit(0)
  return 0
if __name__=="__main__":mod_main(False)