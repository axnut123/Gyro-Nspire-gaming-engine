#Gyro 2D engine-Core module and source code.
#COPYRIGHT (C) Haoriwa 2024 - 2025
#All rights reserved.
#Licensed under the GNU General Public
#License v3.0 (or later).
#You may freely use,modify,and redistribute this
#software.
#under the terms described in the LICENSE file
#included with this project.
#NO warranties are provided.Use at your own
#risk. For full license text, visit-
#https://www.gnu.org/licenses/gpl-3.0.html
#Please use PascalCase to name func, class.
#In main function, everything is clean and
#visible, if more features are needed, add
#them in the main function. But sometimes you
#have to add something in built-in functions.
#Every class, functions in here are all with
#examples, you can learn engine from examples.
from random import randint
from ti_draw import *
from time import *
from ti_system import *
sys=__import__("sys")
gc=__import__("gc")
mp=__import__("micropython")#import done
novid=bool(False);
modamount=int(100);
endtick=None;
langtype=int(1);
active=bool(False);
action=None;
plr=int(0);
plg=int(0);
plb=int(0);
plw=int(0);
plh=int(0);
dev=bool(False);
usemod=bool(True);
dr=bool(False);
debugs=bool(False);
erxt=int(0);
g=str("");
key=str("");
mapslt=int(0);
psx=int(0);
psy=int(0);
v_hev=int(0);
GAMEVER=str("Gyro 26 Build(0094)");
wpnslt=int(0);
item_suit=int(0);
weapon_crb=int(0);
weapon_physcnn=int(0);
weapon_pst=int(0);
weapon_357=int(0);
ammo357=int(0);
ammo9=int(0);
v_live=int(100);
ammo9max=int(180);
ammo357max=int(12);
inclip9=int(0);
inclip357=int(0);
reload9=int(0);
reload357=int(0);
vtk=bool(False);
modenb=bool(False);
ingamemod=str("");
modscripts=list([]);
emptysave=int(1);#True or False dosent work.
class Kernal:#Code base class
  def __init__(self):pass
  @staticmethod
  def quit(self=None):#built-in function, in nspire cx ii python the Kernal.quit function is not defined.
    gc.collect()
    raise SystemExit(self)
  @staticmethod
  def SaveCfg():
    global langtype,dev,dr,usemod,novid,modamount
    try:
      if langtype==1:
        IO.Save(True,"langtype",1)
      elif langtype==2:
        IO.Save(True,"langtype",2)
      else:
        IO.Save(True,"Langtype",1)
        print("[WARN]Language type not found, using default language.")
        Kernal.ErrChk()
      IO.Save(True,"modamount",int(modamount))
      if novid==True:IO.Save(True,"novid",1)
      else:IO.Save(True,"novid",0)
      if dev==True:IO.Save(True,"dev",1)
      else:IO.Save(True,"dev",0)
      if dr==True:IO.Save(True,"dr",1)
      else:IO.Save(True,"dr",0)
      if usemod==True:IO.Save(True,"usemod",1)
      else:IO.Save(True,"usemod",0)
      print("[INFO]Cfg saving success.")
    except Exception as e:
      print("[ERROR]Cfg saving failed."+str(e))
      Kernal.ErrChk()
    return 0
  @staticmethod
  def Init(inittp):#built-in function.for init cfgs or other files engine needed.
    global dev,dr,novid,langtype,usemod,modamount
    if inittp==1:
      try:
        cfg1=IO.Load(True,"novid",None)
        cfg2=IO.Load(True,"dev",returnval=None)
        cfg3=IO.Load(True,"dr",returnval=None)
        cfg4=IO.Load(True,"langtype",returnval=None)
        cfg5=IO.Load(True,"usemod",returnval=None)
        modamount=IO.Load(True,"modamount",returnval=None)
        if cfg1==1:novid=True
        else:novid=False
        if cfg2==1:dev=True
        else:dev=False
        if cfg3==1:dr=True
        else:dr=False
        if cfg4==2:langtype=2
        elif cfg4==1:langtype=1#add more condition if more languages needed.
        if cfg5==1:usemod=True
        else:usemod=False
        del cfg1,cfg2,cfg3,cfg4,cfg5
        gc.collect()
        print("[INFO]Config loading process completed.")
        return 1
      except Exception as e:
        print("[ERROR]Failed on trying to load configs."+str(e))
        return 0
  @staticmethod
  def ErrChk(c=1):#built-in function,for command "forceexitonerror".
    global erxt
    if erxt==1:
      print("[DEBUG]Error or warning encounted,\nstopped engine.")
      Kernal.quit(c)
  @staticmethod
  def WaitUpdate():#built-in function. for check the wait tick.
    global active,action,endtick
    if active and ticks_cpu()>=endtick:
      active=False
      if action:
        action()
        action=None
  @staticmethod
  def ResetGame():#built-in function,for soft reset.
    global mapslt,psx,v_live,v_hev,psy,weapon_crb,debugs,v_hev,weapon_physcnn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit
    mapslt=0;plh=0;plw=0;plg=0;plb=0;plr=0;psx=0;psy=0;v_hev=0;wpnslt=0;item_suit=0;weapon_crb=0;weapon_physcnn=0;weapon_pst=0;weapon_357=0;ammo357=0;ammo9=0;v_live=100;ammo9max=180;ammo357max=12;inclip9=0;inclip357=0;reload9=0;reload357=0
    print("[INFO]Game reset completed.")
    return
  @staticmethod
  def GameLauncher():#Built-in function, for game loading process.
    global novid,modenb,g,tk,ingamemod
    del g
    print("[CONSOLE]Console is being closed.\n[INFO]Engine is now started.")
    gc.collect()
    StdUtil.ConsoleLog(2)
    use_buffer()
    if novid==False:Kernal.Opening()
    if ingamemod=="ingamemod":modenb=False
    StdUtil.ConsoleLog(5)
    if modenb==True and ingamemod!="ingamemod":
      print("[INFO]Trying to load mod script.")
      tk.mod_main()
    else:
      print("[INFO]Mod loader was not enabled,loading main script.")
      main()
  @staticmethod
  def Console():#built-in function,for console.
    global ingamemod,modscripts,g,modenb,vtk,erxt,novid,tk,dev,dr,langtype,usemod,modamount
    print("[PRE-LOAD]Starting console.")
    while g!="run"or g!="start"or g!="begin":
      g=str(input("]"))
      if g=="run"or g=="start"or g=="begin":
        print("[CONSOLE]Running engine.")
        break
      elif g=="setlang":
        g=str(input("1:English,2:Simplified Chinese,3.Cancel"))
        if g=="1":
          langtype=1
          print("[CONSOLE]Language set.")
        elif g=="2":
          langtype=2
          print("[CONSOLE]Language set.")
        elif g=="3":pass
        else:
          print("[ERROR]Language type unknow, using default language.")
          langtype=1
      elif g=="disablemod":
        try:
          del tk
          print("[INFO]Mod is uninstalled, but reboot is recommended.")
          gc.collect()
        except Exception as e:
          print("[ERROR]Mod cannot be uninstalled, "+str(e))
          Kernal.ErrChk()
        vtk=False
        modenb=False
        print("[INFO]Mod disabled.")
      elif g=="modinit":
        if vtk!=True:
          print("[INFO]Mod is loading... if mod loading amount is more than 100, it will take a long time to load, please wait.")
          for i in range(int(modamount)):
            try:
              tk=__import__("gyro_addon_main"+str(i))
              modscripts.append(tk)
            except ImportError:
              continue
          vtk=True
          print("[INFO]Mod init success.")
          ingamemod=tk.mod_info(3)
        else:
          print("[WARN]Mod already init.")
          Kernal.ErrChk()
      elif g=="runmod":
        if vtk==True and ingamemod!="ingamemod":
          modenb=True
          print("[INFO]Mod is running.")
          break
        else:
          print("[ERROR]Mod script not found or mod type is not supported.")
          Kernal.ErrChk()
      elif g=="initcfg":
        Kernal.Init(1)
      elif g=="modver":
        print("Warning: do not let 2 types of mods installed together.")
        if vtk==True:
          print(tk.mod_info(3))
          print(tk.mod_info(2))
        else:
          print("[ERROR]Mod is not found.")
          Kernal.ErrChk()
      elif g=="savecfg":
        Kernal.SaveCfg()
      elif g=="help 1":
        print("Gyro engine help page 1:\nrun:start engine.\nhelp <page(1/2/3)>:get help.\nquit:stop engine and console.\nsetgeomet:set a new resolution for screen.\nforceexitonerror:forcely stop whole engine when encounting any error and warn.\nversion:get engine version and credits.\nhwinfo:get hardware info.\ncls:clear screen.")
      elif g=="help 2":
        print("Gyro engine help page 2:\nloadgame:load game from saved file.\ndeletesave:delete saved game.\nmodinit:__init__ installed mod.\nrunmod:start mod.\nmodver:get version for mod.\ndisablemod:disable mod.(pop)\nadjustthreshold:change the value for gc.threshold()\ndev: toggle devloper mode.")
      elif g=="help 3":
        print("Gyro engine help page 3:\nscuptoggle: toggle the output when screen \nupdate.\nexec:use exec() to execute python code.\nnovid:disable launch video.\ninitcfg:execute cfg init process manually.\nsavecfg:save current configs.\ngetcfgs:get current cfg status.\nsetmodamount:tell mod loader how many mods shold be loaded.\nsetlang:set a language for engine.")
      elif g=="quit"or g=="stop"or g=="exit"or g=="esc":
        del g
        StdUtil.ConsoleLog(3)
        Kernal.quit()
        break
      elif g=="setmodamount":
        g=input("how many mods shold be load(default 100):")
        modamount=g
        print("[CONSOLE]"+str(modamount)+" mods will be trying to load.")
      elif g=="scuptoggle":
        if dr==False:
          dr=True;print("[CONSOLE]Enabled.")
        else:dr=False;print("[CONSOLE]Disabled.")
      elif g=="setgeomet":
        try:
          x1=int(input("xmin"))
          y1=int(input("ymin"))
          x2=int(input("xmax"))
          y2=int(input("ymax"))
          set_window(x1,x2,y1,y2)
          print("[INFO]Resolution set to:"+str(x1)+","+str(y1)+","+str(x2)+","+str(y2))
          break
        except Exception as e:
          print("[ERROR]Setting was failed. "+str(e))
          Kernal.ErrChk()
      elif g=="getcfgs":
        print("novid:"+str(novid))
        print("log output on screen draw:"+str(dr))
        print("dev:"+str(dev))
        print("lang:"+str(ActionUI.DispLanguage("lang")))
        print("use mod:"+str(usemod))
        print("mod amounts:"+str(modamount))
      elif g=="forceexitonerror":
        if erxt==1:
          erxt=0
          print("[CONSOLE]Exit when error disabled.")
        else:
          erxt=1
          print("[CONSOLE]Exit when error enabled.")
      elif g=="version":
        print("Gyro 2D Gaming engine.\n",GAMEVER,"\nFirst runned in 2025/05/12\nMade by Alex_Nute aka axnut123.\nMade in China.\nyour Python version:",sys.version,"\nEngine built on Python 3.4.0")
      elif g=="novid":
        if novid==False:
          novid=True
          print("[CONSOLE]Disabled launch video")
        else:
          novid=False
          print("[CONSOLE]Enabled launch video")
      elif g=="hwinfo":
        print("Version",str(GAMEVER))
        print("Platform",str(get_platform()))
        print("mem free",str(gc.mem_free()))
        print("mem alloc",str(gc.mem_alloc()))
        print("stack use",str(mp.stack_use()))
        print("pystack use",str(mp.pystack_use()))
        print("cpu tick",ticks_cpu())
        print("local time",str(localtime()))
      elif g=="deletesave":
        IO.Delete()
      elif g=="loadgame":
        IO.Load()
      elif g=="help":
        print("Usage: help <1/2/3>. example: help 1 for page 1.")
      elif g=="cls":
        clear_history()
      elif g=="dev":
        if dev==False:
          dev=True
          print("[CONSOLE]Dev mode enabled.")
        else:dev=False;print("[CONSOLE]Dev mode disabled")
      elif g=="adjustthreshold":
        try:
          b=int(input("gc.threshold:"))
          gc.threshold(int(b))
          print("[CONSOLE]New value given.")
        except Exception as e:
          print("[ERROR]Failed. "+str(e))
      elif g=="exec":
        g=str(input("execute:"))
        try:
          exec(g)
          print("[INFO]Executed code.")
        except Exception as e:
          print("[ERROR]Unable to execute code. "+str(e))
          Kernal.ErrChk()
        except SystemExit:
          StdUtil.ConsoleLog(3)
          del g
          Kernal.quit(0)
      elif g=="":pass
      else:
        print("[CONSOLE]Unknown command:",g,".type help <page(1/2/3)> to get help.")
  @staticmethod
  def Info(infotype):#built-in function.For output information about engine.
    infos={
    1:"(C) Haoriwa 2022-2025. All rights reserved.",
    2:"Built on MicroPython 3.4.0.",
    3:"Built for ARM Cortex-M7.",
    4:"License type is GPL3.0,under the license.txt."}
    return infos.get(infotype)
  @staticmethod
  def Opening():#the engine opening
    fill_rect(0,0,500,300)
    set_color(10,210,140)
    draw_text(80,120,"Made By: Alex_Nute")
    paint_buffer()
    sleep(2)
    set_color(0,0,0)
    fill_rect(0,0,500,300)
    set_color(255,100,120)
    draw_text(80,80,"POWERED BY:")
    set_color(10,10,255)
    draw_text(185,80,"Gyro")
    set_color(255,255,255)
    draw_text(10,100,"Copyright © Haoriwa 2022 - 2025, the Half-Life 2 is")
    draw_text(10,115,"copyright for Valve.The ti_draw,ti_system")
    draw_text(10,130,"is copyright for Texas Instruments.Using this")
    draw_text(10,145,"software represents you agreed our terms.")
    draw_text(10,160,GAMEVER)
    paint_buffer()
    sleep(1.7)
    return
