#IlChelcciCore 2D engine-Core module and source code.
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
#========End of license texts===========
#Please use PascalCase to name func, class.
#In main function, everything is clean and
#visible, if more features are needed, add
#them in the main function. But sometimes you
#have to add something in built-in functions.
#Every class, functions in here are all with
#examples, you can learn engine from examples.
#return codes:0~99+ is success,-1 is error.(default)
#some func is special,like Trigger and MouseBox.
#it is using minx miny and maxx maxy not x,y,w,h.
#maxx and maxy can be found as minx+width
#and miny+height.
#for example, 125 is minx,width is 100,then
#just add minx and width together, which is 225.
#same for miny and maxy, just add the height.
#if you need grid,run grid.py.
#resolution is hard to set, do not touch unless you have to.
#0,0,0,0 is default resolution.
#if you're trying to import engine on other file,do
#not use functions with a leading underscore.
import sys
from random import randint
from time import *
showbar=bool(False);
apptitle=str("Half-Life 2");
novid=bool(False);
arogmmd=bool(False);
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
plspd=int(5);
kingignores=str("");
autoloadmod=bool(False);
dev=bool(False);
openingtype=int(1);
usemod=bool(False);
dr=bool(False);
debugs=bool(False);
erxt=int(0);
key=str("");
mapslt=int(0);
psx=int(0);
psy=int(0);
v_hev=int(0);
PI=float(3.14159265358980);
GAMEVER=str("IlChelcciCore 40 Build(0167)");
VERINT=int(167);
DEBUGDATE=str("2026/01/09");
GAMETITLE=str("IlChelcciCore engine built-in example.");
COMPANY=str("Made by axnut123");
COPYRIGHT=str("(C)Haoriwa 2024-2025, all rights reserved.");
wpnslt=int(0);
permissionlvl=int(1);
item_suit=int(0);
weapon_crb=int(0);
weapon_pcn=int(0);
weapon_pst=int(0);
weapon_357=int(0);
ammo357=int(0);
ammo9=int(0);
v_live=int(100);
ammo9max=int(180);
ammo357max=int(12);
inclip9=int(0);
inclip357=int(0);
vtk=bool(False);
ingamemod=str("");
modscripts=list([]);
scrgeometx=int(0);
scrgeomety=int(0);
scrgeometmx=int(0);
scrgeometmy=int(0);
ignoreverchk=bool(False);
gcthresholdint=int(-1);
runmod=bool(False);
runprgm=str("");
released=int(0);
totalmem=int(0);
gcenb=None;
banned=int(0);
newuser=int(0);
emptysave=int(1);#True or False does not work.
def Help(hptp=0):#built-in function, help infos. fill your own help in here.
  if hptp==0:
    return "Welcome to IlChelcciCore for TI-Nspire. For further information, please go to page 1.1."
def version(vertype=0):#built-in function, version output. fill your version here.
  global GAMEVER,DEBUGDATE,GAMETITLE,COMPANY,COPYRIGHT
  if vertype==0:return GAMEVER
  elif vertype==1:return DEBUGDATE
  elif vertype==2:return GAMETITLE
  elif vertype==3:return COPYRIGHT
  elif vertype==4:return COMPANY
  elif vertype==5:return VERINT
  else:raise ValueError("Unknown arguments.")
class CfgError(Exception):pass
class BadArguments(Exception):pass
class UnknownError(Exception):pass
class ModError(Exception):pass
class IOError(Exception):pass#MicroPy does not have this.
class GameError(Exception):pass#Error classes.
class Kernel:#Code base class.
  def __init__(self):pass
  @staticmethod
  def DelObj(objName,logout=False):#built-in function, deletd an object located in globals() dict.
    globals().pop(objName)
    if logout:Kernel.Cout.Info("Deleted '%s'."%(objName))
    gc.collect()
    return 0
  @staticmethod
  def GetVar(varName,logout=False):#built-in function, get a global variable.
    v=globals().get(varName)
    if logout and v is not None:
      Kernel.Cout.Info("Variable '%s' is: %s."%(varName,v))
    elif logout and v is None:Kernel.Cout.Info("Variable '%s' is not defined."%(varName))
    return v
  @staticmethod
  def ConVar(varName,value,logout=False):#built-in function, for change a variable.
    globals()[varName]=value
    if logout:Kernel.Cout.Info("Changed variable '%s' to %s."%(varName,value))
    return varName,value
  @staticmethod
  def KrTerminateProcess(code=None):#built-in function, for forcibly stop this engine.
    Kernel.Cout.Info("Trying to stop forcibly by code:%s.\nIf terminate fail, hold esc key for 5 secs to stop."%(code))
    gc.collect()
    blocks=[]
    while True:blocks.append(bytearray(1024*1024))
  @staticmethod
  def quit(code=None):#built-in function, in nspire cx ii python the quit function is not defined.
    StdUtil.ConsoleLog(3,code)
    gc.collect()
    raise SystemExit(code)
  @staticmethod
  def GetTotalMem():#built-in function, for getting total memory.
    Kernel.ConVar("totalmem",gc.mem_alloc()+gc.mem_free())
    Kernel.Cout.DevInfo("Total mem is %s."%(globals().get("totalmem")))
    return Kernel.GetVar("totalmem")
  @staticmethod
  def GetGcState():#built-in function, get gc is enabled state.
    Kernel.ConVar("gcenb",gc.isenabled())
    Kernel.Cout.DevInfo("Gc enabled is now %s."%(gcenb))
    return Kernel.GetVar("gcenb")
  @staticmethod
  def SetGcState(state):#built-in function, for set gc enabled.
    if state:
      gc.enable()
      Kernel.Cout.Info("Gc enabled.")
      Kernel.ConVar("gcenb",True)
      return True
    else:
      gc.disable()
      Kernel.Cout.Info("Gc disabled.")
      Kernel.ConVar("gcenb",False)
      return False
  @staticmethod
  def ToggleGcState():#built-in function, for toggle gc enabled.
    global gcenb
    if gcenb:
      Kernel.SetGcState(False)
      Kernel.Cout.DevInfo("Gc disabled.")
      return False
    else:
      Kernel.SetGcState(True)
      Kernel.Cout.DevInfo("Gc enabled.")
      return True
  @staticmethod
  def SaveCfg():#built-in function, saving cfg variable to nspire document.
    global userid,arogmmd,ignoreverchk,scrgeometx,scrgeomety,scrgeometmx,scrgeometmy,gcthresholdint,autoloadmod,langtype,dev,dr,usemod,novid,modamount,erxt,openingtype,gcenb,showbar
    suserid=str(userid)
    try:
      IO.Save(True,"optp"+suserid,int(openingtype))
      IO.Save(True,"scgx"+suserid,scrgeometx)
      IO.Save(True,"scgy"+suserid,scrgeomety)
      IO.Save(True,"scgmx"+suserid,scrgeometmx)
      IO.Save(True,"scgmy"+suserid,scrgeometmy)
      if langtype==1:
        IO.Save(True,"langtype"+suserid,1)
      elif langtype==2:
        IO.Save(True,"langtype"+suserid,2)
      else:
        IO.Save(True,"langtype"+suserid,1)
        Kernel.Cout.Warning("Language type not found, saving as default language.")
        Kernel.ErrChk(1,"Language type not found.")
      IO.Save(True,"permlvl"+suserid,permissionlvl)
      IO.Save(True,"erxt"+suserid,int(erxt))
      IO.Save(True,"modamount"+suserid,modamount)
      IO.Save(True,"gcthint"+suserid,int(gcthresholdint))
      if showbar:IO.Save(True,"showbar"+suserid,1)
      else:IO.Save(True,"showbar"+suserid,0)
      if novid:IO.Save(True,"novid"+suserid,1)#True or false dosent work here. use 1 or 0.
      else:IO.Save(True,"novid"+suserid,0)
      if ignoreverchk:IO.Save(True,"ignoreverchk"+suserid,1)
      else:IO.Save(True,"ignoreverchk"+suserid,0)
      if gcenb:IO.Save(True,"gcenb"+suserid,1)
      else:IO.Save(True,"gcenb"+suserid,0)
      if autoloadmod:IO.Save(True,"autoloadmod"+suserid,1)
      else:IO.Save(True,"autoloadmod"+suserid,0)
      if dev:IO.Save(True,"dev"+suserid,1)
      else:IO.Save(True,"dev"+suserid,0)
      if dr:IO.Save(True,"dr"+suserid,1)
      else:IO.Save(True,"dr"+suserid,0)
      if usemod:IO.Save(True,"usemod"+suserid,1)
      else:IO.Save(True,"usemod"+suserid,0)
      if arogmmd:IO.Save(True,"arogmmd"+suserid,1)
      else:IO.Save(True,"arogmmd"+suserid,0)
      Kernel.Cout.Info("Cfg saving success.")
      return 0
    except Exception as e:
      Kernel.Cout.Error("Cfg saving failed."+str(e))
      Kernel.ErrChk(3,"Failed to save cfgs.")
      return -1
  @staticmethod
  def Init(inittp):#built-in function.for init cfgs or other files engine needed.
    global userid,showbar,ignoreverchk,permissionlvl,arogmmd,gcenb,scrgeomety,scrgeometx,scrgeometmx,scrgeometmy,autoloadmod,gcthresholdint,dev,dr,novid,langtype,usemod,modamount,erxt,mod,released,openingtype
    suserid=str(userid)
    if inittp==1:
      try:
        cfg0=IO.Load(True,"gcenb"+suserid)
        cfg1=IO.Load(True,"novid"+suserid)
        cfg2=IO.Load(True,"dev"+suserid)
        cfg3=IO.Load(True,"dr"+suserid)
        cfg4=IO.Load(True,"usemod"+suserid)
        cfg5=IO.Load(True,"autoloadmod"+suserid)
        cfg6=IO.Load(True,"arogmmd"+suserid)
        cfg7=IO.Load(True,"ignoreverchk"+suserid)
        cfg8=IO.Load(True,"showbar"+suserid)
        openingtype=IO.Load(True,"optp"+suserid)
        permissionlvl=int(IO.Load(True,"permlvl"+suserid))
        erxt=IO.Load(True,"erxt"+suserid)
        langtype=IO.Load(True,"langtype"+suserid)
        released=IO.Load(True,"released")
        scrgeometx=IO.Load(True,"scgx"+suserid)
        scrgeomety=IO.Load(True,"scgy"+suserid)
        scrgeometmx=IO.Load(True,"scgmx"+suserid)
        scrgeometmy=IO.Load(True,"scgmy"+suserid)
        modamount=IO.Load(True,"modamount"+suserid)
        gcthresholdint=IO.Load(True,"gcthint"+suserid)
        if cfg0==1:gcenb=True
        else:gcenb=False
        if cfg1==1:novid=True
        else:novid=False
        if cfg2==1:dev=True
        else:dev=False
        if cfg3==1:dr=True
        else:dr=False
        if langtype not in (1,2):
          langtype=1
          Kernel.Cout.Warning("Language type not found, using default language.")
          Kernel.ErrChk(1,"Language type not found.")
        if cfg4==1:usemod=True
        else:usemod=False
        if cfg5==1:autoloadmod=True
        else:autoloadmod=False
        if cfg6==1:arogmmd=True
        else:arogmmd=False
        if cfg7==1:ignoreverchk=True
        else:ignoreverchk=False
        if cfg8==1:showbar=True
        else:showbar=False
        del cfg0,cfg1,cfg2,cfg3,cfg4,cfg5,cfg6,cfg7,cfg8
        if autoloadmod or arogmmd:Kernel._ModHandler(2)
        gc.threshold(gcthresholdint)
        Kernel.GetTotalMem()
        gc.collect()
        Kernel.Cout.Info("Config loading process completed.")
        return 1
      except Exception as e:
        Kernel.Cout.Error("Failed on trying to load configs."+str(e))
        Kernel.ErrChk(3,"Cfg load process failed.")
        return -1
    elif inittp==2:
      pt=get_platform()
      if pt not in ("hh","ios","dt"):
        use_buffer()
        set_color(210,10,10)
        fill_rect(0,0,500,300)
        set_color(240,240,240)
        draw_text(10,80,ActionUI.DispLanguage("plterr"))
        draw_text(10,100,ActionUI.DispLanguage("supsys")+str(pt)+".")
        draw_text(10,120,ActionUI.DispLanguage("prsesc"))
        paint_buffer()
        Kernel.Cout.Fatal("Platform not supported.")
        while get_key()!="esc":pass
        Kernel.quit(-1)
      else:
        del pt
        gc.collect()
        Kernel.Cout.Preload("Platform check done.")
        return 2
  @staticmethod
  def KrErrChk(errtype,reason="Unknown reason.",forceraise=False):#built-in function, for raise any error.
    global erxt
    if erxt==1 or forceraise:
      if not forceraise:Kernel.Cout.Debug("Error or warning encountered,\nstopped engine.")
      else:Kernel.Cout.Debug("Forcibly raised an error!")
      gc.collect()
      exec("raise %s('%s')"%(errtype,reason))
  @staticmethod
  def ErrChk(errtype=None,reason="Unknown reason.",forceraise=False):#built-in function, error check. also used in command "forceexitonerror".
    global erxt
    if erxt==1 or forceraise:
      if not forceraise:Kernel.Cout.Debug("Error or warning encountered,\nstopped engine.")
      else:Kernel.Cout.Debug("Forcibly raised an error!")
      gc.collect()
      if errtype==1:raise BadArguments(reason)
      elif errtype==2:raise IOError(reason)
      elif errtype==3:raise CfgError(reason)
      elif errtype==4:raise ModError(reason)
      elif errtype==5:raise GameError(reason)
      else:raise UnknownError(reason)
  @staticmethod
  def _ModHandler(hdtp):#built-in function,for managing mods.
    global vtk,mod,usemod,ingamemod,ignoreverchk
    if hdtp==1:
      try:
        del mod
        Kernel.Cout.Info("Mod is uninstalled, but reboot is\nrecommended.")
        gc.collect()
      except Exception as e:
        Kernel.Cout.Error("Mod cannot be uninstalled, there is no mod installed.")
        Kernel.ErrChk(4,"Cannot uninstall mod.")
      vtk=False
      usemod=False
      Kernel.Cout.Info("Mod disable process done.")
    elif hdtp==2:
      if vtk!=True:
        Kernel.Cout.Info("Mod is loading... if mod loading amount is more than 100, it will take a long time to load,\nplease wait.")
        for i in range(int(modamount)):
          try:
            mod=__import__("ilcc_addon_main"+str(i))
            modscripts.append(mod)
          except ImportError:
            continue
        vtk=True
        Kernel.Cout.Info("Mod init process done.")
        try:
          ingamemod=mod.mod_type()
        except:
          ingamemod=str("")
          vtk=False
          Kernel.Cout.Info("No mod file detected.")
      else:
        Kernel.Cout.Info("Mod already init.")
        Kernel.ErrChk(4,"Repeating init.")
    elif hdtp==3:
      if vtk and ingamemod!="ingamemod":
        usemod=True
        Kernel.Cout.Info("Mod is running.")
        return 0
      else:
        Kernel.Cout.Error("Mod script not found or mod type is not supported.")
        Kernel.ErrChk(4,"Mod not found.")
        return -1
    elif hdtp==4:
      Kernel.Cout.Msg("Warning: do not let 2 types of mods installed together.")
      if vtk:
        Kernel.Cout.Msg(mod.mod_type())
        Kernel.Cout.Msg(mod.mod_info(draw=False))
      else:
        Kernel.Cout.Error("Mod is not found.")
        Kernel.ErrChk(4,"Mod not found.")
    elif hdtp==5:
      if ingamemod=="ingamemod" and mod.mod_type()=="ingamemod"and usemod and mod is not None and vtk:mod.mod_main(ignoreverchk)
    else:
      Kernel.Cout.Error("Unknown argument.")
      Kernel.ErrChk(1,"Unknown argument.")
      return -1
  @staticmethod
  def WaitUpdate():#built-in function. for check the wait tick.
    global active,action,endtick
    if active and ticks_cpu()>=endtick:
      active=False
      if action:
        action()
        action=None
  class Cout:#console output class.
    def __init__(self):pass
