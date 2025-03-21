#COPYRIGHT (C) Haoriwa 2022 - 2024
#All rights reserved.
# the license is under LICENSE.txt *
from random import *
from ti_draw import *
from time import *
from ti_system import *
import sys,gc
import micropython as mp
debugs=False;erxt=0;g="0";key="0";mapslt=0;psx=95;psy=95;v_hev=0;gmver="Gyro 21 Build(0066)";wpnslt=0
item_suit=0;weapon_crb=0;weapon_physcnn=0;weapon_pst=0;weapon_357=0;ammo357=0;ammo9=0;v_live=100
ammo9max=180;ammo357max=12;inclip9=0;inclip357=0;reload9=0;reload357=0;vtk=False;modenb=False
def quit(c=0):#built-in function, in nspire cx ii python the quit function is not defined.
  raise SystemExit(c)
def extchk():#built-in function,for command "enableforceexitonerror".
  global erxt
  if erxt==1:
    print("[DEBUG]Error or warning encounted,stopped engine.")
    quit(1)
def vwindow(x,y,wintp):#built-in function,for display window, gui elements.
  set_color(135,135,135)
  global mapslt,debugs,v_live,v_hev,wpnslt,ammo9,ammo357,inclip9,inclip357,weapon_pst,weapon_crb,weapon_physcnn,weapon_357
  if wintp==1:
    fill_rect(x,y,120,40)
    set_color(255,255,255)
    draw_text(x+10,y+20,"Vgui window")
    print("[INFO]Vgui window render request sent to client.")
    return 0
  elif wintp==2:
    if debugs==True:
      set_color(0,0,0)
      draw_text(10,20,"mem free:"+str(gc.mem_free()))
      draw_text(10,35,"mem alloc:"+str(gc.mem_alloc()))
      draw_text(10,55,"stack use:"+str(mp.stack_use()))
      draw_text(10,70,"pystack use:"+str(mp.pystack_use()))
      draw_text(10,85,"cpu tick:"+str(ticks_cpu()))
      draw_text(10,100,"local time:"+str(localtime()))
      draw_text(10,115,"player pos:"+str(psx)+","+str(psy))
      draw_text(10,130,"map id:"+str(mapslt))
      paint_buffer()
  elif wintp==3:
    set_color(250,250,250)
    draw_text(10,80,"HALF-LIFE²")
    draw_text(10,100,"m:resume")
    draw_text(10,120,"q:quit game")
  elif wintp==4:
    set_color(250,250,250)
    draw_text(10,100,"enter:start")
    draw_text(10,120,"a:quick start")
    draw_text(10,140,"esc:quit")
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
  elif wintp==6:
    set_color(200,150,50)
    if v_hev!=0:
      draw_text(80,190,v_hev)
      draw_text(80,200,"SUIT")
    if v_live>=20:
      set_color(200,150,50)
      draw_text(20,190,v_live)
      draw_text(20,200,"HEALTH")
    else:
      set_color(250,100,10)
      draw_text(20,190,v_live)
      draw_text(20,200,"HEALTH")
  elif wintp==7:
    set_color(210,10,10)
    fill_rect(0,0,500,300)
    set_color(255,255,255)
    draw_text(20,80,"You died,press e and move to revive")
  elif wintp==8:
    if wpnslt==1 or wpnslt==2:#ammunation management.
      pass
    elif wpnslt==3 and weapon_pst==1:
      if ammo9>=18:
        set_color(200,150,50)
      else:
        set_color(255,100,50)
      draw_text(210,200,"AMMO")
      draw_text(210,190,inclip9)
      draw_text(250,190,ammo9)
    elif wpnslt==4 and weapon_357==1:
      if ammo357>=6:
        set_color(200,150,50)
      else:
        set_color(250,100,50)
      draw_text(210,200,"AMMO")
      draw_text(210,190,inclip357)
      draw_text(250,190,ammo357)
  else:
    print("[ERROR]Window type is not defined.")
    extchk()
    return 1
def func_title(x,y,texttp):#built-in function,for display a title.
  if texttp==1:
    set_color(255,0,0)
    draw_text(x,y,"Trigger")
    print("[INFO]Title displayed.")
    return 0
  else:
    print("[INFO]Title type not defined.")
    extchk()
    return 1
