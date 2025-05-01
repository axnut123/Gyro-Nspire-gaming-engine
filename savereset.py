from ti_system import *
#Save repair.
def Delete(custom=False,name="customFile",gamevar=None):#built-in function, for delete saved game.
  if custom==False:
    try:
      store_value("playery",95)
      store_value("playerx",95)
      store_value("v_hev",0)
      store_value("emptysave",1)
      store_value("inclip9",0)
      store_value("inclip357",0)
      store_value("wpnslt",0)
      store_value("v_live",100)
      store_value("weapon_crb",0)
      store_value("weapon_physcnn",0)
      store_value("weapon_pst",0)
      store_value("weapon_357",0)
      store_value("mapslt",0)
      store_value("ammo9",0)
      store_value("ammo357",0)
      store_value("item_suit",0)
      print("[IO]Reset completed.")
      return 0
    except Exception as e:
      print("[ERROR]Operation failed.",str(e))
      Kernal.ErrChk()
      return 1
  else:
    try:
      store_value(str(name),gamevar)
      print("[IO]File operate success on:"+str(name))
      return 0
    except Exception as e:
      print("[ERROR]File operate on:"+str(name)+" failed.\n"+str(e))
      return 1
if __name__=="__main__":Delete();print("Game save reset.")