#Example for Cout class:
#Kernel.Cout.Msg("hello")
#output: hello
#Kernel.Cout.Info("hello")
#output: [INFO]hello
#kernel.Cout.DevMsg("hello for dev")
#when dev is True then output: hello for dev
#otherwise it will not print the message.
#Kernel.Cout.Msg("hello but no auto return",autoret=False)
#output: hello but no auto return
#which means it will not add "\n" at the endline.
#Kernel.Cout.Msg("hello but no flush",flush=False)
#output: hello but no flush
#which means the text on console might not showing instantly.
    @staticmethod
    def _CoutBase(ctp,text,autoret,flush):#built-in function. Base function for console output methods.
      CHAR={0:"",1:"[WARN]",2:"[ERROR]",3:"[FATAL]",4:"[DEBUG]",5:"[INFO]",6:"[CONSOLE]",7:"[PRE-LOAD]",8:"[IO]"}
      if autoret:e="\n"
      else:e=""
      c=CHAR.get(ctp)
      sys.stdout.write(c+text+e)
      if flush:sys.stdout.flush()
      return 0
    @staticmethod
    def Msg(text,autoret=True,flush=True):Kernel.Cout._CoutBase(0,text,autoret,flush)
    @staticmethod
    def Warning(text,autoret=True,flush=True):Kernel.Cout._CoutBase(1,text,autoret,flush)
    @staticmethod
    def Error(text,autoret=True,flush=True):Kernel.Cout._CoutBase(2,text,autoret,flush)
    @staticmethod
    def Fatal(text,autoret=True,flush=True):Kernel.Cout._CoutBase(3,text,autoret,flush)
    @staticmethod
    def Debug(text,autoret=True,flush=True):Kernel.Cout._CoutBase(4,text,autoret,flush)
    @staticmethod
    def Info(text,autoret=True,flush=True):Kernel.Cout._CoutBase(5,text,autoret,flush)
    @staticmethod
    def Console(text,autoret=True,flush=True):Kernel.Cout._CoutBase(6,text,autoret,flush)
    @staticmethod
    def Preload(text,autoret=True,flush=True):Kernel.Cout._CoutBase(7,text,autoret,flush)
    @staticmethod
    def IO(text,autoret=True,flush=True):Kernel.Cout._CoutBase(8,text,autoret,flush)
    @staticmethod
    def DevMsg(text,autoret=True,flush=True):
      if dev:Kernel.Cout._CoutBase(0,text,autoret,flush)
    @staticmethod
    def DevWarning(text,autoret=True,flush=True):
      if dev:Kernel.Cout._CoutBase(1,text,autoret,flush)
    @staticmethod
    def DevError(text,autoret=True,flush=True):
      if dev:Kernel.Cout._CoutBase(2,text,autoret,flush)
    @staticmethod
    def DevFatal(text,autoret=True,flush=True):
      if dev:Kernel.Cout._CoutBase(3,text,autoret,flush)
    @staticmethod
    def DevDebug(text,autoret=True,flush=True):
      if dev:Kernel.Cout._CoutBase(4,text,autoret,flush)
    @staticmethod
    def DevInfo(text,autoret=True,flush=True):
      if dev:Kernel.Cout._CoutBase(5,text,autoret,flush)
    @staticmethod
    def DevConsole(text,autoret=True,flush=True):
      if dev:Kernel.Cout._CoutBase(6,text,autoret,flush)
    @staticmethod
    def DevPreload(text,autoret=True,flush=True):
      if dev:Kernel.Cout._CoutBase(7,text,autoret,flush)
    @staticmethod
    def DevIO(text,autoret=True,flush=True):
      if dev:Kernel.Cout._CoutBase(8,text,autoret,flush)
  @staticmethod
  def _ResetGame():#built-in function,for soft reset.
    global plspd,ammo9max,ammo357max,mapslt,psx,v_live,v_hev,plh,plw,plr,plg,plb,psy,weapon_crb,debugs,v_hev,weapon_pcn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit
    plspd=0;mapslt=0;plh=0;plw=0;plg=0;plb=0;plr=0;psx=0;psy=0;v_hev=0;wpnslt=0;item_suit=0;weapon_crb=0;weapon_pcn=0;weapon_pst=0;weapon_357=0;ammo357=0;ammo9=0;v_live=100;ammo9max=180;ammo357max=12;inclip9=0;inclip357=0
    Kernel.Cout.Info("Game reset completed.")
    return 0
  @staticmethod
  def _CreateWindow(geomety,geometx,geometmx,geometmy):#built-in function,for creating window.
    set_window(geometx,geometmx,geomety,geometmy)
    set_color(0,0,0)
    fill_rect(0,0,500,300)
    ActionUI.DispUi(0,0,9)
    use_buffer()#Start buffer system
    paint_buffer()
    Kernel.Cout.Info("Window created with size:\nX:%s,MAXX:%s,Y:%s,MAXY:%s."%(geometx,geometmx,geomety,geometmy))
    return 0
  @staticmethod
  def _GameLauncher():#Built-in function, for game loading process.
    global runmod,novid,usemod,mod,ingamemod,scrgeomety,scrgeometx,scrgeometmx,scrgeometmy,gcthresholdint,runprgm,released,GAMETITLE,DEBUGDATE,GAMEVER,openingtype,COMPANY,COPYRIGHT,gcenb,ignoreverchk
    Kernel.Cout.Preload("Starting console.")
    if not released:Kernel._Console()
    else:
      Kernel.Cout.Console("Console is being ignore and closed because game is in release state.")
      runprgm="Prgm.Main()"#You can change your main entry by editing this string.
      Kernel.Cout.Console("Set default script to function: %s."%(runprgm))
    Kernel.Cout.Info("Engine is now started.")
    gc.collect()
    Kernel.Cout.Info("Engine and game info:\nversion:%s, debug date:%s,\ncompany name:%s,\ncopyright info:%s,\ngame title:'%s'."%(GAMEVER,DEBUGDATE,COMPANY,COPYRIGHT,GAMETITLE))
    StdUtil.ConsoleLog(2)
    Kernel.GetGcState()
    Kernel.SetGcState(gcenb)
    gc.threshold(int(gcthresholdint))
    Kernel.ConVar("menuslt",randint(1,2),True)
    Kernel._CreateWindow(scrgeomety,scrgeometx,scrgeometmx,scrgeometmy)
    if not novid:Kernel.Opening(openingtype)
    if arogmmd and released:
      runmod=True
      usemod=True
      Kernel.Cout.Info("Auto run out game mod enabled.")
    StdUtil.ConsoleLog(5)
    if ingamemod=="ingamemod":usemod=False
    if runmod and usemod and ingamemod=="outgamemod" and ingamemod is not None:
      clear()
      Kernel.Cout.Info("Trying to load mod script.")
      mod.mod_main(ignoreverchk)
    else:
      Kernel.Cout.Info("Mod loader was not enabled,\nrunning:%s."%(runprgm))
      usemod=True
      exec(runprgm)
    return 0
  @staticmethod
  def _Console():#built-in function,for console.
    global arogmmd,runprgm,scrgeometx,scrgeomety,scrgeometmx,scrgeometmy,ingamemod,modscripts,usemod,vtk,erxt,novid,mod,dev,dr,langtype,usemod,modamount,autoloadmod,gcthresholdint,kingignores,released,GAMEVER,DEBUGDATE,GAMETITLE,openingtype,COMPANY,COPYRIGHT,permissionlvl,ignoreverchk
    Kernel.Cout.Preload("Console is created because game is in debug state.")
    while True:
      g=str(input("]"))
      permissionlvl=int(permissionlvl)
      if permissionlvl>=1 and g=="run"or permissionlvl>=1 and g=="start":
        Kernel.ConVar("runmod",False,True)
        Kernel.Cout.Console("Running engine.")
        runprgm="Prgm.Main()"#You can change your main entry by editing this string.
        del g
        break
      elif g=="begin"and permissionlvl>=3:
        Kernel.ConVar("runmod",False,True)
        runprgm=str(input("function name:"))
        del g
        break
      elif g=="ignoreverchkonmod"and permissionlvl>=3:
        if ignoreverchk:ignoreverchk=True
        else:ignoreverchk=False
      elif g=="releasegame"and permissionlvl>=4:
        Kernel.Cout.Msg("Are you sure you want to release the game?\nOnce released, the console will no longer launch at startup.All dev-related configuration files will be preserved.Please review and update dev\nconfigs if necessary before proceeding. This\naction can only be undone by\nchanging the 'released' variable after console\nclosed or use 'cancelrelease' command before\nconsole closed.")
        r=str(input("Confirm. (y/n):"))
        if r=="y":
          released=1
          IO.Save(True,"released",released)
          Kernel.Cout.Console("Your game have been released,\nthis console will no longer launch at next startup.")
        else:Kernel.Cout.Console("User cancelled.")
        del r
      elif g=="cancelrelease"and permissionlvl>=4:
        r=str(input("Confirm for cancelling your releasegame\ncommand. (y/n):"))
        if r=="y":
          released=0
          IO.Save(True,"released",released)
          Kernel.Cout.Console("Game releasing have been\ncancelled.")
        else:Kernel.Cout.Console("User cancelled.")
        del r
      elif g=="getvar"and permissionlvl>=4:
        getv=str(input("variable name:"))
        try:Kernel.GetVar(getv,True)
        except Exception as e:
          Kernel.Cout.Error("Unable to get var."+str(e))
        del getv
      elif g=="delvar"and permissionlvl>=4:
        delv=str(input("variable name:"))
        try:Kernel.DelObj(delv,True)
        except Exception as e:
          Kernel.Cout.Error("Unable to delete var:"+str(e)+".")
      elif g=="togglegcstate"and permissionlvl>=4:
        Kernel.ToggleGcState()
      elif g=="setlang"and permissionlvl>=1:
        g=str(input("1:English,2:Simplified Chinese,3.Cancel"))
        if g=="1":
          langtype=1
          Kernel.Cout.Console("Language set.")
        elif g=="2":
          langtype=2
          Kernel.Cout.Console("Language set.")
        elif g=="3":pass
        else:
          Kernel.Cout.Error("Language type unknown, using default language.")
          langtype=1
          Kernel.ErrChk(3,"Language type unknown.")
      elif g=="disablemod"and permissionlvl>=1:Kernel._ModHandler(1);Kernel.ConVar("runmod",False,True)
      elif g=="autoloadmod"and permissionlvl>=1:
        if autoloadmod:autoloadmod=False
        else:autoloadmod=True
        Kernel.Cout.Console("Auto mod load process is now:"+str(autoloadmod)+".")
      elif g=="modinit"and permissionlvl>=1:Kernel._ModHandler(2)
      elif g=="autorunoutgamemod"and permissionlvl>=1:
        if arogmmd:arogmmd=False
        else:arogmmd=True
        Kernel.Cout.Console("auto run out game mod is now: %s."%(arogmmd))
      elif g=="runmod"and permissionlvl>=1:
        Kernel.ConVar("runmod",True,True)
        a=Kernel._ModHandler(3)
        if a==0:del a;break
        else:Kernel.ConVar("runmod",False,True)
      elif g=="initcfg"and permissionlvl>=1:Kernel.Init(1)
      elif g=="modver"and permissionlvl>=1:Kernel._ModHandler(4)
      elif g=="savecfg"and permissionlvl>=1:
        Kernel.SaveCfg()
      elif g=="help 1"and permissionlvl>=1:
        Kernel.Cout.Msg("IlChelcciCore engine help page 1:\nrun:start engine.\nhelp <page(1-7)>:get help.\nquit:stop engine and console.\nsetgeomet:set a new resolution for screen.\nforceexitonerror:forcibly stop whole engine when encounting any error and warn.\nversion:get engine version and credits.\nhwinfo:get hardware info.\ncls:clear screen.")
      elif g=="help 2"and permissionlvl>=1:
        Kernel.Cout.Msg("IlChelcciCore engine help page 2:\nloadgame:load game from saved file.\ndeletesave:delete saved game.\nmodinit:init installed mod.\nrunmod:start mod.\nmodver:get version for mod.\ndisablemod:disable mod.(pop)\nadjustthreshold:change the value for\ngc.threshold()\ndev: toggle developer mode.")
      elif g=="help 3"and permissionlvl>=1:
        Kernel.Cout.Msg("IlChelcciCore engine help page 3:\nscuptoggle: toggle the output when screen \nupdate.\nexec:use exec() to execute python code.\nnovid:disable launch video.\ninitcfg:execute cfg init process manually.\nsavecfg:save current configs.\ngetcfgs:get current cfg status.\nsetmodamount:tell mod loader how many mods should be loaded.")
      elif g=="help 4"and permissionlvl>=1:
        Kernel.Cout.Msg("IlChelcciCore engine help page 4:\nautoloadmod:toggle the auto mod loading\nprocess.\nsetlang:set a language for engine.\nbegin:start a dedicated function,\ne.g. 'Prgm.Main()' for main function.\nreleasegame:release your game.\ncancelrelease:undo when you released game\nwith command 'releasegame'.\nchangegameinfo:change the infos of game temporarily.")
      elif g=="help 5"and permissionlvl>=1:
        Kernel.Cout.Msg("IlChelcciCore engine help page 5:\nconvar:change a global var.\ngetvar:get a value from a var.\ndelvar:delete a provided var.\nsetopening:allocate a new opening type.\ntogglegcstate:toggle gc state to True or False.\ngccollect:trigger gc.collect.\nautorunoutgamemod:toggles when game is\nreleased automatically run out game mod.\nme:get current user ID and current permission level.")
      elif g=="help 6"and permissionlvl>=1:
        Kernel.Cout.Msg("IlChelcciCore engine help page 6:\nsay:say a string.\nignoreverchkonmod:toggle mod version check.\nsetapptitle:set a new app title.\ntogglebar:toggles title bar.\nban:ban a user by userid.\nunban:unban a user by userid.\nop:give a user op permission.\ndeop:remove a user's op permission.\nuser:check an user's permission level.")
      elif g=="help 7"and permissionlvl>=1:
        Kernel.Cout.Msg("IlChelcciCore engine help page 7:\nisbanned:check ban state of given user ID.\npardon:same as unban.")
      elif g=="isbanned" and permissionlvl >=4:
        a=int(input("userid to check ban state(input 0 to cancel):"))
        if Permission.IsValid(a) is False or a==0:
          Kernel.Cout.Console("User ID does not exist.")
          continue
        Kernel.Cout.Info("User ID %s's ban state is: '%s'."%(a,Permission.IsBanned(a)))
      elif g=="ban"and permissionlvl>=4:
        a=int(input("userid to ban(input 0 to cancel):"))
        if a==0:continue
        Permission.Ban(a)
      elif g=="unban"and permissionlvl>=4 or g=="pardon" and permissionlvl>=4:
        a=int(input("userid to unban(input 0 to cancel):"))
        if a==0:continue
        Permission.Unban(a)
      elif g=="op"and permissionlvl>=4:
        a=int(input("userid to op(input 0 to cancel):"))
        if a==0:continue
        Permission.SetGroup(a,4)
      elif g=="deop"and permissionlvl>=4 or g=="pardon"and permissionlvl>=4:
        a=int(input("userid to deop(input 0 to cancel):"))
        if a==0:continue
        Permission.RemoveGroup(a)
      elif g=="togglebar"and permissionlvl>=1:
        if Kernel.GetVar("showbar"):Kernel.ConVar("showbar",False)
        else:Kernel.ConVar("showbar",True)
        Kernel.Cout.Console("Show title bar is now: %s."%(Kernel.GetVar("showbar")))
      elif g=="setapptitle"and permissionlvl>=4:
        s=str(input("New app title:"))
        Kernel.ConVar("apptitle",s)
        Kernel.Cout.Console("New title is: %s."%(Kernel.GetVar("apptitle")))
      elif g=="me"and permissionlvl>=1:
        Kernel.Cout.Msg("Current user is: %s."%(Kernel.GetVar("userid")))
        Kernel.Cout.Msg("Your current permission level is: %s."%(permissionlvl))
      elif g=="user"and permissionlvl>=4:
        a=int(input("User ID(input 0 to cancel):"))
        if a==0:continue
        if Permission.IsValid(a) is False:
          Kernel.Cout.Console("User ID does not exist.")
          continue
        Kernel.Cout.Console("User ID %s's permission level is: %s."%(a,Permission.User(a)))
      elif g=="convar"and permissionlvl>=4:
        v=str(input("variable:"))
        f=str(input("value:"))
        try:
          Kernel.ConVar(v,f,True)
        except Exception as e:
          Kernel.Cout.Error("Variable operation failed. %s"%(e))
        del v,f
      elif g=="gccollect"and permissionlvl>=4:
        gc.collect()
        Kernel.Cout.Console("Gc collect completed.")
      elif permissionlvl>=1 and g=="quit"or permissionlvl>=1 and g=="stop"or permissionlvl>=1 and g=="exit"or g=="esc"and permissionlvl>=1:
        del g
        Kernel.quit(0)
        break
      elif permissionlvl>=1 and g=="say":
        s=str(input("string:"))
        sys.stdout.write(s+"\n")
      elif g=="changegameinfo"and permissionlvl>=4:
        Kernel.Cout.Console("Change info(1.version/2.debug date/3.company/4.copyright/5.game title/0.cancel.):")
        while True:
          g=get_key()
          if g=="1":
            GAMEVER=str(input("New value:"))
            Kernel.Cout.Console("Game version set to:%s."%(GAMEVER))
            break
          elif g=="2":
            DEBUGDATE=str(input("New value:"))
            Kernel.Cout.Console("Debug date set to:%s."%(DEBUGDATE))
            break
          elif g=="3":
            COMPANY=str(input("New value:"))
            Kernel.Cout.Console("Company set to:%s."%(COMPANY))
            break
          elif g=="4":
            COPYRIGHT=str(input("New value:"))
            Kernel.Cout.Console("Copyright set to:%s."%(COPYRIGHT))
            break
          elif g=="5":
            GAMETITLE=str(input("New value:"))
            Kernel.Cout.Console("Game title set to:%s."%(GAMETITLE))
            break
          elif g=="0":
            Kernel.Cout.Console("Cancelled.")
            break
      elif g=="setmodamount"and permissionlvl>=1:
        modamount=input("how many mods should engine load?(default 100):")
        Kernel.Cout.Console(str(modamount)+" mods will be trying to load at next time.")
      elif g=="scuptoggle"and permissionlvl>=2:
        if not dr:
          dr=True;Kernel.Cout.Console("Enabled.")
        else:dr=False;Kernel.Cout.Console("Disabled.")
      elif g=="setgeomet"and permissionlvl>=2:
        try:
          scrgeometx=int(input("xmin:"))
          scrgeomety=int(input("ymin:"))
          scrgeometmx=int(input("xmax:"))
          scrgeometmy=int(input("ymax:"))
          Kernel.Cout.Console("Resolution set to:"+str(scrgeometx)+","+str(scrgeomety)+","+str(scrgeometmx)+","+str(scrgeometmy))
        except Exception as e:
          Kernel.Cout.Error("Setting was failed. "+str(e))
          Kernel.ErrChk(3,"Bad arguments.")
      elif g=="getcfgs"and permissionlvl>=1:
        Kernel.Cout.Msg("exit on error:"+str(erxt))
        Kernel.Cout.Msg("gc threshold:"+str(gcthresholdint))
        Kernel.Cout.Msg("novid:"+str(novid))
        Kernel.Cout.Msg("log output on screen draw:"+str(dr))
        Kernel.Cout.Msg("dev:"+str(dev))
        Kernel.Cout.Msg("lang:"+str(ActionUI.DispLanguage("lang")))
        Kernel.Cout.Msg("use mod:"+str(usemod))
        Kernel.Cout.Msg("mod amounts:"+str(modamount))
        Kernel.Cout.Msg("auto load mod:"+str(autoloadmod))
        Kernel.Cout.Msg("Resolution:"+str(scrgeometx)+","+str(scrgeomety)+","+str(scrgeometmx)+","+str(scrgeometmy))
        Kernel.Cout.Msg("Permission level:%s."%(permissionlvl))
        Kernel.Cout.Msg("show bar:%s."%(Kernel.GetVar("showbar")))
      elif g=="forceexitonerror"and permissionlvl>=3:
        if erxt==1:
          erxt=0
          Kernel.Cout.Console("Exit when error disabled.")
        else:
          erxt=1
          Kernel.Cout.Console("Exit when error enabled.")
      elif g=="setopening"and permissionlvl>=1:
        openingtype=int(input("new opening type:"))
        Kernel.Cout.Console("Opening type is now:%s."%(openingtype))
      elif permissionlvl>=1 and g=="version"or g=="ver"and permissionlvl>=1:
        Kernel.Cout.Msg("IlChelcciCore 2D Gaming engine.\n"+str(GAMEVER)+"\nDebugged in:"+str(DEBUGDATE)+"\nMade by Alex_Nute aka axnut123.\nMade in China.\nyour Python version:"+str(sys.version)+"\nEngine built on Python 3.4.0.\nCopyright and company info:"+COPYRIGHT+","+COMPANY+".")
      elif g=="novid"and permissionlvl>=2:
        if not novid:
          novid=True
          Kernel.Cout.Console("Disabled launch video.")
        else:
          novid=False
          Kernel.Cout.Console("Enabled launch video.")
      elif g=="hwinfo"and permissionlvl>=2:
        Kernel.Cout.Msg("Version:"+str(GAMEVER))
        Kernel.Cout.Msg("Platform:"+str(get_platform()))
        Kernel.Cout.Msg("mem free:"+str(gc.mem_free()))
        Kernel.Cout.Msg("mem alloc:"+str(gc.mem_alloc()))
        Kernel.Cout.Msg("total mem:"+str(totalmem))
        Kernel.Cout.Msg("stack use:"+str(mp.stack_use()))
        Kernel.Cout.Msg("pystack use:"+str(mp.pystack_use()))
        Kernel.Cout.Msg("cpu tick:"+str(ticks_cpu()))
        Kernel.Cout.Msg("local time:"+str(localtime()))
        Kernel.Cout.Msg("gc threshold:"+str(gcthresholdint))
        Kernel.Cout.Msg("gc is enabled:%s"%(gc.isenabled()))
      elif g=="deletesave"and permissionlvl>=1:
        IO.Delete()
      elif g=="loadgame"and permissionlvl>=1:
        IO.Load()
      elif g=="help"and permissionlvl>=1:
        Kernel.Cout.Msg("ILCC Command help.\nUsage: help <page 1-7>\nexample: help 1 for page 1.")
      elif permissionlvl>=1 and g=="cls"or permissionlvl>=1 and g=="clr" or g=="clear"and permissionlvl>=1:
        clear_history()
      elif permissionlvl>=4 and g=="dev"or g=="developer"and permissionlvl>=4:
        if not dev:
          dev=True
          Kernel.Cout.Console("Dev mode enabled.")
        else:dev=False;Kernel.Cout.Console("Dev mode disabled.")
      elif g=="adjustthreshold"and permissionlvl>=4:
        try:
          gcthresholdint=int(input("gc.threshold:"))
          gc.threshold(gcthresholdint)
          Kernel.Cout.Console("New value given.")
        except Exception as e:
          Kernel.Cout.Error("Failed. "+str(e))
      elif permissionlvl>=4 and g=="exec"or g=="execute"and permissionlvl>=4:
        g=str(input("execute:"))
        try:
          exec(g)
          Kernel.Cout.Console("Executed code.")
        except Exception as e:
          Kernel.Cout.Error("Unable to execute code. "+str(e))
          Kernel.ErrChk(5,"Cannot execute code.")
        except BaseException:
          del g
          Kernel.quit(0)
      elif g=="":pass
      else:Kernel.Cout.Console("Unknown command or lacking\npermission on command:"+str(g)+".\nType help <page(1-7)> to get help.")
    return 0
  @staticmethod
  def Opening(optp=1):#the engine opening.
    if optp==1:
      set_color(0,0,0)
      fill_rect(0,0,500,300)
      ActionUI.DispBaseUI(0,0,1)
      set_color(10,210,140)
      draw_text(80,120,ActionUI.DispLanguage("cp0"))
      paint_buffer()
      sleep(2)
      set_color(0,0,0)
      fill_rect(0,0,500,300)
      ActionUI.DispBaseUI(0,0,1)
      set_color(255,100,120)
      draw_text(80,80,"POWERED BY:")
      set_color(10,10,255)
      draw_text(185,80,"IlChelcciCore")
      set_color(255,255,255)
      draw_text(10,100,ActionUI.DispLanguage("cp1"))
      draw_text(10,115,ActionUI.DispLanguage("cp2"))
      draw_text(10,130,ActionUI.DispLanguage("cp3"))
      draw_text(10,145,ActionUI.DispLanguage("cp4"))
      draw_text(10,160,GAMEVER)
      ActionUI.DispUi(0,0,9)
      paint_buffer()
    elif optp==2:
      set_color(0,0,0)
      fill_rect(0,0,500,300)
      paint_buffer()
      sleep(0.7)
      posy=10;posx=0
      set_color(20,20,255)
      fill_rect(0,0,350,300)
      set_color(255,255,255)
      draw_text(5,12,"#starting sequence.( secondary.S .Season.3 normal react.(**")
      sleep(1)
      paint_buffer()
      draw_text(5,posy+10,"Ma = Checking programming system 314014113")
      draw_text(5,posy+20,"Mx = nu 82224")
      draw_text(5,posy+30,"ar = arts78779")
      posy = posy+10
      sleep(0.5)
      paint_buffer()
      draw_text(5,posy+30,"m2 = 250785536")
      draw_text(5,posy+40,"--| 6 423GGG Dll6267")
      draw_text(5,posy+50,"O | = ◆")
      draw_text(5,posy+60,"m | = ▪ ¤   4 Camuu")
      draw_text(5,posy+70,"m6| = 4b822b Hb m2g 40b20 tba")
      draw_text(5,posy+80,".8 | = ◆ b2a      ◆   4 eclai")
      draw_text(5,posy+90,"k8| = Obj4722269 bectebgwarbnt")
      draw_text(5,posy+100,"     .baccDefine   8276* 8779")
      draw_text(5,posy+110,"∌∠i.quur cfbi  9721741*")
      draw_text(5,posy+120,"     .suff: Stuff 8  7313  34227")
      draw_text(5,posy+130,"     .baccDefine   8276* 8779")
      paint_buffer()
    sleep(1.7)
    return optp