def func_trigger(minx,miny,maxx,maxy,trgtp):#built-in function,for trigger a specific event.
  global mapslt#map selection needs global var
  if psx>=minx and psx<=maxx and psy>=miny and psy<=maxy:
    if trgtp==1:
      func_title(120,80,1)
      print("[INFO]Trigger executed.")
      return 0
    elif trgtp==2:
      mapslt=1
      print("[INFO]Trigger executed.")
      return 0
    elif trgtp==3:
      mapslt=0
      print("[INFO]Trigger executed.")
      return 0
    else:
      print("[ERROR]Trigger is not defined.")
      extchk()
      return 1
def event_ammopick(type,amount):#built-in function,for picking up the ammunation box event
  global ammo9,ammo9max,ammo357,ammo357max
  if type==1:
    if ammo9<=ammo9max:
      ammo9+=amount
  if type==2:
    if ammo357<=ammo357max:
      ammo357+=amount
  return 0
def weaponclip(type):#built-in function,for detect clips in gun.
  global inclip9,inclip357,ammo357,ammo9
  if type==1:
    if inclip9==0 and ammo9>=18:
      reload9=0
      sleep(1)
      ammo9-=18
      inclip9+=18
      reload9=1
  elif type==2:
    if inclip357==0 and ammo357>=6:
      reload357=0
      sleep(4)
      ammo357-=6
      inclip357+=6
      reload357=1
  return 0
def consolelog(type):#built-in function,for console output
  if type==1:
    pass
  elif type==2:
    print("[INFO]Start the opening")
  elif type==3:
    print("[INFO]Exit success,code:0")
  elif type==4:
    print("[INFO]All assets are ready to use.")
  elif type==5:
    print("[INFO]Game start")
  elif type==6:
    print("[INFO]Map loaded")
  elif type==7:
    print("[INFO]Player died.")
  return type
def c0a0():#map define,a debug map.
  set_color(10,180,10)
  fill_rect(0,0,500,300)
  set_color(140,140,140)
  fill_rect(60,35,60,35)
  return 0
def c1a0():#map define,i would say it is .bsp file =)
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
  return(0)
def vg0():#pause menu,built-in function
  set_color(120,120,120)
  fill_rect(0,0,500,300)
  set_color(255,255,255)
  draw_text(150,17,gmver)
  vwindow(0,0,3)
  return 0
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
  draw_text(20,180,"Go fuck your self!")
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
def gmanintro():#opening
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
  draw_text(20,180,"Rise and shine mister Freeman,rise and shine.")
  paint_buffer()
  sleep(3)
  set_color(0,0,0)
  r=0
  g=0
  b=0
  for i in range(25):
    fill_rect(0,0,500,300)
    set_color(210,210,255)
    draw_text(20,180,"Rise and shine mister Freeman,rise and shine.")
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
  draw_text(20,180,"No one deserving to sleeping on the job,")
  draw_text(20,190,"but the effort for the world have gone to waste untill...")
  draw_text(20,200,"emm...")
  paint_buffer()
  sleep(7)
  set_color(0,0,0)
  fill_rect(0,0,500,300)
  set_color(210,210,255)
  draw_text(20,180,"Well,let's just say your hour has come again.")
  paint_buffer()
  sleep(5)
  set_color(0,0,0)
  fill_rect(0,0,500,300)
  set_color(210,210,255)
  draw_text(20,180,"The right man in the wrong place")
  draw_text(20,190,"will make the whole world difference")
  paint_buffer()
  sleep(5)
  r=0
  g=0
  b=0
  for i in range(25):
    fill_rect(0,0,500,300)
    set_color(210,210,255)
    draw_text(20,180,"The right man in the wrong place")
    draw_text(20,190,"will make the whole world difference")
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
  draw_text(20,180,"So.Wake up,mr.Freeman.")
  paint_buffer()
  sleep(3)
  set_color(255,255,255)
  for i in range(50):
    draw_line(x,y,x1,y)
    x=randint(0,500);x1=x+30
    y=randint(0,300);
  set_color(210,210,255)
  draw_text(20,190,"wake up and smell the ashes...")
  paint_buffer()
  sleep(2)
  for i in range(25):
    fill_rect(0,0,500,300)
    set_color(210,210,255)
    draw_text(20,190,"wake up and smell the ashes...")
    r+=10;b+=10;g+=10
    set_color(r,g,b)
    sleep(0.01)
    paint_buffer()
  sleep(1)
  clear()
  return(0)