class IO:#Input-Output class.
  def __init__(self):pass
  @staticmethod
  def Save(custom=False,name="customFile",gamevar=None):#built-in function, for saving game.
    global emptysave,mapslt,psx,v_live,v_hev,psy,weapon_crb,v_hev,weapon_physcnn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit
    if custom==False:
      try:
        store_value("playery",psy)
        store_value("playerx",psx)
        store_value("v_hev",v_hev)
        store_value("emptysave",0)
        store_value("inclip9",inclip9)
        store_value("inclip357",inclip357)
        store_value("wpnslt",wpnslt)
        store_value("v_live",v_live)
        store_value("weapon_crb",weapon_crb)
        store_value("weapon_physcnn",weapon_physcnn)
        store_value("weapon_pst",weapon_pst)
        store_value("weapon_357",weapon_357)
        store_value("mapslt",mapslt)
        store_value("ammo9",ammo9)
        store_value("ammo357",ammo357)
        store_value("item_suit",item_suit)
        print("[IO]Game saved.")
        return 0
      except Exception as e:
        print("[ERROR]Operation failed.",str(e))
        Kernal.ErrChk()
        return 1
    else:
      try:
        store_value(str(name),gamevar)
        print("[IO]Saved file:"+str(name)+".")
        return 0
      except Exception as e:
        print("[ERROR]File operation on:"+str(name)+" failed.\n"+str(e))
        Kernal.ErrChk()
        return 1
  @staticmethod
  def Delete(custom=False,name="customFile",gamevar=None):#built-in function, for delete saved game.
    global emptysave,mapslt,psx,v_live,v_hev,psy,weapon_crb,v_hev,weapon_physcnn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit
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
        print("[IO]File deleted.")
        return 0
      except Exception as e:
        print("[ERROR]Operation failed.",str(e))
        Kernal.ErrChk()
        return 1
    else:
      try:
        store_value(str(name),gamevar)
        print("[IO]File operate success on:"+str(name)+".")
        return 0
      except Exception as e:
        print("[ERROR]File operate on:"+str(name)+" failed.\n"+str(e))
        return 1
  @staticmethod
  def Load(custom=False,name="customFile",logout=True,returnval=0):#built-in function, for load a saved game.
    global emptysave,mapslt,psx,v_live,v_hev,psy,weapon_crb,v_hev,weapon_physcnn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit
    if custom==False:
      try:
        mapslt=recall_value("mapslt")
        emptysave=recall_value("emptysave")
        wpnslt=recall_value("wpnslt")
        weapon_357=recall_value("weapon_357")
        weapon_pst=recall_value("weapon_pst")
        ammo9=recall_value("ammo9")
        ammo357=recall_value("ammo357")
        psy=recall_value("playery")
        psx=recall_value("playerx")
        v_live=recall_value("v_live")
        v_hev=recall_value("v_hev")
        inclip9=recall_value("inclip9")
        inclip357=recall_value("inclip357")
        weapon_crb=recall_value("weapon_crb")
        weapon_physcnn=recall_value("weapon_physcnn")
        item_suit=recall_value("item_suit")
        if v_live<=0:
          print("[WARN]Game save is invalid with health:"+str(v_live)+".\n please reset current save. with savereset.py")
          Kernal.ErrChk()
          return 2
        if emptysave==1:
          print("[WARN]Trying to load an empty save.")
          Kernal.ErrChk()
          return 2
        else:
          print("[IO]Game loaded from save.")
          return 0
      except Exception as e:
        print("[ERROR]Operation failed.",str(e))
        Kernal.ErrChk()
        return 1
    else:
      try:
        returnval=recall_value(str(name))
        if logout==True:print("[IO]File operation on:"+str(name)+" success.")
        return returnval
      except Exception as e:
        print("[ERROR]File operation failed on:"+str(name)+".\n"+str(e))
        Kernal.ErrChk()
        return "ERR"