class IO:#Input-Output class.
  def __init__(self):pass
  @staticmethod
  def _Translator(translatetype,inputs=None):#built-in function, for translating str to int or int to str.
    if translatetype==1:
      tsdt1={"ignoredisable":0,"ignorehud":1,"ignorevfx":2,"ignoredeath":3,"ignoreall":4}
      ch1=tsdt1.get(inputs)
      return ch1
    elif translatetype==2:
      tsdt2={0:"ignoredisable",1:"ignorehud",2:"ignorevfx",3:"ignoredeath",4:"ignoreall"}
      ch2=tsdt2.get(inputs)
      return ch2
  @staticmethod
  def Save(custom=False,name="customFile",gamevar=None,logout=True,overwriteOnly=False):#built-in function, for saving game.
    global userid,emptysave,mapslt,psx,v_live,v_hev,psy,weapon_crb,v_hev,weapon_pcn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit,plspd,plr,plg,plb,plh,plw,kingignores
    suserid=str(userid)
    if not custom:
      try:
        store_value("playery"+suserid,psy)
        store_value("playerx"+suserid,psx)
        store_value("v_hev"+suserid,v_hev)
        store_value("emptysave"+suserid,0)
        store_value("inclip9"+suserid,inclip9)
        store_value("inclip357"+suserid,inclip357)
        store_value("wpnslt"+suserid,wpnslt)
        store_value("v_live"+suserid,v_live)
        store_value("weapon_crb"+suserid,weapon_crb)
        store_value("weapon_pcn"+suserid,weapon_pcn)
        store_value("weapon_pst"+suserid,weapon_pst)
        store_value("weapon_357"+suserid,weapon_357)
        store_value("mapslt"+suserid,mapslt)
        store_value("ammo9"+suserid,ammo9)
        store_value("ammo357"+suserid,ammo357)
        store_value("item_suit"+suserid,item_suit)
        store_value("plspd"+suserid,plspd)
        store_value("plw"+suserid,plw)
        store_value("plh"+suserid,plh)
        store_value("plr"+suserid,plr)
        store_value("plg"+suserid,plg)
        store_value("plb"+suserid,plb)
        store_value("kingignores"+suserid,int(IO._Translator(1,inputs=kingignores)))
        if logout:Kernel.Cout.IO("Game saved.")
        return 0
      except Exception as e:
        Kernel.Cout.Error("Operation failed."+str(e))
        Kernel.ErrChk(2,"Cannot save file.")
        return -1
    else:
      try:
        if overwriteOnly==True:
          if IO.Load(True,name,False,False) is None:
            return -1
        store_value(str(name),gamevar)
        if logout:Kernel.Cout.IO("Saved file:"+str(name)+".")
        return 0
      except Exception as e:
        Kernel.Cout.Error("File operation on:"+str(name)+" failed.\n"+str(e))
        Kernel.ErrChk(2,"Cannot save file.")
        return -1
  @staticmethod
  def Delete(custom=False,name="customFile",gamevar=None,logout=True):#built-in function, for delete saved game.
    global userid,emptysave,mapslt,psx,v_live,v_hev,psy,weapon_crb,v_hev,weapon_pcn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit,plspd,plr,plg,plb,plh,plw,kingignores
    suserid=str(userid)
    if not custom:
      try:
        store_value("playery"+suserid,95)
        store_value("playerx"+suserid,95)
        store_value("plspd"+suserid,5)
        store_value("kingignores"+suserid,0)
        store_value("v_hev"+suserid,0)
        store_value("emptysave"+suserid,1)
        store_value("inclip9"+suserid,0)
        store_value("inclip357"+suserid,0)
        store_value("wpnslt"+suserid,0)
        store_value("v_live"+suserid,100)
        store_value("weapon_crb"+suserid,0)
        store_value("weapon_pcn"+suserid,0)
        store_value("weapon_pst"+suserid,0)
        store_value("weapon_357"+suserid,0)
        store_value("mapslt"+suserid,0)
        store_value("ammo9"+suserid,0)
        store_value("plh"+suserid,5)
        store_value("plw"+suserid,5)
        store_value("plr"+suserid,0)
        store_value("plg"+suserid,0)
        store_value("plb"+suserid,0)
        store_value("ammo357"+suserid,0)
        store_value("item_suit"+suserid,0)
        if logout:Kernel.Cout.IO("File deleted.")
        return 0
      except Exception as e:
        Kernel.Cout.Error("Operation failed."+str(e))
        Kernel.ErrChk(4,"Cannot delete file.")
        return -1
    else:
      try:
        store_value(str(name),int(gamevar))
        if logout:Kernel.Cout.IO("File operate success on:"+str(name)+".")
        return 0
      except Exception as e:
        Kernel.Cout.Error("File operate on:"+str(name)+" failed.\n"+str(e))
        Kernel.ErrChk(2,"Cannot operate file.")
        return -1
  @staticmethod
  def Load(custom=False,name="customFile",logout=True,ReturnZeroOnNull=False,):#built-in function, for load a saved game.
    returnval=None
    global userid,emptysave,mapslt,psx,v_live,v_hev,psy,weapon_crb,v_hev,weapon_pcn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit,plspd,plw,plh,plr,plg,plb,kingignores
    if not custom:
      try:
        suserid=str(userid)
        plr=recall_value("plr"+suserid)
        plg=recall_value("plg"+suserid)
        plb=recall_value("plb"+suserid)
        plw=recall_value("plw"+suserid)
        plh=recall_value("plh"+suserid)
        plspd=recall_value("plspd"+suserid)
        kingignoreinputraw=recall_value("kingignores"+suserid)
        mapslt=recall_value("mapslt"+suserid)
        emptysave=recall_value("emptysave"+suserid)
        wpnslt=recall_value("wpnslt"+suserid)
        weapon_357=recall_value("weapon_357"+suserid)
        weapon_pst=recall_value("weapon_pst"+suserid)
        ammo9=recall_value("ammo9"+suserid)
        ammo357=recall_value("ammo357"+suserid)
        psy=recall_value("playery"+suserid)
        psx=recall_value("playerx"+suserid)
        v_live=recall_value("v_live"+suserid)
        v_hev=recall_value("v_hev"+suserid)
        inclip9=recall_value("inclip9"+suserid)
        inclip357=recall_value("inclip357"+suserid)
        weapon_crb=recall_value("weapon_crb"+suserid)
        weapon_pcn=recall_value("weapon_pcn"+suserid)
        item_suit=recall_value("item_suit"+suserid)
        kingignores=IO._Translator(2,kingignoreinputraw)
        del kingignoreinputraw
        if v_live<=0:
          Kernel.Cout.Warning("Game save is invalid with health:"+str(v_live)+".\n please reset current save. with savereset.py.")
          Kernel.ErrChk(5,"Health is 0 at game save.")
          return -2
        if emptysave:
          Kernel.Cout.Warning("Trying to load an empty save.")
          Kernel.ErrChk(5,"Cannot load empty save.")
          return -2
        else:
          if logout:Kernel.Cout.IO("Game loaded from save.")
          return 0
      except Exception as e:
        Kernel.Cout.Error("Operation failed."+str(e))
        Kernel.ErrChk(2,"Cannot load file.")
        return -1
    else:
      try:
        returnval=recall_value(str(name))
        if logout:Kernel.Cout.IO("File operation on:"+str(name)+" success.")
        return returnval
      except Exception as e:
        Kernel.Cout.Error("File operation failed on:"+str(name)+".\n"+str(e))
        Kernel.ErrChk(2,"Cannot load file.")
        if ReturnZeroOnNull:return 0
        else:return None