def mainmenu():#main menu function
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
  draw_text(150,17,gmver)
  set_pen("thin","solid")
  return 0
def opening():#the engine opening
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
  draw_text(10,100,"Copyright © Haoriwa 2022 - 2024, the Half-Life 2 is")
  draw_text(10,115,"copyright for Valve.The ti_draw,ti_system")
  draw_text(10,130,"is copyright for Texas Instruments.Using this")
  draw_text(10,145,"software represents you agreed our terms.")
  draw_text(10,160,gmver)
  paint_buffer()
  sleep(1.5)
  return 0
def mapstat():#built-in function,for map render,trigger and other stuff.
  global mapslt
  if mapslt==0:
    c1a0()
    func_trigger(0,0,20,50,2)
    return 0
  if mapslt==1:
    c0a0()
    func_trigger(125,75,100,100,3)
    return 0
  else:
    print("[ERROR]mapstat function cannot find defined type.")
    extchk()
    return 1
def main():#main function
  global mapslt,psx,v_live,v_hev,psy,weapon_crb,debugs,inclp,v_hev,weapon_physcnn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit
  use_buffer()
  mainmenu()
  vwindow(0,0,4)
  paint_buffer()
  while True:#main menu
    k=get_key()
    if k=="enter":
      gmanintro()
      v_live=100
      break
    elif k=="a":
      gmanintlol()
      v_live=100
      break
    elif k=="esc":
      consolelog(3)
      quit()
  clear()
  gc.collect()
  consolelog(4)
  while True:#game logic loop
    consolelog(1)
    mapstat()#logic check in here,define your trigger in this function.
    vwindow(0,0,8)
    set_color(0,0,0)
    fill_rect(psx,psy,5,5)
    if item_suit==1:#hud
      vwindow(0,0,6)
    set_color(0,0,0)
    fill_rect(psx,psy,5,5)
    if v_live<=0:#death detecting
      vwindow(0,0,7)
      k=get_key()
      consolelog(7)
      while get_key()!="esc":
         k=get_key()
         if k=="e":
           v_live = 100
           break
    k=get_key()#key detect loop
    for key in ["g","d","j","l","r","esc","z","h","s","t","u","1","2","0","up","down","left","right"]:
      while k!=key:
        k=get_key()
        mapstat()
        set_color(0,0,0)
        fill_rect(psx,psy,5,5)
        if item_suit==1:
          vwindow(0,0,6)
          vwindow(0,0,8)
        vwindow(0,0,2)
        if k=="u":
          if debugs==False:
            debugs=True
            print("[INFO]Debug drawing enabled")
          else:
            debugs=False
            print("[INFO]Debug drawing disabled")
            break
        elif k=="l":
          psx+=5
          clear()
          fill_rect(psx,psy,5,5)
          break
        elif k=="j":
          psx-=5
          clear()
          fill_rect(psx,psy,5,5)
          break
        elif k=="d":
          psy-=5
          clear()
          fill_rect(psx,psy,5,5)
          break
        elif k=="r":
          psy+=5
          clear()
          fill_rect(psx,psy,5,5)
          break
        elif k=="t":
          v_hev-=10
          break
        elif k=="s":
          v_hev+=10
          break
        elif k=="z":
          v_live-=10
          break
        elif k=="h":
          event_ammopick(1,18)
          event_ammopick(2,6)
          break
        elif k=="y":
          v_live+=10
          break
        elif k=="tab":
          gc.collect()
          print("[DEBUG]gc collect completed.")
          break
        elif k=="up":#maybe create a new function to recall the effects.
          if wpnslt==3 and reload9==0 and weapon_pst==1 and inclip9!=0:
            inclip9-=1
            weaponclip(1)
            set_color(240,240,0)
            draw_line(psx,psy-20,psx,psy-45)
          if wpnslt==4 and reload357==0 and weapon_357==1 and inclip357!=0:
            inclip357-=1
            weaponclip(2)
            set_color(240,240,0)
            draw_line(psx,psy-20,psx,psy-85)
          if wpnslt==1 and weapon_crb==1:
            set_color(210,210,210)
            fill_arc(psx-19,psy-9,50,30,30,100)
          if wpnslt==2 and weapon_physcnn==1:
            set_color(255,150,10)
            set_pen("thick","solid")
            draw_line(psx,psy,psx,psy-35)
            set_pen("thin","solid")
          paint_buffer()
          sleep(0.1)
          break
        elif k=="down":
          if wpnslt==3 and reload9==0 and weapon_pst==1 and inclip9!=0:
            inclip9-=1
            weaponclip(1)
            set_color(240,240,0)
            draw_line(psx,psy+20,psx,psy+45)
          if wpnslt==4 and reload357==0 and weapon_357==1 and inclip357!=0:
            inclip357-=1
            weaponclip(2)
            set_color(240,240,0)
            draw_line(psx,psy+20,psx,psy+85)
          if wpnslt==1 and weapon_crb==1:
            set_color(210,210,210)
            fill_arc(psx-19,psy-9,50,30,-30,-100)
          if wpnslt==2 and weapon_physcnn==1:
            set_color(255,150,10)
            set_pen("thick","solid")
            draw_line(psx,psy,psx,psy+35)
            set_pen("thin","solid")
          paint_buffer()
          sleep(0.1)
          break
        elif k=="left":
          if wpnslt==3 and reload9==0 and weapon_pst==1 and inclip9!=0:
            inclip9-=1
            weaponclip(1)
            set_color(240,240,0)
            draw_line(psx-20,psy,psx-45,psy)
          if wpnslt==4 and reload357==0 and weapon_357==1 and inclip357!=0:
            inclip357-=1
            weaponclip(2)
            set_color(240,240,0)
            draw_line(psx-20,psy,psx-85,psy)
          if wpnslt==1 and weapon_crb==1:
            set_color(210,210,210)
            fill_arc(psx-19,psy-9,50,30,-120,-90)
          if wpnslt==2 and weapon_physcnn==1:
            set_color(255,150,10)
            set_pen("thick","solid")
            draw_line(psx,psy,psx-35,psy)
            set_pen("thin","solid")
          paint_buffer()
          sleep(0.1)
          break
        elif k=="right":
          if wpnslt==3 and reload9==0 and weapon_pst==1 and inclip9!=0:
            inclip9-=1
            weaponclip(1)
            set_color(240,240,0)
            draw_line(psx+20,psy,psx+45,psy)
          if wpnslt==4 and reload357==0 and weapon_357==1 and inclip357!=0:
            inclip357-=1
            weaponclip(2)
            set_color(240,240,0)
            draw_line(psx+20,psy,psx+85,psy)
          if wpnslt==1 and weapon_crb==1:
            set_color(210,210,210)
            fill_arc(psx-19,psy-9,50,30,-30,100)
          if wpnslt==2 and weapon_physcnn==1:
            set_color(255,150,10)
            set_pen("thick","solid")
            draw_line(psx,psy,psx+35,psy)
            set_pen("thin","solid")
          paint_buffer()
          sleep(0.1)
          break
        elif k=="g":
          if wpnslt==3:
            weaponclip(1)
          elif wpnslt==4:
            weaponclip(2)
          break
        elif k=="menu":
          weapon_crb=1
          weapon_physcnn=1
          weapon_pst=1
          weapon_357=1
          item_suit=1
        elif k=="1":
          if item_suit==1:pass
          else:break
          vwindow(0,0,5)
          if weapon_crb==1:
            set_color(120,120,120)
            fill_rect(30,30,80,50)
            set_color(200,150,50)
            draw_text(31,82,"CROWBAR")
          if weapon_physcnn==1:
            set_color(120,120,120)
            fill_rect(30,100,120,50)
            set_color(200,150,50)
            draw_text(31,145,"GRAVITY GUN")
          k=get_key()
          paint_buffer()
          while k!="0":
            k=get_key()
            if k=="0":
              clear()
              mapstat()
              fill_rect(psx,psy,5,5)
              break
            elif k=="1" and weapon_crb==1:
              wpnslt=1
              clear()
              mapstat()
              fill_rect(psx,psy,5,5)
              break
            elif k=="2" and weapon_physcnn==1:
              wpnslt=2
              clear()
              mapstat()
              fill_rect(psx,psy,5,5)
              break
        elif k=="2":
          if item_suit==1:pass
          else:break
          vwindow(0,0,5)
          if weapon_pst==1:
            set_color(120,120,120)
            fill_rect(55,30,80,50)
            set_color(200,150,50)
            draw_text(56,82,"PISTOL")
          if weapon_357==1:
            set_color(120,120,120)
            fill_rect(55,100,125,50)
            set_color(200,150,50)
            draw_text(56,142,".357 MAGNUM")
          paint_buffer()
          k=get_key()
          while k!="0":
            k=get_key()
            if k=="0":
              clear()
              mapstat()
              fill_rect(psx,psy,5,5)
              break
            elif k=="1" and weapon_pst==1:
              wpnslt=3
              clear()
              mapstat()
              fill_rect(psx,psy,5,5)
              break
            elif k=="2" and weapon_357==1:
              wpnslt=4
              clear()
              mapstat()
              fill_rect(psx,psy,5,5)
              break
            paint_buffer()
          break
        elif k=="m":
          while True:#pause menu
            vg0();ky="0"
            paint_buffer()
            k=get_key()
            for ky in["m","q"]:
              while k!=ky:
                clear()
                vg0()
                k=get_key()
                vwindow(0,0,2)
                paint_buffer()
                if k=="m":
                  clear()
                  fill_rect(500,500,1,1)
                  break
                elif k=="q":
                  consolelog(3)
                  quit(0)
                  break
                elif k=="u":
                  if debugs==False:
                    debugs=True
                    print("[INFO]Debug drawing enabled")
                  else:
                    debugs=False
                    print("[INFO]Debug drawing disabled")
              break
            break
          break
        paint_buffer()
      break
  return 0