class UniFX:#Universal VFX class.
  def __init__(self):pass
  @staticmethod
  def LowHealth():#built-in function, vfx for low health.
    set_color(190,20,20)
    set_pen("thick","solid")
    draw_rect(0,0,317,211)
    set_pen("thin","solid")
    return 0
  class BulletFX:#Class for bullet flare.
    def __init__(self):pass
    @staticmethod
    def BltFlr(btp):#Built-in function. for bullet flare.
      global psy,psx
      if btp==1:
        set_color(240,240,5)
        draw_line(psx,psy-20,psx,psy-45)
        return 1
      elif btp==2:
        set_color(240,240,5)
        draw_line(psx,psy-20,psx,psy-85)
        return 2
      elif btp==3:
        set_color(210,210,210)
        fill_arc(psx-19,psy-9,50,30,30,100)
        return 3
      elif btp==4:
        set_color(255,150,10)
        set_pen("thick","solid")
        draw_line(psx,psy,psx,psy-35)
        set_pen("thin","solid")
        return 4
      elif btp==5:
        set_color(240,240,0)
        draw_line(psx,psy+20,psx,psy+45)
        return 5
      elif btp==6:
        set_color(240,240,0)
        draw_line(psx,psy+20,psx,psy+85)
        return 6
      elif btp==7:
        set_color(210,210,210)
        fill_arc(psx-19,psy-9,50,30,-30,-100)
        return 7
      elif btp==8:
        set_color(255,150,10)
        set_pen("thick","solid")
        draw_line(psx,psy,psx,psy+35)
        set_pen("thin","solid")
        return 8
      elif btp==9:
        set_color(240,240,0)
        draw_line(psx-20,psy,psx-45,psy)
        return 9
      elif btp==10:
        set_color(240,240,0)
        draw_line(psx-20,psy,psx-85,psy)
        return 10
      elif btp==11:
        set_color(210,210,210)
        fill_arc(psx-19,psy-9,50,30,-120,-90)
        return 11
      elif btp==12:
        set_color(255,150,10)
        set_pen("thick","solid")
        draw_line(psx,psy,psx-35,psy)
        set_pen("thin","solid")
        return 12
      elif btp==13:
        set_color(240,240,0)
        draw_line(psx+20,psy,psx+45,psy)
        return 13
      elif btp==14:
        set_color(240,240,0)
        draw_line(psx+20,psy,psx+85,psy)
        return 14
      elif btp==15:
        set_color(210,210,210)
        fill_arc(psx-19,psy-9,50,30,-30,100)
        return 15
      elif btp==16:
        set_color(255,150,10)
        set_pen("thick","solid")
        draw_line(psx,psy,psx+35,psy)
        set_pen("thin","solid")
        return 16
      else:
        print("[ERROR]Cannot find type of the VFX that dedicated")
        Kernal.ErrChk()
        return 0