class Permission:#permission level class.
  def __init__(self):pass
  @staticmethod
  def IsValid(id):#built-in function, validate given id.
    a=int(IO.Load(True,"user"+str(id),False,True))
    if a==0 or a=="0":
      return False
    else: return True
  @staticmethod
  def User(id):#built-in function, get current permission level.
    if not Permission.IsValid(id):
      Kernel.Cout.Error("Current user does not exist.")
      Kernel.ErrChk(1,"Current user does not exist.")
      return 1
    return IO.Load(True,"permlvl"+str(id),False,False)
  @staticmethod
  def SetGroup(id,level):#built-in function, set current permission level.
    if not Permission.IsValid(id):
      Kernel.Cout.Error("Current user does not exist.")
      Kernel.ErrChk(1,"Current user does not exist.")
      return 1
    if level>4:
      level=4
      Kernel.Cout.Warning("Permission level cannot exceed 4, set to 4 automatically.")
      Kernel.ErrChk(1,"Permission level exceed max level.")
    elif level<1:
      level=1
      Kernel.Cout.Warning("Permission level cannot below 1, set to 1 automatically.")
      Kernel.ErrChk(1,"Permission level below min level.")
    if str(id)==str(Kernel.GetVar("userid")):
      Kernel.ConVar("permissionlvl",level)
    IO.Save(True,"permlvl"+str(id),int(level),False,True)
    Kernel.Cout.Info("Changed user ID %s's permission level to '%s'."%(id,level))
    return id,level
  @staticmethod
  def RemoveGroup(id):#built-in function, remove current permission level.
    if not Permission.IsValid(id):
      Kernel.Cout.Error("Current user does not exist.")
      Kernel.ErrChk(1,"Current user does not exist.")
      return 1
    IO.Save(True,"permlvl"+str(id),1,False,True)
    if str(id)==str(Kernel.GetVar("userid")):
      Kernel.ConVar("permissionlvl",1)
    Kernel.Cout.Info("Deopped user ID '%s'."%(id))
    return id
  @staticmethod
  def Ban(id):#built-in function, ban a user by userid.
    if not Permission.IsValid(id):
      Kernel.Cout.Error("Current user does not exist.")
      Kernel.ErrChk(1,"Current user does not exist.")
      return 1
    if str(id)==str(Kernel.GetVar("userid")):
      Kernel.Cout.Error("You may not ban yourself.")
      Kernel.ErrChk(1,"You may not ban yourself.")
      return 1
    IO.Save(True,"banned"+str(id),1,False,True)
    Kernel.Cout.Info("Banned user ID '%s'."%(id))
    return id
  @staticmethod
  def Unban(id):#built-in function, unban a user by userid.
    if not Permission.IsValid(id):
      Kernel.Cout.Error("Current user does not exist.")
      Kernel.ErrChk(1,"Current user does not exist.")
      return 1
    IO.Save(True,"banned"+str(id),0,False,True)
    Kernel.Cout.Info("Unbanned user ID '%s'."%(id))
    return id
  @staticmethod
  def IsBanned(id):#built-in function, check if a user is banned by userid.
    if not Permission.IsValid(id):
      Kernel.Cout.Error("Current user does not exist.")
      Kernel.ErrChk(1,"Current user does not exist.")
      return 1
    b=IO.Load(True,"banned"+str(id),False)
    if b==1:
      return True
    else:
      return False
  @staticmethod
  def Pardon(id):#built-in function, pardon a user by userid.
    Permission.Unban(id)
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
        Kernel.Cout.Error("Cannot find type of the VFX that dedicated.")
        Kernel.ErrChk(1,"VFX type not found.")
        return -1