if (__name__=="__main__"):#all program starts from here.
  print("[PRE-LOAD]Starting console and engine.\n[PRE-LOAD]current resolution:",get_screen_dim())
  while g!="run"or g!="start":
    g=str(input("Console_"))
    if g=="run"or g=="start":
      print("[CONSOLE]Running engine.")
      break
    elif g=="disablemod":
      sys.modules.pop("gyro_addon_main1")
      vtk=False
      modenb=False
      print("[INFO]Mod disabled.")
    elif g=="modinit":
      if vtk!=True:
        import gyro_addon_main1 as tk
        vtk=True
        print("[INFO]Mod init success.")
      else:
        print("[WARN]Mod already init.")
    elif g=="runmod":
      if vtk==True:
        modenb=True
        print("[INFO]Mod is running")
        break
      else:
        print("[ERROR]Mod script not found")
    elif g=="modver":
      if vtk==True:
        print(tk.mod_info(0))
      else:
        print("[ERROR]Mod is not found.")
    elif g=="help 1":
      print("Gyro engine help page 1:\nrun:start engine.\nhelp <page(1/2)>:get help.\nquit:stop engine and console.\nsetgeomet:set a new resolution for screen.\nenableforceexitonerror:forcely stop whole engine when encounting any error and warn.\nversion:get engine version and credits.\nhwinfo:get hardware info.\ncls:clear screen.")
    elif g=="help 2":
      print("Gyro engine help page2:\nmodinit:init installed mod.\nrunmod:start mod.\nmodver:get version for mod.\ndisablemod:disable mod.(pop)")
    elif g=="quit"or g=="stop"or g=="exit":
      del g
      consolelog(3)
      quit()
      break
    elif g=="setgeomet":
      x1=int(input("xmin"))
      y1=int(input("ymin"))
      x2=int(input("xmax"))
      y2=int(input("ymax"))
      set_window(x1,x2,y1,y2)
      del x1,x2,y1,y2
      break
    elif g=="enableforceexitonerror":
      erxt=1
      print("[CONSOLE]Exit when error enabled.")
      break
    elif g=="version":
      e=get_platform()
      print("Gyro 2D Gaming engine.\n",gmver,"\nComplied in 2025/03/21\nMade by Alex_Nute aka axnut123.\nMade in China.\nCurrent platform:",e,"\nyour Python version:",sys.version,"\nEngine built on Python 3.4.0")
      del e
    elif g=="hwinfo":
      print("mem free",str(gc.mem_free()))
      print("mem alloc",str(gc.mem_alloc()))
      print("stack use",str(mp.stack_use()))
      print("pystack use",str(mp.pystack_use()))
      print("cpu tick",ticks_cpu())
      print("local time",str(localtime()))
    elif g=="help":
      print("Usage: help <1or2>. example: help 1 for page 1.")
    elif g=="cls":
      clear_history()
    else:
      print("[CONSOLE]Unknown command:",g,".type help <page(1/2)> to get help.")
  del g
  print("[CONSOLE]Console is being closed.\n[INFO]Engine is now started.")
  gc.collect()
  consolelog(2)
  opening()
  consolelog(5)
  if modenb==True:
    clear()
    tk.mod_main()
  else:
    main()