class Actors:#entity class.
  def __init__(self):pass
  class King:#Player class.
    def __init__(self):pass
    @staticmethod
    def Draw():#built-in function, draw player.
      global plr,plg,plb,psy,psx,plw,plh,v_live
      set_color(plr,plg,plb)
      if v_live<=0 or v_live==0:return 0
      fill_rect(psx,psy,plw,plh)
      return 0
    @staticmethod
    def Init(inittype,ar1=None,ar2=None,ar3=None):#built-in function,for init player vars
      global plr,plg,plb,psy,psx,plw,plh,v_live,v_hev,ammo9,ammo357,inclip9,inclip357,item_suit,weapon_crb,weapon_pst,weapon_357,weapon_physcnn
      if inittype==1:
        plr=ar1
        plg=ar2
        plb=ar3
        return 1
      elif inittype==2:
        psx=ar1
        psy=ar2
        return 2
      elif inittype==3:
        plw=ar1
        plh=ar2
        return 3
      elif inittype==4:
        v_live=ar1
        return 4
      elif inittype==5:
        v_hev=ar1
        return 5
      elif inittype==6:
        ammo9=ar1
        inclip9=ar2
        return 6
      elif inittype==7:
        ammo357=ar1
        inclip357=ar2
        return 7
      elif inittype==8:
        weapon_crb=ar1
        return 8
      elif inittype==9:
        weapon_pst=ar1
        return 9
      elif inittype==10:
        weapon_357=ar1
        return 10
      elif inittype==11:
        weapon_physcnn=ar1
        return 11
      elif inittype==12:
        item_suit=ar1
        return 12
      else:
        print("[ERROR]Unknown init type.")
        Kernal.ErrChk()
        return 0
  class Queen:#npc entities.
    def __init__(self):pass
    def Draw(x,y,w=5,h=5,r=20,g=20,b=20):#built-in function,for drawing entities.
      set_color(r,g,b)
      fill_rect(x,y,w,h)
      return 0
class ActionUI:#UI class
  def __init__(self):pass
  @staticmethod
  def DispLanguage(langstr):#built-in function,for replacing given key to specific value.
    global langtype
    if langtype==1:#English
      langdict1={
      "usemod":"Enable mod:",
      "lang":"English",
      "gofuckyourself":"Go fuck your self!",
      "riseandshine":"Rise and shine mister Freeman,rise and shine.",
      "sleepingonthejob":"No one is deserving to sleeping on the job,",
      "effortoftheworld":"But the effort of the world will have gone to waste untill...",
      "em":"emm...",
      "yourhourhascome":"Well,let's just say your hour has come again.",
      "rightman":"The right man in the wrong place",
      "maketheworld":"Will make the whole world difference.",
      "wakeup":"So,wake up,Mr.Freeman.",
      "smell":"Wake up and smell the ashes...",
      "memfree":"mem free:",
      "memalloc":"mem alloc:",
      "stackuse":"stack use:",
      "pystackuse":"pystack use:",
      "cputick":"cpu tick:",
      "localtime":"local time:",
      "ppos":"player pos:",
      "mapid":"map id:",
      "ver":"Version:",
      "platform":"current platform:",
      "escres":"esc:resume",
      "menu":"menu:main menu",
      "savegm":"s:save game",
      "loadgm":"l:load game",
      "modamount":"loaded mods:",
      "delgm":"d:delete save",
      "quitgm":"q:quit game",
      "start1":"enter:start a new game",
      "start2":"a:quick start",
      "loadgm1":"b:load game",
      "delgm1":"c:delete save",
      "escquit":"esc:quit game",
      "suit":"SUIT",
      "health":"HEALTH",
      "youdied":"You died,press enter to continue",
      "ammo":"AMMO",
      "crb":"CROWBAR",
      "physcnn":"GRAVITY GUN",
      "pst":"PISTOL",
      "357":".357 MAGNUM",
      "load":"Loading...",
      "dr":"log output when screen update",
      "dev":"developer mode",
      "savecfg":"s:save cfg",
      "langset":"language setting",
      "set":"tab:settings",
      "titset":"Settings(press to toggle)"}
      try:
        return str(langdict1.get(langstr))
      except Exception as e:
        print("[ERROR]ActionUI.DispLanguage() method has an error occured."+str(e))
        return "Undef"
    elif langtype==2:#Schinese
      langdict2={
      "modamount":"模组加载数:",
      "usemod":"启用模组:",
      "lang":"简体中文",
      "set":"tab:设置",
      "savecfg":"s:保存设置",
      "dr":"当屏幕更新时输出",
      "dev":"开发者模式",
      "langset":"语言设置",
      "gofuckyourself":"滚你妈的！",
      "riseandshine":"该醒了,弗里曼先生,该醒了。",
      "sleepingonthejob":"还有谁比你更有资格享受空闲呢,",
      "effortoftheworld":"但是整个世界的努力都将因此而徒劳",
      "em":"恩...",
      "yourhourhascome":"我只是想说是你该再次出手的时候了。",
      "rightman":"正义之子在有悖常理的世界",
      "maketheworld":"会让世界天翻地腹。",
      "wakeup":"醒来吧,弗里曼先生",
      "smell":"振作起来,战斗吧",
      "memfree":"可用内存:",
      "memalloc":"分配的内存:",
      "stackuse":"已用栈:",
      "pystackuse":"已用py栈:",
      "cputick":"处理器刻:",
      "localtime":"本地时间:",
      "ppos":"玩家坐标:",
      "mapid":"地图编号:",
      "ver":"版本号:",
      "platform":"当前平台:",
      "escres":"esc:回到游戏",
      "menu":"menu:主菜单",
      "savegm":"s:保存",
      "loadgm":"l:加载",
      "delgm":"d:删除存档",
      "quitgm":"q:退出",
      "start1":"enter:新游戏",
      "start2":"a:快速开始",
      "loadgm1":"b:加载",
      "delgm1":"c:删除存档",
      "escquit":"esc:退出",
      "suit":"防护衣",
      "health":"生命值",
      "youdied":"你死了,按下enter继续",
      "ammo":"弹药",
      "crb":"翘棍",
      "physcnn":"重力枪",
      "pst":"手枪",
      "357":".357 马格南",
      "load":"载入中...",
      "titset":"设置(按下切换)"}
      try:
        return str(langdict2.get(langstr))
      except Exception as e:
        print("[ERROR]ActionUI.DispLanguage() method has an error occured."+str(e))
        return "Undef"
    else:
      return "[ERROR]Language not found."
  @staticmethod
  def DispUi(x,y,wintp):#built-in function,for display window, gui elements.
    set_color(135,135,135)
    global emptysave,dev,mapslt,debugs,v_live,v_hev,wpnslt,ammo9,ammo357,inclip9,inclip357,weapon_pst,weapon_crb,weapon_physcnn,weapon_357,dr,langtype,usemod,modamount
    emptysave=recall_value("emptysave")
    if wintp==1:
      fill_rect(x,y,120,40)
      set_color(255,255,255)
      draw_text(x+10,y+20,"Vgui window")
      print("[INFO]Vgui window render request sent to client.")
      return 0
    elif wintp==2:
      if debugs==True and dev==True:
        set_color(0,0,0)
        draw_text(10,20,str(ActionUI.DispLanguage("memfree"))+str(gc.mem_free()))
        draw_text(10,35,str(ActionUI.DispLanguage("memalloc"))+str(gc.mem_alloc()))
        draw_text(10,55,str(ActionUI.DispLanguage("stackuse"))+str(mp.stack_use()))
        draw_text(10,70,str(ActionUI.DispLanguage("pystackuse"))+str(mp.pystack_use()))
        draw_text(10,85,str(ActionUI.DispLanguage("cputick"))+str(ticks_cpu()))
        draw_text(10,100,str(ActionUI.DispLanguage("localtime"))+str(localtime()))
        draw_text(10,115,str(ActionUI.DispLanguage("ppos"))+str(psx)+","+str(psy))
        draw_text(10,130,str(ActionUI.DispLanguage("mapid"))+str(mapslt))
        draw_text(10,145,str(ActionUI.DispLanguage("ver"))+str(GAMEVER))
        draw_text(10,160,str(ActionUI.DispLanguage("platform"))+str(get_platform()))
        draw_text(10,175,str(ActionUI.DispLanguage("modamount"))+str(modamount))
        paint_buffer()
        return 0
    elif wintp==3:
      set_color(250,250,250)
      draw_text(10,80-20,"HALF-LIFE²")
      draw_text(10,100-20,str(ActionUI.DispLanguage("escres")))
      draw_text(10,120-20,str(ActionUI.DispLanguage("menu")))
      draw_text(10,140-20,str(ActionUI.DispLanguage("savegm")))
      if emptysave==1:
        set_color(210,210,210)
      draw_text(10,160-20,str(ActionUI.DispLanguage("loadgm")))
      set_color(250,250,250)
      draw_text(10,180-20,str(ActionUI.DispLanguage("delgm")))
      draw_text(10,200-20,str(ActionUI.DispLanguage("set")))
      draw_text(10,220-20,str(ActionUI.DispLanguage("quitgm")))
      return 0
    elif wintp==4:
      set_color(250,250,250)
      draw_text(10,100,str(ActionUI.DispLanguage("start1")))
      draw_text(10,120,str(ActionUI.DispLanguage("start2")))
      if emptysave==1:
        set_color(210,210,210)
      draw_text(10,140,str(ActionUI.DispLanguage("loadgm1")))
      set_color(250,250,250)
      draw_text(10,160,str(ActionUI.DispLanguage("delgm1")))
      draw_text(10,180,str(ActionUI.DispLanguage("set")))
      draw_text(10,200,str(ActionUI.DispLanguage("escquit")))
      paint_buffer()
      return 0
    elif wintp==5:
      set_color(120,120,120)
      fill_rect(30,0,15,15)
      set_color(200,150,50)
      draw_text(31,13,"1")
      set_color(120,120,120)
      fill_rect(55,0,15,15)
      set_color(200,150,50)
      draw_text(56,13,"2")
      return 0
    elif wintp==6:
      set_color(200,150,50)
      if v_hev>0:
        draw_text(80,190,v_hev)
        draw_text(80,200,str(ActionUI.DispLanguage("suit")))
      if v_live>=21:
        set_color(200,150,50)
        draw_text(15,190,v_live)
        draw_text(15,200,str(ActionUI.DispLanguage("health")))
      else:
        set_color(250,100,10)
        draw_text(15,190,v_live)
        draw_text(15,200,str(ActionUI.DispLanguage("health")))
        return 0
    elif wintp==7:
      set_color(210,10,10)
      fill_rect(0,0,500,300)
      set_color(255,255,255)
      draw_text(20,80,str(ActionUI.DispLanguage("youdied")))
      return 0
    elif wintp==8:
      if wpnslt==1 or wpnslt==2:#ammunation management.
        pass
      elif wpnslt==3 and weapon_pst==1:
        if ammo9>=18:
          set_color(200,150,50)
        else:
          set_color(255,100,50)
        draw_text(210,200,str(ActionUI.DispLanguage("ammo")))
        draw_text(210,190,inclip9)
        draw_text(250,190,ammo9)
      elif wpnslt==4 and weapon_357==1:
        if ammo357>=6:
          set_color(200,150,50)
        else:
          set_color(250,100,50)
        draw_text(210,200,str(ActionUI.DispLanguage("ammo")))
        draw_text(210,190,inclip357)
        draw_text(250,190,ammo357)
        return 0
    elif wintp==9:
      set_color(250,250,250)
      draw_text(220,205,str(ActionUI.DispLanguage("load")))
      paint_buffer()
      return 0
    elif wintp==10:
      set_color(120,120,120)
      fill_rect(30,30,80,50)
      set_color(200,150,50)
      draw_text(31,82,str(ActionUI.DispLanguage("crb")))
      return 0
    elif wintp==11:
      set_color(120,120,120)
      fill_rect(30,100,120,50)
      set_color(200,150,50)
      draw_text(31,145,str(ActionUI.DispLanguage("physcnn")))
      return 0
    elif wintp==12:
      set_color(120,120,120)
      fill_rect(55,30,80,50)
      if ammo9==0:
        set_color(255,10,10)
      else:set_color(200,150,50)
      draw_text(56,82,str(ActionUI.DispLanguage("pst")))
      return 0
    elif wintp==13:
      set_color(120,120,120)
      fill_rect(55,100,125,50)
      if ammo357==0:
        set_color(255,10,10)
      else:set_color(200,150,50)
      draw_text(56,142,str(ActionUI.DispLanguage("357")))
      return 0
    elif wintp==14:
      set_color(250,250,250)
      draw_text(10,80,str(ActionUI.DispLanguage("titset")))
      draw_text(10,100,"a:"+str(ActionUI.DispLanguage("dr"))+":"+str(dr))
      draw_text(10,120,"b:"+str(ActionUI.DispLanguage("dev"))+":"+str(dev))
      draw_text(10,140,"c:"+str(ActionUI.DispLanguage("langset"))+":"+str(ActionUI.DispLanguage("lang")))
      draw_text(10,160,"d:"+str(ActionUI.DispLanguage("usemod")+str(usemod)))
      draw_text(10,180,str(ActionUI.DispLanguage("savecfg")))
      draw_text(10,200,str(ActionUI.DispLanguage("escres")))
      return 0
    else:
      print("[ERROR]Window type is not defined.")
      Kernal.ErrChk()
      return 1
  @staticmethod
  def Title(x,y,texttp):#built-in function,for display a title.
    if texttp==1:
      set_color(255,0,0)
      draw_text(x,y,"Trigger")
      print("[INFO]Title displayed.")
      return 0
    else:
      print("[INFO]Title type not defined.")
      Kernal.ErrChk()
      return 1