class Actors:#entity class.
#in Actors class, Draw method return 1 is not rendered,0 is rendered.
  def __init__(self):pass
  class King:#Player class.
    def __init__(self):pass
    @staticmethod
    def Kick(logout=True):#built-in function, kick the player to main menu.
      ActionUI.DispUi(0,0,"kickscr")
      ActionUI.DispUi(0,0,9)
      sleep(3)
      StdUtil.InMenu(True)
      if logout:Kernel.Cout.Info("Kicked player out of the game.")
    @staticmethod
    def Draw(hide=False,ignorehide=False):#built-in function, draw player.
      global plr,plg,plb,psy,psx,plw,plh,v_live
      if not ignorehide and v_live<=0 or hide:return 1
      if plw<=0 or plh<=0:
        Kernel.Cout.Error("Player height or width is 0 or\nunder 0!")
        Kernel.ErrChk(5,"Player height or width is 0 or\nunder 0.",True)
      set_color(plr,plg,plb)
      fill_rect(psx,psy,plw,plh)
      return 0
    @staticmethod
    def Kill(clearsuit=False,devonly=False,logout=True):#built-in function, kill player.
      if devonly:return -1
      Kernel.ConVar("v_live",-99999)
      if clearsuit:Kernel.ConVar("v_hev",0)
      if logout:Kernel.Cout.Info("Killed player by function.")
      return 0
    @staticmethod
    def Status(*ignoretp):#built-in function, checking player status.
      global v_live,item_suit
#Do not let "ignoredisable" mixed with other argument,
#same as "ignoreall".
      if "ignoredisable"in ignoretp:
        pass
      if "ignoreall"in ignoretp:
        ignoretp=("ignorehud","ignoredeath","ignorevfx")
      if "ignorevfx"not in ignoretp and v_live<=20 and v_live>=0:#low health VFX.
        UniFX.LowHealth()
      if "ignoredeath"not in ignoretp and v_live<=0:#death detecting.
        ActionUI.DispUi(0,0,7)
        Actors.King.Draw()
        paint_buffer()
        StdUtil.ConsoleLog(7)
        while True:
           k=get_key()
           if k=="enter":
             IO.Load()
             break
      if "ignorehud"not in ignoretp and item_suit:#hud.
        ActionUI.DispUi(0,0,6)
        ActionUI.DispUi(0,0,8)
      return ignoretp
    @staticmethod
    def Move(mvtp,direction,step=5,goto=(0,0),ignorefreeze=False):#built-in function,for movements and teleporting. set the step to 0 to freeze player.
      global psx,psy,v_live
      if mvtp==0:
        if not ignorefreeze and v_live<=0:
          Kernel.Cout.Info("Player died,ignored input.")
          return -1
        if direction==1 or direction=="right":psx+=step;return mvtp,direction,step,psx,psy
        elif direction==2 or direction=="left":psx-=step;return mvtp,direction,step,psx,psy
        elif direction==3 or direction=="down":psy+=step;return mvtp,direction,step,psx,psy
        elif direction==4 or direction=="up":psy-=step;return mvtp,direction,step,psx,psy
        else:
          Kernel.Cout.Error("Undefined direction or None in direction.")
          Kernel.ErrChk(1,"Undefined direction or None in direction for Actors.King.Move().")
          return -1
      elif mvtp==1:
        x,y=goto
        psx=x
        psy=y
        return mvtp,x,y,psx,psy
      else:
        Kernel.Cout.Error("Undefined movement type.")
        Kernel.ErrChk(1,"Undefined movement type.")
        return -1
    @staticmethod
    def Init(inittype,ar1=None,ar2=None,ar3=None):#built-in function,for init player vars.
      global plspd,plr,plg,plb,psy,psx,plw,plh,v_live,v_hev,ammo9,ammo357,inclip9,inclip357,item_suit,weapon_crb,weapon_pst,weapon_357,weapon_pcn,kingignores
      if inittype==1 or inittype=="color":
        plr=ar1
        plg=ar2
        plb=ar3
        return 1,plr,plg,plb
      elif inittype==2 or inittype=="position":
        psx=ar1
        psy=ar2
        return 2,psx,psy
      elif inittype==3 or inittype=="size":
        plw=ar1
        plh=ar2
        return 3,plw,plh
      elif inittype==4 or inittype=="health":
        v_live=ar1
        return 4,v_live
      elif inittype==5 or inittype=="suit":
        v_hev=ar1
        return 5,v_hev
      elif inittype==6 or inittype=="ammo9":
        ammo9=ar1
        inclip9=ar2
        return 6,ammo9,inclip9
      elif inittype==7 or inittype=="ammo357":
        ammo357=ar1
        inclip357=ar2
        return 7,ammo357,inclip357
      elif inittype==8 or inittype=="giveCrowbar":
        weapon_crb=ar1
        return 8,weapon_crb
      elif inittype==9 or inittype=="givePistol":
        weapon_pst=ar1
        return 9,weapon_pst
      elif inittype==10 or inittype=="give357":
        weapon_357=ar1
        return 10,weapon_357
      elif inittype==11 or inittype=="givePhyscnn":
        weapon_pcn=ar1
        return 11,weapon_pcn
      elif inittype==12 or inittype=="giveSuit":
        item_suit=ar1
        return 12,item_suit
      elif inittype==13 or inittype=="speed":
        plspd=ar1
        return 13,plspd
      elif inittype==14 or inittype=="ignores":
        kingignores=ar1
        return 14,kingignores
      else:
        Kernel.Cout.Error("Unknown init type.")
        Kernel.ErrChk(1,"Unknown init type.")
        return -1
  class Queen:#npc entities.
    def __init__(self):pass
    @staticmethod
    def Draw(x,y,w=5,h=5,r=20,g=20,b=20,hide=False):#built-in function,for drawing entities.
      if hide:return 1
      set_color(r,g,b)
      fill_rect(x,y,w,h)
      return 0
  class Pawn():#props or other obj class.
    def __init__(self):pass
    @staticmethod
    def Draw(x,y,w=5,h=5,rd=2,r=25,g=25,b=20,shape=0,hide=False):#built-in function,for draw the pawn.
      if hide:return 1
      set_color(r,g,b)
      if shape==0:fill_circle(x,y,rd);return 0
      elif shape==1:fill_rect(x,y,w,h);return 0
      else:
        Kernel.Cout.Error("Pawn shape type unknown.")
        Kernel.ErrChk(1,"Pawn shape type undef.")
        return -1
class ActionUI:#UI class.
  def __init__(self):pass
  @staticmethod
  def DispLanguage(langstr):#built-in function,for replacing given key to specific value.
    global langtype,langdict1
    langdict1={
    "plterr":"This engine cannot run on your system.",
    "liberr":"The engine failed to start.",
    "reqmis":"Required dependencies are missing.",
    "supsys":"Supported platform:hh,ios,dt. your platform:",
    "prsesc":"Press esc to quit.",
    "libchk":"please check the libraries. Press esc to quit.",
    "cp0":"Made by:Alex_Nute",
    "cp1":"Copyright © Haoriwa 2024 - 2025, the Half-Life 2 is",
    "cp2":"copyright for Valve.The ti_draw,ti_system",
    "cp3":"is copyright for Texas Instruments.Using this",
    "cp4":"software represents you agreed our terms.",
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
    "dbdate":"Debugged in:",
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
    "youdied":"You died,press enter to continue.",
    "ammo":"AMMO",
    "crb":"CROWBAR",
    "physcnn":"GRAVITY GUN",
    "pst":"PISTOL",
    "357":".357 MAGNUM",
    "dangerset":"This option is dangerous!",
    "load":"Loading...",
    "dr":"log output when screen update",
    "dev":"developer mode",
    "savecfg":"s:save cfg",
    "langset":"language setting",
    "reso":"Resolution:",
    "set":"tab:settings",
    "titset":"Settings(press to toggle)",
    "erxt":"force exit on error",
    "gcisenb":"Is gc enabled",
    "totalmem":"Total Mem:",
    "gcthreshold":"gc threshold:",
    "gametitle":"game title:",
    "kicktext":"You have been kicked out of the game.",
    "wesendyoutomenu1":"We will send you back to",
    "wesendyoutomenu2":"main menu in a few seconds.",
    "usemod":"Is mod enabled",
    "noactulmodcnt":"(Configurated counts.)"};
    langdict2={
    "usemod":"是否启用模组:",
    "gametitle":"游戏名:",
    "liberr":"引擎启动失败。",
    "reqmis":"必要依赖项缺失。",
    "libchk":"请检查安装的库,按下esc以退出。",
    "plterr":"此引擎无法在你的系统运行。",
    "supsys":"可运行的平台:hh,ios,dt。当前平台:",
    "prsesc":"按下esc以退出。",
    "cp0":"由Alex_Nute制作",
    "cp1":"版权所有 © Haoriwa 2024 - 2025, 半条命2",
    "cp2":"(半衰期2)由Valve所有。ti_draw,ti_system库",
    "cp3":"由德州仪器所有(TI)。使用此",
    "cp4":"软件将代表你同意使用规则。",
    "modamount":"模组加载数:",
    "usemod":"启用模组",
    "lang":"简体中文",
    "erxt":"发生错误时退出",
    "set":"tab:设置",
    "savecfg":"s:保存设置",
    "dbdate":"测试日期:",
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
    "dangerset":"此设置非常危险!",
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
    "reso":"分辩率:",
    "titset":"设置(按下切换)",
    "gcisenb":"是否启用垃圾清理",
    "totalmem":"总运行内存:",
    "noactulmodcnt":"(被配置数量)",
    "kicktext":"你被踢出了游戏。",
    "wesendyoutomenu1":"我们将在几秒后把你送回主菜单。",
    "wesendyoutomenu2":"",
    "gcthreshold":"清理阈值:"};
    if langtype==1:out=str(langdict1.get(langstr))
    elif langtype==2:out=str(langdict2.get(langstr))
    else:out=str(langdict1.get(langstr))
    if out is not None:
      return out
    else:
      Kernel.Cout.Error("ActionUI.DispLanguage() method has an error occurred.")
      Kernel.ErrChk(1,"Missing key and value or dict error.")
      return langstr
  @staticmethod
  def CheckBox(x,y,ipt):#built-in function, a check box.
    if ipt:
      draw_rect(x,y,13,13)
      draw_line(x,y+5,x+5,y+13)
      x+=5
      y+=13
      draw_line(x,y,x+8,y-11)
      return True
    else:
      draw_rect(x,y,13,13)
      return False
  @staticmethod
  def DispUi(x,y,wintp):#built-in function,for display window, gui elements.
    global emptysave,erxt,dev,mapslt,debugs,v_live,v_hev,wpnslt,usemod,ammo9,ammo357,inclip9,inclip357,weapon_pst,weapon_crb,weapon_pcn,weapon_357,dr,langtype,usemod,modamount,GAMETITLE
    if wintp==1:
      set_color(135,135,135)
      fill_rect(x,y,120,40)
      set_color(255,255,255)
      draw_text(x+10,y+20,"Vgui window")
      Kernel.Cout.Info("Vgui window render request sent to client.")
    elif wintp==2:
      if debugs and dev:
        StdUtil.WaitStart(100,lambda:Kernel.GetGcState())
        set_color(0,0,0)
        draw_text(10,20,str(ActionUI.DispLanguage("memfree"))+str(gc.mem_free())+"|"+str(ActionUI.DispLanguage("totalmem"))+str(totalmem))
        draw_text(10,35,str(ActionUI.DispLanguage("memalloc"))+str(gc.mem_alloc())+"|"+str(ActionUI.DispLanguage("gcisenb"))+":"+str(gcenb))
        draw_text(10,55,str(ActionUI.DispLanguage("stackuse"))+str(mp.stack_use())+"|"+str(ActionUI.DispLanguage("pystackuse"))+str(mp.pystack_use()))
        draw_text(10,70,str(ActionUI.DispLanguage("gcthreshold"))+str(gc.threshold())+"|"+str(ActionUI.DispLanguage("cputick"))+str(ticks_cpu()))
        draw_text(10,85,str(ActionUI.DispLanguage("gametitle"))+GAMETITLE)
        draw_text(10,100,str(ActionUI.DispLanguage("localtime"))+str(localtime()))
        draw_text(10,115,str(ActionUI.DispLanguage("ppos"))+str(psx)+","+str(psy)+"|"+str(ActionUI.DispLanguage("mapid"))+str(mapslt))
        draw_text(10,130,str(ActionUI.DispLanguage("usemod"))+":"+str(usemod))
        draw_text(10,145,str(ActionUI.DispLanguage("ver"))+str(GAMEVER))
        draw_text(10,160,str(ActionUI.DispLanguage("dbdate")+str(DEBUGDATE)))
        draw_text(10,175,str(ActionUI.DispLanguage("platform"))+str(get_platform()))
        draw_text(10,190,str(ActionUI.DispLanguage("reso"))+str(scrgeometx)+","+str(scrgeomety)+","+str(scrgeometmx)+","+str(scrgeometmy))
        draw_text(10,205,str(ActionUI.DispLanguage("modamount"))+str(modamount)+str(ActionUI.DispLanguage("noactulmodcnt")))
        paint_buffer()
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
    elif wintp==5:
      set_color(120,120,120)
      fill_rect(30,0,15,15)
      set_color(200,150,50)
      draw_text(31,13,"1")
      set_color(120,120,120)
      fill_rect(55,0,15,15)
      set_color(200,150,50)
      draw_text(56,13,"2")
    elif wintp==6 and item_suit:
      set_color(200,150,50)
      if v_hev>0:
        draw_text(80,190,v_hev)
        draw_text(80,200,str(ActionUI.DispLanguage("suit")))
      if v_live>=21:
        set_color(200,150,50)
      else:
        set_color(250,100,10)
      draw_text(15,190,v_live)
      draw_text(15,200,str(ActionUI.DispLanguage("health")))
    elif wintp==7:
      set_color(210,10,10)
      fill_rect(0,0,500,300)
      set_color(255,255,255)
      draw_text(20,80,str(ActionUI.DispLanguage("youdied")))
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
    elif wintp==9:
      set_color(250,250,250)
      draw_text(220,205,str(ActionUI.DispLanguage("load")))
      paint_buffer()
    elif wintp==10:
      set_color(120,120,120)
      fill_rect(30,30,80,50)
      set_color(200,150,50)
      draw_text(31,82,str(ActionUI.DispLanguage("crb")))
    elif wintp==11:
      set_color(120,120,120)
      fill_rect(30,100,120,50)
      set_color(200,150,50)
      draw_text(31,145,str(ActionUI.DispLanguage("physcnn")))
    elif wintp==12:
      set_color(120,120,120)
      fill_rect(55,30,80,50)
      if ammo9==0:
        set_color(255,10,10)
      else:set_color(200,150,50)
      draw_text(56,82,str(ActionUI.DispLanguage("pst")))
    elif wintp==13:
      set_color(120,120,120)
      fill_rect(55,100,125,50)
      if ammo357==0:
        set_color(255,10,10)
      else:set_color(200,150,50)
      draw_text(56,142,str(ActionUI.DispLanguage("357")))
    elif wintp==14:
      set_color(250,250,250)
      draw_text(10,40,str(ActionUI.DispLanguage("titset")))
      if not dev:set_color(190,190,190)
      else:set_color(250,250,250)
      ActionUI.CheckBox(10,45,dr);draw_text(30,60,"a:"+str(ActionUI.DispLanguage("dr")));set_color(250,250,250)
      if released:set_color(190,190,190)
      else:set_color(250,250,250)
      ActionUI.CheckBox(10,65,dev);draw_text(30,80,"b:"+str(ActionUI.DispLanguage("dev")));set_color(250,250,250)
      draw_text(10,100,"c:"+str(ActionUI.DispLanguage("langset"))+":"+str(ActionUI.DispLanguage("lang")))
      ActionUI.CheckBox(10,105,usemod);draw_text(30,120,"d:"+str(ActionUI.DispLanguage("usemod")))
      if not dev:set_color(190,190,190)
      else:set_color(250,250,250)
      ActionUI.CheckBox(10,125,erxt);draw_text(30,140,"e:"+str(ActionUI.DispLanguage("erxt")))
      ActionUI.CheckBox(10,145,gcenb);draw_text(30,160,"f:%s (%s)"%(ActionUI.DispLanguage("gcisenb"),ActionUI.DispLanguage("dangerset")));set_color(250,250,250)
      draw_text(10,180,str(ActionUI.DispLanguage("savecfg")))
      draw_text(10,200,str(ActionUI.DispLanguage("escres")))
    elif wintp=="kickscr":
      set_color(50,0,0)
      fill_rect(0,0,500,300)
      set_color(225,225,225)
      draw_text(47,120,ActionUI.DispLanguage("kicktext"))
      draw_text(47,135,ActionUI.DispLanguage("wesendyoutomenu1"))
      draw_text(47,150,ActionUI.DispLanguage("wesendyoutomenu2"))
    else:
      Kernel.Cout.Error("UI type is not defined.")
      Kernel.ErrChk(1,"Missing UI type.")
    ActionUI.DispBaseUI(0,0,1)#one little problem is if there is no dispui called front layered ui will not be displayed as well.
  @staticmethod
  def DispBaseUI(x,y,uitp):#built-in function. for display a ui that always at front.
    if uitp==1:
      if not Kernel.GetVar("showbar"):
        return
      set_color(30,30,30)
      fill_rect(0,0,320,20)
      set_color(210,210,210)
      draw_text(7,17,Kernel.GetVar("apptitle"))#this is just a example. you can try other things.
    else:
      Kernel.Cout.Error("UI type is not defined.")
      Kernel.ErrChk(1,"Missing UI type.")
  @staticmethod
  def Title(x,y,texttp):#built-in function,for display a title.
    if texttp==1:
      set_color(255,0,0)
      draw_text(x,y,"Trigger")
      Kernel.Cout.Info("Title displayed.")
      return 1
    else:
      Kernel.Cout.Info("Title type not defined.")
      Kernel.ErrChk(1,"Unknown title type.")
      return -1