class StdUtil:#Builtins class, Standard utilities.
  def __init__(self):pass
  @staticmethod
  def ConsoleLog(numoflog):#built-in function,for console output
    typeforlog={
      1:"[INFO]Screen updated.",
      2:"[INFO]Start the Opening.",
      3:"[INFO]Exit success,code:0",
      4:"[INFO]All assets are ready to use.",
      5:"[INFO]Game start",
      6:"[INFO]Map loaded",
      7:"[INFO]Player died."}
    print(typeforlog.get(numoflog))
    return numoflog
  @staticmethod
  def WaitStart(sec,callback):#built-in function. similar to sleep but will not stop engine.
    global endtick,active,action
    endtick=ticks_cpu()+sec
    active=True
    action=callback
  @staticmethod
  def Trigger(minx,miny,maxx,maxy,trgtp):#built-in function,for trigger a specific event.
    global v_live,mapslt,psx,psy#map selection needs global var
    if psx>=minx and psx<=maxx and psy>=miny and psy<=maxy:
      if trgtp==1:
        ActionUI.Title(120,80,1)
        print("[INFO]Trigger executed.")
        return 1
      elif trgtp==2:
        mapslt=1
        print("[INFO]Trigger executed.")
        return 2
      elif trgtp==3:
        mapslt=0
        print("[INFO]Trigger executed.")
        return 3
      elif trgtp==4:
        v_live-=15
        print("[INFO]Trigger executed.")
        return 4
      else:
        print("[ERROR]Trigger is not defined.")
        Kernal.ErrChk()
        return 0
  @staticmethod
  def ExecOnce(exectp):#built-in function.for executing sth. once.
    exed1=False
    if exectp==1:
      if exed1==False:
        trg1=StdUtil.Trigger(100,100,50,50,4)#Do something here.
        if trg1==4:
          exed1=True
          return 1
    else:
      print("[ERROR]Function cannot find exec type.")
      Kernal.ErrChk()
      return 0
  @staticmethod
  def SettingMenu():#settings menu,built-in function.
    set_color(120,120,120)
    fill_rect(0,0,500,300)
    set_color(250,250,250)
    ActionUI.DispUi(0,0,14)
    return 0
  @staticmethod
  def PauseMenu():#pause menu,built-in function.
    set_color(120,120,120)
    fill_rect(0,0,500,300)
    set_color(255,255,255)
    draw_text(150,17,GAMEVER)
    ActionUI.DispUi(0,0,3)
    return 0
  @staticmethod
  def MapStat():#built-in function,for map render,trigger and other stuff.
    global mapslt
    if mapslt==0:
      Assets.c1a0()
      StdUtil.Trigger(0,0,20,50,2)
      StdUtil.ExecOnce(1)
      return 0
    if mapslt==1:
      Assets.c0a0()
      StdUtil.Trigger(125,75,100,100,3)
      return 0
    else:
      print("[ERROR]MapStat function cannot find defined type.")
      Kernal.ErrChk()
      return 1