class StdUtil:#Builtins class, Standard utilities.
  def __init__(self):pass
  @staticmethod
  def ConsoleLog(numoflog,c=None):#built-in function,for console output. do not use.
    logs={
      1:"[INFO]Screen updated.",
      2:"[INFO]Start the Opening.",
      3:"[INFO]Engine stopped with code:%s."%(c),
      4:"[INFO]All assets are ready to use.",
      5:"[INFO]Game start.",
      6:"[INFO]Map ID:%s loaded."%(c),
      7:"[INFO]Player died."}
    l=logs.get(numoflog)
    Kernel.Cout.Msg(l)
    return numoflog
  @staticmethod
  def WaitStart(sec,callback):#built-in function. Async sleep.
    global endtick,active,action
    endtick=ticks_cpu()+sec
    active=True
    action=callback
  @staticmethod
  def TriggerOnce(minx,miny,maxx,maxy,trgtp):#built-in function. trigger that only run once.
    global v_live,psy,psx
    if psx>=minx and psx<=maxx and psy>=miny and psy<=maxy:
      if trgtp==1:
        if not Kernel.GetVar("gtemp1"):
          v_live-=10
          Kernel.ConVar("gtemp1",True)
          Kernel.Cout.Info("Trigger executed.")
          return 1
        else:return 0
      else:
        Kernel.Cout.Info("Trigger is not defined.")
        Kernel.ErrChk(1,"Unknown trigger.")
        return -1
  @staticmethod
  def Trigger(minx,miny,maxx,maxy,trgtp):#built-in function,for trigger a specific event.
    global v_live,mapslt,psx,psy#map selection needs global var
    if psx>=minx and psx<=maxx and psy>=miny and psy<=maxy:
      if trgtp==1:
        ActionUI.Title(120,80,1)
        Kernel.Cout.Info("Trigger executed.")
        return 1
      elif trgtp==2:
        mapslt=1
        Kernel.ConVar("gtemp1",None)
#this code is mean to reset the trigger once in
#map0, you can choose to not reset the trigger.
        Kernel.Cout.Info("Trigger executed.")
        return 2
      elif trgtp==3:
        mapslt=0
        Kernel.Cout.Info("Trigger executed.")
        return 3
      else:
        Kernel.Cout.Info("Trigger is not defined.")
        Kernel.ErrChk(1,"Unknown trigger.")
        return -1
  @staticmethod
  def MouseBox(minx,miny,maxx,maxy,enabled):#built-in function.for checking mouse position.
#Warn:better use keyboard to operate menu, using
#this function will have huge impact to perfomance.
#and it's hard to box the area you need.
#I have developed a tool for this kind of funcs,
#goto shell and run boxtest.py.
#but you still can use this API for game.sorry for no example.
    x, y=get_mouse()
    if x>=minx and x<=maxx and y>=miny and y<=maxy and enabled:return True
    else:return False
  @staticmethod
  def SettingMenu():#settings menu,built-in function.
    set_color(120,120,120)
    fill_rect(0,0,500,300)
    set_color(250,250,250)
    ActionUI.DispUi(0,0,14)
    return 0
  @staticmethod
  def InMenu(menustate):#built-in function, for changing menu state.
    if menustate:Kernel.ConVar("inmenu",True)
    else:Kernel.ConVar("inmenu",False)
    return menustate
  @staticmethod
  def IsInMenu():#built-in function, for getting menu state.
    return Kernel.GetVar("inmenu")
  @staticmethod
  def PauseMenu():#pause menu,built-in function.
    set_color(120,120,120)
    fill_rect(0,0,500,300)
    set_color(255,255,255)
    draw_text(130,17,GAMEVER)
    draw_text(130,30,str(ActionUI.DispLanguage("dbdate"))+DEBUGDATE)
    ActionUI.DispUi(0,0,3)
    return 0
  @staticmethod
  def MapStat():#built-in function,for map render,trigger and other stuff.
    global mapslt
    if mapslt==0:
      Assets.c1a0()
      StdUtil.Trigger(0,0,20,50,2)
      StdUtil.TriggerOnce(150,50,150,100,1)
      return 0
    if mapslt==1:
      Assets.c0a0()
      StdUtil.Trigger(125,75,225,175,3)
      return 1
    else:
      Kernel.Cout.Error("MapStat function cannot find defined type.")
      Kernel.ErrChk(1,"Missing type.")
      return -1
class Wbase:#Weapon system class.
  def __init__(self):pass
  @staticmethod
  def SelectWeapon(wpnid,logout=False):
    Kernel.ConVar("wpnslt",wpnid)
    if logout:Kernel.Cout.Info("Selected %s"%(Kernel.GetVar("wpnslt")))
    return wpnid
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
        ammo9-=18
        inclip9+=18
        return 1
    elif type==2:
      if inclip357==0 and ammo357>=6:
        ammo357-=6
        inclip357+=6
        return 2
class Assets:#asset class.
  def __init__(self):pass
  @staticmethod
  def c0a0():#map define,a debug map.
    set_color(10,180,10)
    fill_rect(0,0,500,300)
    set_color(140,140,140)
    fill_rect(60,35,60,35)
    return 0
  @staticmethod
  def c1a0():#map define.
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
  def gmanintro():#Opening, it is too complex, might damage your brain!
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
  def MainMenu1():#built-in function, main menu varient 1.
    posy=20;rgbr=10;rgbb=100;posx=0;w=0;h=0;g=0;b=0;r=0
    set_pen("medium","solid")
    a=0
    def fillwindow(bx,by):
      set_color(210,210,0)
      by+=2
      bx+=6
      fill_rect(bx,by,2,2);bx+=6;fill_rect(bx,by,2,2)
      by+=4
      bx-=6
      fill_rect(bx,by,2,2);bx+=6;fill_rect(bx,by,2,2)
    set_color(0,0,100)
    fill_rect(0,0,500,300)
    for i in range(1,200):
      fill_rect(0,posy,500,300)
      set_color(rgbr,0,rgbb)
      rgbr+=10;posy+=10
      if rgbr >= 240:
        break
      else:
        pass
    set_color(220,220,220)
    for i in range(100):
      fill_circle(randint(0,500),randint(0,100),1)
    fill_circle(100,50,10);l=0;m=0;set_pen("thin","solid")
    for i in range(2):
      draw_line(l,m,m,l)
      l=randint(60,80);m=randint(20,60)
    set_pen("thick","solid")
    set_color(0,0,100)
    fill_circle(105,50,7)
    set_color(250,250,0);posx=-30
    for i in range(6):
      g=randint(0,255);b=randint(0,255);r=randint(0,255)
      set_color(r,g,b)
      draw_line(randint(0,500),300,randint(0,500),randint(0,20))
    if a==1:
      for i in range(6):
        g=randint(200,255)
        set_color(g,g,0)
        draw_line(randint(0,500),300,randint(0,500),randint(0,20))
      else:
        pass
    set_color(10,10,10)
    for i in range(1,25):#stage1
      set_color(10,10,10)
      fill_rect(posx,posy,20,h)
      set_color(255,0,0)
      ax=posx;ay=posy
      ax+=4;ay-=4
      fill_rect(ax,ay,2,2)
      fillwindow(posx,posy)
      h=randint(40,60);posx+=20;posy=randint(120,160)
    set_color(10,10,10);fill_rect(-20,160,520,520);posy=160;posx=-20
    set_color(110,110,110)
    for i in range(1,25):#stage2
      set_color(110,110,110)
      fill_rect(posx,posy,20,h)
      fillwindow(posx,posy)
      h=randint(20,40);posx+=20;posy=randint(160,180)
    set_color(110,110,110)
    fill_rect(-20,180,520,520)
    set_color(150,150,150);posy=180;posx=-20
    for i in range(1,25):#stage3
      set_color(150,150,150)
      fill_rect(posx,posy,20,h)
      fillwindow(posx,posy)
      h=randint(20,40);posx+=20;posy=randint(180,200)
    set_color(150,150,150)
    fill_rect(-20,200,520,520)
    set_color(220,220,0);posy=140;posx=0
    set_color(255,0,0)
    fill_circle(randint(20,300),randint(2,120),2)
    set_color(255,255,255)
    draw_text(10,80,"HALF-LIFE²")
    draw_text(130,17,GAMEVER)
    draw_text(130,30,str(ActionUI.DispLanguage("dbdate"))+DEBUGDATE)
    set_pen("thin","solid")
    return 0
  @staticmethod
  def MainMenu2():#main menu function, I don't even know how am I built this.
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
    draw_text(130,17,GAMEVER)
    draw_text(130,30,str(ActionUI.DispLanguage("dbdate"))+DEBUGDATE)
    set_pen("thin","solid")
    return 0
class Prgm:#program class.
  def __init__(self):pass
  @staticmethod
  def Main():#main function.It's a very standard template for engine.
    StdUtil.InMenu(True)
    l_menuslt=Kernel.GetVar("menuslt",False)
    global userid,ingamemod,released,erxt,modscripts,langtype,mapslt,dev,dr,emptysave,psx,v_live,v_hev,psy,weapon_crb,debugs,v_hev,weapon_pcn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit,usemod,plspd,plw,plh,plr,plg,plb,kingignores
    suserid=str(userid)
    StdUtil.ConsoleLog(4)
    while True:#game logic loop.
      if StdUtil.IsInMenu():#menu guard.
        Kernel._ResetGame()
        if l_menuslt==1:Assets.MainMenu1()
        else:Assets.MainMenu2()
        ActionUI.DispUi(0,0,4)
        gc.collect()
        paint_buffer()
        while True:#main menu.
          k=get_key()
          emptysave=IO.Load(True,"emptysave"+suserid,False)
          if k=="enter":
            Assets.gmanintro()
            StdUtil.InMenu(False)
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
            Actors.King.Init(13,5)
            Actors.King.Init(14,"ignoredisable")
            break
          elif k=="b":
            for i in range(2):
              if emptysave==1:IO.Load()
            if emptysave==1:continue
            IO.Load()
            StdUtil.InMenu(False)
            break
          elif k=="c":
            IO.Delete()
          elif k=="menu":
            ActionUI.DispUi(0,0,9)
            if l_menuslt==1:Assets.MainMenu1()
            else:Assets.MainMenu2()
            ActionUI.DispUi(0,0,4)
            paint_buffer()
          elif k=="a":
            Assets.gmanintlol()
            StdUtil.InMenu(False)
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
            Actors.King.Init(13,5)
            Actors.King.Init(14,"ignoredisable")
            break
          elif k=="tab":
            while True:
              k=get_key()
              clear()
              StdUtil.SettingMenu()
              paint_buffer()
              if k=="a" and dev:
                if dr:dr=False
                else:dr=True
              elif k=="b" and not released:
                if dev:dev=False
                else:dev=True
              elif k=="c":#add more conditions if you have more language.
                if langtype==1:
                  langtype=2
                elif langtype==2:
                  langtype=1
              elif k=="d":
                if usemod:usemod=False
                else:usemod=True
              elif k=="e" and dev:
                if erxt==1:erxt=0
                else:erxt=1
              elif k=="f" and dev:Kernel.ToggleGcState()
              elif k=="s":
                Kernel.SaveCfg()
              elif k=="esc":
                ActionUI.DispUi(0,0,9)
                if l_menuslt==1:Assets.MainMenu1()
                else:Assets.MainMenu2()
                ActionUI.DispUi(0,0,4)
                paint_buffer()
                break
          elif k=="esc":
            Kernel.quit(0)
        clear()
        gc.collect()
      if dr:StdUtil.ConsoleLog(1)#print a log when screen update.
      StdUtil.MapStat()#logic check in here,define your trigger in this function.
      for key in ["None"]:
        while k!=key and not StdUtil.IsInMenu():
          k=get_key()
          Kernel.WaitUpdate()
          StdUtil.MapStat()
          ActionUI.DispUi(0,0,2)
          Kernel._ModHandler(5)
          Actors.King.Draw()
          Actors.King.Status(kingignores)
          if k=="u" and dev:
            if not debugs:
              debugs=True
              Kernel.Cout.Info("Debug drawing enabled.")
            else:
              debugs=False
              Kernel.Cout.Info("Debug drawing disabled.")
              break
          elif k=="right":
            Actors.King.Move(0,"right",plspd)
            break
          elif k=="left":
            Actors.King.Move(0,"left",plspd)
            break
          elif k=="up":
            Actors.King.Move(0,"up",plspd)
            break
          elif k=="down":
            Actors.King.Move(0,"down",plspd)
            break
          elif k=="p" and dev:
            Actors.King.Kick()
          elif k=="t" and dev:
            v_hev-=10
            break
          elif k=="s"and dev:
            v_hev+=10
            break
          elif k=="z"and dev:
            v_live-=10
            break
          elif k=="h"and dev:
            Wbase.EventAmmoPick(1,18)
            Wbase.EventAmmoPick(2,6)
            break
          elif k=="y"and dev:
            v_live+=10
            break
          elif k=="tab" and dev:
            gc.collect()
            Kernel.Cout.Debug("gc collect completed.")
            break
          elif k=="d":
            if wpnslt==3 and weapon_pst==1 and inclip9!=0:
              inclip9-=1
              UniFX.BulletFX.BltFlr(1)
            if wpnslt==4 and weapon_357==1 and inclip357!=0:
              inclip357-=1
              UniFX.BulletFX.BltFlr(2)
            if wpnslt==1 and weapon_crb==1:
              UniFX.BulletFX.BltFlr(3)
            if wpnslt==2 and weapon_pcn==1:
              UniFX.BulletFX.BltFlr(4)
            paint_buffer()
            sleep(0.1)
            break
          elif k=="r":
            if wpnslt==3 and weapon_pst==1 and inclip9!=0:
              inclip9-=1
              UniFX.BulletFX.BltFlr(5)
            if wpnslt==4 and weapon_357==1 and inclip357!=0:
              inclip357-=1
              UniFX.BulletFX.BltFlr(6)
            if wpnslt==1 and weapon_crb==1:
              UniFX.BulletFX.BltFlr(7)
            if wpnslt==2 and weapon_pcn==1:
              UniFX.BulletFX.BltFlr(8)
            paint_buffer()
            sleep(0.1)
            break
          elif k=="j":
            if wpnslt==3 and weapon_pst==1 and inclip9!=0:
              inclip9-=1
              UniFX.BulletFX.BltFlr(9)
            if wpnslt==4 and weapon_357==1 and inclip357!=0:
              inclip357-=1
              UniFX.BulletFX.BltFlr(10)
            if wpnslt==1 and weapon_crb==1:
              UniFX.BulletFX.BltFlr(11)
            if wpnslt==2 and weapon_pcn==1:
              UniFX.BulletFX.BltFlr(12)
            paint_buffer()
            sleep(0.1)
            break
          elif k=="l":
            if wpnslt==3 and weapon_pst==1 and inclip9!=0:
              inclip9-=1
              UniFX.BulletFX.BltFlr(13)
            if wpnslt==4 and weapon_357==1 and inclip357!=0:
              inclip357-=1
              UniFX.BulletFX.BltFlr(14)
            if wpnslt==1 and weapon_crb==1:
              UniFX.BulletFX.BltFlr(15)
            if wpnslt==2 and weapon_pcn==1:
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
          elif k=="w"and dev:
            Actors.King.Kill()
          elif k=="menu"and dev:
            Actors.King.Init(8,1)
            Actors.King.Init(9,1)
            Actors.King.Init(10,1)
            Actors.King.Init(11,1)
            Actors.King.Init(12,1)
          elif k=="1":
            if item_suit==1:pass
            else:break
            ActionUI.DispUi(0,0,5)
            if weapon_crb==1:
              ActionUI.DispUi(0,0,10)
            if weapon_pcn==1:
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
                Wbase.SelectWeapon(1)
                clear()
                StdUtil.MapStat()
                Actors.King.Draw()
                break
              elif k=="2" and weapon_pcn==1:
                Wbase.SelectWeapon(2)
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
                Wbase.SelectWeapon(3)
                clear()
                StdUtil.MapStat()
                Actors.King.Draw()
                break
              elif k=="2" and weapon_357==1 and ammo357!=0:
                Wbase.SelectWeapon(1)
                clear()
                StdUtil.MapStat()
                Actors.King.Draw()
                break
              paint_buffer()
            break
          elif k=="esc":
            while True:#pause menu.
              StdUtil.PauseMenu()
              ky="0"
              paint_buffer()
              for ky in["None"]:
                while k!=ky:
                  clear()
                  StdUtil.PauseMenu()
                  k=get_key()
                  emptysave=IO.Load(True,"emptysave"+suserid,False)
                  ActionUI.DispUi(0,0,2)
                  paint_buffer()
                  if k=="esc":
                    clear()
                    break
                  elif k=="q":
                    Kernel.quit(0)
                    break
                  elif k=="tab":
                    while True:
                      k=get_key()
                      clear()
                      StdUtil.SettingMenu()
                      paint_buffer()
                      if k=="a" and dev:
                        if dr:dr=False
                        else:dr=True
                      elif k=="b" and not released:
                        if dev:dev=False
                        else:dev=True
                      elif k=="c":#add more conditions if you have more language.
                        if langtype==1:
                          langtype=2
                        elif langtype==2:
                          langtype=1
                      elif k=="d":
                        if not usemod:usemod=True
                        else:usemod=False
                      elif k=="e" and dev:
                        if erxt==1:erxt=0
                        else:erxt=1
                      elif k=="f" and dev:Kernel.ToggleGcState()
                      elif k=="s":
                        Kernel.SaveCfg()
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
                    Kernel.Cout.Info("Return to main menu.")
                    l_menuslt=randint(1,2)
                    ActionUI.DispUi(0,0,9)
                    StdUtil.InMenu(True)
                    break
                  elif k=="u":
                    if not debugs:
                      debugs=True
                      Kernel.Cout.Info("Debug drawing enabled.")
                    else:
                      debugs=False
                      Kernel.Cout.Info("Debug drawing disabled.")
                break
              break
            break
          paint_buffer()
        break
    return 0
if (__name__=="__main__"):#all program starts from here.
  try:#import check.
    from ti_system import *#normally,gui tools are also included in ti_system.
    import micropython as mp
    if get_platform()=="pc":
      import gcc as gc
      import tkinter as tk
    else:import gc
    Kernel.Cout.Preload("Libraries are successfully loaded.")
  except ImportError:
    try:
      from ti_draw import fill_rect,set_color,draw_text,use_buffer,paint_buffer
      use_buffer()
      set_color(210,10,10)
      fill_rect(0,0,500,300)
      set_color(240,240,240)
      draw_text(10,80,ActionUI.DispLanguage("liberr"))
      draw_text(10,100,ActionUI.DispLanguage("reqmis"))
      draw_text(10,120,ActionUI.DispLanguage("prsesc"))
      paint_buffer()
      Kernel.Cout.Fatal("Library import failed.\nPlease check the libraries installed.\nRequired: ti_system, micropython.")
      while get_key()!="esc":pass
      Kernel.quit(-1)
    except:
      Kernel.Cout.Fatal("The engine cannot run on your device.\nPlease check the libraries installed.\nRequired: ti_system, micropython.")
      Kernel.quit(-1)
  userid=int(IO.Load(True,"loggedinuser",False,True))
  if userid==0 or userid=="0":
    Kernel.Cout.Error("You need an account to play this\ngame!")
    Kernel.quit(1)
  banned=int(IO.Load(True,"banned"+str(userid),False,True))
  newuser=int(IO.Load(True,"newuser"+str(userid),False,True))
  if banned==1 or banned=="1":
    Kernel.Cout.Fatal("Your account have been banned from\nthis game.")
    Kernel.quit(1)
  if newuser==1 or newuser=="1":
    Kernel.SaveCfg()
    IO.Save(True,"emptysave"+str(userid),0)
    IO.Save(True,"newuser"+str(userid),0)
  Kernel.Init(2)
  Kernel.Init(1)
  Kernel._GameLauncher()