class Wbase:#Weapon system class.
  def __init__(self):pass
  @staticmethod
  def EventAmmoPick(type,amount):#built-in function,for picking up the ammunation box event
    global ammo9,ammo9max,ammo357,ammo357max
    if type==1:
      if ammo9<=ammo9max:
        ammo9+=amount
        return 1
    if type==2:
      if ammo357<=ammo357max:
        ammo357+=amount
        return 2
  @staticmethod
  def WeaponClip(type):#built-in function,for detect clips in gun.
    global inclip9,inclip357,ammo357,ammo9
    if type==1:
      if inclip9==0 and ammo9>=18:
        reload9=0
        ammo9-=18
        inclip9+=18
        reload9=1
        return 1
    elif type==2:
      if inclip357==0 and ammo357>=6:
        reload357=0
        ammo357-=6
        inclip357+=6
        reload357=1
        return 2
class Assets:#asset class
  def __init__(self):pass
  @staticmethod
  def c0a0():#map define,a debug map.
    set_color(10,180,10)
    fill_rect(0,0,500,300)
    set_color(140,140,140)
    fill_rect(60,35,60,35)
    return 0
  @staticmethod
  def c1a0():#map define
    set_color(200,200,90)
    fill_rect(0,0,500,300)
    set_color(170,170,255)
    fill_rect(0,40,80,300)
    fill_rect(160,40,80,300)
    set_color(0,0,0)
    draw_line(240,0,240,300)
    set_color(205,150,20)
    fill_rect(120,120,7,15)
    fill_rect(120,150,7,15)
    set_color(10,250,15)
    fill_circle(123,90,3)
    set_color(10,10,190)
    fill_rect(80,0,80,5)
    set_color(205,150,20)
    fill_rect(40,0,10,5)
    fill_rect(180,0,10,5)
    set_color(0,0,0)
    draw_line(-25,25,15,25)
    set_color(160,10,10)
    fill_rect(45,10,15,10)
    set_color(0,0,0)
    draw_rect(100,100,50,50)
    return 0
  @staticmethod
  def gmanintlol():#an opening function.
    r=0
    b=0
    g=0
    for i in range(255):
      set_color(0,0,0)
      fill_rect(0,0,500,300)
      r+=1;b+=1;g+=1
      set_color(r,g,b)
      draw_text(120,120,"HALF-LIFE²")
      paint_buffer()
      clear()
    sleep(1)
    set_color(0,0,0)
    fill_rect(0,0,500,300)
    set_color(255,255,255)
    draw_text(120,120,"HALF-LIFE²")
    set_color(210,210,255)
    draw_text(20,180,str(ActionUI.DispLanguage("gofuckyourself")))
    paint_buffer()
    sleep(0.7)
    set_color(0,0,0)
    r=0
    g=0
    b=0
    for i in range(25):
      fill_rect(0,0,500,300)
      set_color(210,210,255)
      r+=10;b+=10;g+=10
      set_color(r,g,b)
      paint_buffer()
      sleep(0.01)
    set_pen("thin","solid")
    return 0
  @staticmethod
  def gmanintro():#Opening
    r=0;g=0;b=0;x=0;y=0;x1=0;y1=0
    set_pen("thin","solid")
    for i in range(255):
      set_color(0,0,0)
      fill_rect(0,0,500,300)
      r+=1;b+=1;g+=1
      set_color(r,g,b)
      draw_text(120,120,"HALF-LIFE²")
      paint_buffer()
      clear()
    sleep(3)
    set_color(0,0,0)
    fill_rect(0,0,500,300)
    set_color(255,255,255)
    draw_text(120,120,"HALF-LIFE²")
    set_color(210,210,255)
    draw_text(20,180,str(ActionUI.DispLanguage("riseandshine")))
    paint_buffer()
    sleep(3)
    set_color(0,0,0)
    r=0
    g=0
    b=0
    for i in range(25):
      fill_rect(0,0,500,300)
      set_color(210,210,255)
      draw_text(20,180,str(ActionUI.DispLanguage("riseandshine")))
      r+=10;b+=10;g+=10
      set_color(r,g,b)
      sleep(0.01)
    paint_buffer()
    sleep(1)
    for i in range(25):
      fill_rect(0,0,500,300)
      r-=10;b-=10;g-=10
      set_color(r,g,b)
      sleep(0.01)
    set_color(255,255,255)
    paint_buffer()
    for i in range(50):
      draw_line(x,y,x1,y)
      x=randint(0,500);x1=x+30
      y=randint(0,300);
    set_color(210,210,255)
    draw_text(20,180,str(ActionUI.DispLanguage("sleepingonthejob")))
    draw_text(20,190,str(ActionUI.DispLanguage("effortoftheworld")))
    draw_text(20,200,str(ActionUI.DispLanguage("em")))
    paint_buffer()
    sleep(7)
    set_color(0,0,0)
    fill_rect(0,0,500,300)
    set_color(210,210,255)
    draw_text(20,180,str(ActionUI.DispLanguage("yourhourhascome")))
    paint_buffer()
    sleep(5)
    set_color(0,0,0)
    fill_rect(0,0,500,300)
    set_color(210,210,255)
    draw_text(20,180,str(ActionUI.DispLanguage("rightman")))
    draw_text(20,190,str(ActionUI.DispLanguage("maketheworld")))
    paint_buffer()
    sleep(5)
    r=0
    g=0
    b=0
    for i in range(25):
      fill_rect(0,0,500,300)
      set_color(210,210,255)
      draw_text(20,180,str(ActionUI.DispLanguage("rightman")))
      draw_text(20,190,str(ActionUI.DispLanguage("maketheworld")))
      r+=10;b+=10;g+=10
      set_color(r,g,b)
      sleep(0.01)
      paint_buffer()
    sleep(2)
    for i in range(25):
      fill_rect(0,0,500,300)
      r-=10;b-=10;g-=10
      set_color(r,g,b)
      sleep(0.01)
    set_color(210,210,255)
    draw_text(20,180,str(ActionUI.DispLanguage("wakeup")))
    paint_buffer()
    sleep(3)
    set_color(255,255,255)
    for i in range(50):
      draw_line(x,y,x1,y)
      x=randint(0,500);x1=x+30
      y=randint(0,300);
    set_color(210,210,255)
    draw_text(20,190,str(ActionUI.DispLanguage("smell")))
    paint_buffer()
    sleep(2)
    for i in range(25):
      fill_rect(0,0,500,300)
      set_color(210,210,255)
      draw_text(20,190,str(ActionUI.DispLanguage("smell")))
      r+=10;b+=10;g+=10
      set_color(r,g,b)
      sleep(0.01)
      paint_buffer()
    sleep(1)
    clear()
    return 0
  @staticmethod
  def MainMenu():#main menu function
    posy=20;rgbr=10;rgbb=100;posx=0;w=0;h=0;g=0;b=0;r=0
    set_pen("medium","solid")
    a=0
    set_color(0,0,100)
    fill_rect(0,0,500,300)
    for i in range(1,200):
      fill_rect(0,posy,500,300)
      set_color(rgbr,0,rgbb)
      rgbr+=10;posy+=11.3
      if rgbr >= 240:
        break
    set_color(215,0,100)
    fill_rect(0,205,500,300)
    set_color(220,220,220)
    for i in range(100):
      fill_circle(randint(0,500),randint(0,100),1)
    fill_circle(100,50,5);l=0;m=0;set_pen("thin","solid")
    for i in range(2):
      draw_line(l,m,m,l)
      l=randint(60,80);m=randint(20,60)
    set_pen("thick","solid")
    set_color(0,0,100)
    fill_circle(103,50,4)
    set_color(250,250,0);posx=-30
    set_color(58,58,150)
    fill_rect(220+20,0,37,300)
    set_color(55,55,105)
    fill_rect(239+20,69,18,57)
    set_color(54,54,145)
    fill_rect(242+21,69,5,57);posy=72
    for i in range(5):
      fill_rect(239+20,posy,17,5)
      posy+=11
    set_color(5,10,100)
    set_pen("thin","solid")
    for i in range(randint(7,10)):
      draw_line(239,randint(82,95),randint(181,230),300)
      draw_line(279,randint(82,95),randint(280,330),300)
    set_color(55,55,163)
    fill_rect(242+20,49,18,57)
    fill_rect(265,106,5,13)
    fill_rect(265+9,106,5,20)
    set_color(255,0,0)
    fill_circle(randint(20,210),randint(2,180),2)
    set_color(255,255,255)
    draw_text(10,80,"HALF-LIFE²")
    draw_text(150,17,GAMEVER)
    set_pen("thin","solid")
    return 0
def main():#main function.It's a very standard template for engine.
  ActionUI.DispUi(0,0,9)
  inmenu=True
  global ingamemod,modscripts,langtype,mapslt,dev,dr,emptysave,psx,v_live,v_hev,psy,weapon_crb,debugs,v_hev,weapon_physcnn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit,usemod
  StdUtil.ConsoleLog(4)
  while True:#game logic loop
    if inmenu==True:#menu guard
      Kernal.ResetGame()
      Assets.MainMenu()
      ActionUI.DispUi(0,0,4)
      gc.collect()
      paint_buffer()
      while True:#main menu
        k=get_key()
        emptysave=IO.Load(True,"emptysave",False,None)
        if k=="enter":
          Assets.gmanintro()
          inmenu=False
          Actors.King.Init(1,0,0,0)
          Actors.King.Init(2,95,95)
          Actors.King.Init(3,5,5)
          Actors.King.Init(4,100)
          Actors.King.Init(5,0)
          Actors.King.Init(6,0,0)
          Actors.King.Init(7,0,0)
          Actors.King.Init(8,0)
          Actors.King.Init(9,0)
          Actors.King.Init(10,0)
          Actors.King.Init(11,0)
          Actors.King.Init(12,0)
          break
        elif k=="b":
          for i in range(2):
            if emptysave==1:IO.Load()
          if emptysave==1:continue
          IO.Load()
          inmenu=False
          break
        elif k=="c":
          IO.Delete()
        elif k=="menu":
          ActionUI.DispUi(0,0,9)
          Assets.MainMenu()
          ActionUI.DispUi(0,0,4)
          paint_buffer()
        elif k=="a":
          Assets.gmanintlol()
          inmenu=False
          Actors.King.Init(1,0,0,0)
          Actors.King.Init(2,95,95)
          Actors.King.Init(3,5,5)
          Actors.King.Init(4,100)
          Actors.King.Init(5,0)
          Actors.King.Init(6,0,0)
          Actors.King.Init(7,0,0)
          Actors.King.Init(8,0)
          Actors.King.Init(9,0)
          Actors.King.Init(10,0)
          Actors.King.Init(11,0)
          Actors.King.Init(12,0)
          break
        elif k=="tab":
          while True:
            k=get_key()
            clear()
            StdUtil.SettingMenu()
            paint_buffer()
            if k=="a":
              if dr==True:dr=False
              else:dr=True
            elif k=="b":
              if dev==True:dev=False
              else:dev=True
            elif k=="c":#add more conditions if you have more language.
              if langtype==1:
                langtype=2
              elif langtype==2:
                langtype=1
            elif k=="d":
              if usemod==True:usemod=False
              else:usemod=True
            elif k=="s":
              Kernal.SaveCfg()
            elif k=="esc":
              ActionUI.DispUi(0,0,9)
              Assets.MainMenu()
              ActionUI.DispUi(0,0,4)
              paint_buffer()
              break
        elif k=="esc":
          StdUtil.ConsoleLog(3)
          Kernal.quit()
      clear()
      gc.collect()
    if dr==True:StdUtil.ConsoleLog(1)#print a log when screen update.
    StdUtil.MapStat()#logic check in here,define your trigger in this function.
    if v_live<=20 and v_live>=0:UniFX.LowHealth()
    if v_live<=0:#death detecting
      ActionUI.DispUi(0,0,7)
      Actors.King.Draw()
      paint_buffer()
      StdUtil.ConsoleLog(7)
      while get_key()!="unknow":
         k=get_key()
         if k=="enter":
           IO.Load()
           break
    for key in ["unknow"]:
      while k!=key:
        k=get_key()
        Kernal.WaitUpdate()
        StdUtil.MapStat()
        if ingamemod=="ingamemod" and tk.mod_info(3)=="ingamemod"and usemod==True:tk.mod_main()
        if item_suit==1:#hud
          ActionUI.DispUi(0,0,6)
          ActionUI.DispUi(0,0,8)
        ActionUI.DispUi(0,0,2)
        Actors.King.Draw()
        if v_live<=20 and v_live>=0:
          UniFX.LowHealth()
        if k=="u" and dev==True:
          if debugs==False:
            debugs=True
            print("[INFO]Debug drawing enabled.")
          else:
            debugs=False
            print("[INFO]Debug drawing disabled.")
            break
        elif k=="right":
          psx+=5
          break
        elif k=="left":
          psx-=5
          break
        elif k=="up":
          psy-=5
          break
        elif k=="down":
          psy+=5
          break
        elif k=="t" and dev==True:
          v_hev-=10
          break
        elif k=="s"and dev==True:
          v_hev+=10
          break
        elif k=="z"and dev==True:
          v_live-=10
          break
        elif k=="h"and dev==True:
          Wbase.EventAmmoPick(1,18)
          Wbase.EventAmmoPick(2,6)
          break
        elif k=="y"and dev==True:
          v_live+=10
          break
        elif k=="tab" and dev==True:
          gc.collect()
          print("[DEBUG]gc collect completed.")
          break
        elif k=="d":#maybe create a new function to recall the effects.
          if wpnslt==3 and reload9==0 and weapon_pst==1 and inclip9!=0:
            inclip9-=1
            UniFX.BulletFX.BltFlr(1)
          if wpnslt==4 and reload357==0 and weapon_357==1 and inclip357!=0:
            inclip357-=1
            UniFX.BulletFX.BltFlr(2)
          if wpnslt==1 and weapon_crb==1:
            UniFX.BulletFX.BltFlr(3)
          if wpnslt==2 and weapon_physcnn==1:
            UniFX.BulletFX.BltFlr(4)
          paint_buffer()
          sleep(0.1)
          break
        elif k=="r":
          if wpnslt==3 and reload9==0 and weapon_pst==1 and inclip9!=0:
            inclip9-=1
            UniFX.BulletFX.BltFlr(5)
          if wpnslt==4 and reload357==0 and weapon_357==1 and inclip357!=0:
            inclip357-=1
            UniFX.BulletFX.BltFlr(6)
          if wpnslt==1 and weapon_crb==1:
            UniFX.BulletFX.BltFlr(7)
          if wpnslt==2 and weapon_physcnn==1:
            UniFX.BulletFX.BltFlr(8)
          paint_buffer()
          sleep(0.1)
          break
        elif k=="j":
          if wpnslt==3 and reload9==0 and weapon_pst==1 and inclip9!=0:
            inclip9-=1
            UniFX.BulletFX.BltFlr(9)
          if wpnslt==4 and reload357==0 and weapon_357==1 and inclip357!=0:
            inclip357-=1
            UniFX.BulletFX.BltFlr(10)
          if wpnslt==1 and weapon_crb==1:
            UniFX.BulletFX.BltFlr(11)
          if wpnslt==2 and weapon_physcnn==1:
            UniFX.BulletFX.BltFlr(12)
          paint_buffer()
          sleep(0.1)
          break
        elif k=="l":
          if wpnslt==3 and reload9==0 and weapon_pst==1 and inclip9!=0:
            inclip9-=1
            UniFX.BulletFX.BltFlr(13)
          if wpnslt==4 and reload357==0 and weapon_357==1 and inclip357!=0:
            inclip357-=1
            UniFX.BulletFX.BltFlr(14)
          if wpnslt==1 and weapon_crb==1:
            UniFX.BulletFX.BltFlr(15)
          if wpnslt==2 and weapon_physcnn==1:
            UniFX.BulletFX.BltFlr(16)
          paint_buffer()
          sleep(0.1)
          break
        elif k=="f":
          if wpnslt==3:#Dont be afraid from lambda, its just letting the method waiting for wait function.
            StdUtil.WaitStart(150,lambda:Wbase.WeaponClip(1))
          elif wpnslt==4:
            StdUtil.WaitStart(300,lambda:Wbase.WeaponClip(2))
          break
        elif k=="menu"and dev==True:
          weapon_crb=1
          weapon_physcnn=1
          weapon_pst=1
          weapon_357=1
          item_suit=1
        elif k=="1":
          if item_suit==1:pass
          else:break
          ActionUI.DispUi(0,0,5)
          if weapon_crb==1:
            ActionUI.DispUi(0,0,10)
          if weapon_physcnn==1:
            ActionUI.DispUi(0,0,11)
          paint_buffer()
          while k!="0":
            k=get_key()
            if k=="0":
              clear()
              StdUtil.MapStat()
              Actors.King.Draw()
              break
            elif k=="1" and weapon_crb==1:
              wpnslt=1
              clear()
              StdUtil.MapStat()
              Actors.King.Draw()
              break
            elif k=="2" and weapon_physcnn==1:
              wpnslt=2
              clear()
              StdUtil.MapStat()
              Actors.King.Draw()
              break
        elif k=="2":
          if item_suit==1:pass
          else:break
          ActionUI.DispUi(0,0,5)
          if weapon_pst==1:
            ActionUI.DispUi(0,0,12)
          if weapon_357==1:
            ActionUI.DispUi(0,0,13)
          paint_buffer()
          while k!="0":
            k=get_key()
            if k=="0":
              clear()
              StdUtil.MapStat()
              Actors.King.Draw()
              break
            elif k=="1" and weapon_pst==1 and ammo9!=0:
              wpnslt=3
              clear()
              StdUtil.MapStat()
              Actors.King.Draw()
              break
            elif k=="2" and weapon_357==1 and ammo357!=0:
              wpnslt=4
              clear()
              StdUtil.MapStat()
              Actors.King.Draw()
              break
            paint_buffer()
          break
        elif k=="esc":
          while True:#pause menu
            StdUtil.PauseMenu()
            ky="0"
            paint_buffer()
            for ky in["Null"]:
              while k!=ky:
                clear()
                StdUtil.PauseMenu()
                k=get_key()
                emptysave=IO.Load(True,"emptysave",False,None)
                ActionUI.DispUi(0,0,2)
                paint_buffer()
                if k=="esc":
                  clear()
                  break
                elif k=="q":
                  StdUtil.ConsoleLog(3)
                  Kernal.quit(0)
                  break
                elif k=="tab":
                  while True:
                    k=get_key()
                    clear()
                    StdUtil.SettingMenu()
                    paint_buffer()
                    if k=="a":
                      if dr==True:dr=False
                      else:dr=True
                    elif k=="b":
                      if dev==True:dev=False
                      else:dev=True
                    elif k=="c":#add more conditions if you have more language.
                      if langtype==1:
                        langtype=2
                      elif langtype==2:
                        langtype=1
                    elif k=="d":
                      if usemod==False:usemod=True
                      else:usemod=False
                    elif k=="s":
                      Kernal.SaveCfg()
                    elif k=="esc":
                      ActionUI.DispUi(0,0,9)
                      paint_buffer()
                      clear()
                      break
                elif k=="d":
                  IO.Delete()
                elif k=="s":
                  IO.Save()
                elif k=="l":
                  if emptysave==1:
                    for i in range(2):
                      if emptysave==1:IO.Load()
                  if emptysave==1:continue
                  IO.Load()
                  break
                elif k=="menu":
                  print("[INFO]Server stopped.")
                  ActionUI.DispUi(0,0,9)
                  inmenu=True
                  break
                elif k=="u":
                  if debugs==False:
                    debugs=True
                    print("[INFO]Debug drawing enabled.")
                  else:
                    debugs=False
                    print("[INFO]Debug drawing disabled.")
              break
            break
          break
        paint_buffer()
      break
  return 0
if (__name__=="__main__"):#all program starts from here.
  Kernal.Init(1)
  Kernal.Console()
  Kernal.GameLauncher()