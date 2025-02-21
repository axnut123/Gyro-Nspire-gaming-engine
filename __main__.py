#COPYRIGHT (C) Haoriwa 2022 - 2024
#All rights reserved.
# the license is under LICENSE.txt *
from random import *
from ti_draw import *
from ti_system import *
from time import *
import sys
import gc
erxt=0;g="0";key="0";mapslt=0;psx=95;psy=95;v_hev=0;gmver="Gyro 20 Build(0055)";wpnslt=0
item_suit=0;weapon_crb=0;weapon_physcnn=0;weapon_pst=0;weapon_357=0;ammo357=0;ammo9=0
ammo9max=180;ammo357max=12;inclip9=0;inclip357=0;reload9=0;reload357=0;vtk=False;modenb=False
def quit(c=0):#built-in function, in nspire cx ii python the quit function is not defined.
  sys.exit(c)
  return 0
def extchk():#built-in function,for command "enableforceexitonerror".
  global erxt
  if erxt==1:
    print("[DEBUG]Error or warning encounted,stopped engine.")
    sys.exit()
  else:pass
def vwindow(x,y,wintp):#built-in function,for display window.
  set_color(135,135,135)
  global mapslt
  if wintp==1:
    fill_rect(x,y,120,40)
    set_color(255,255,255)
    draw_text(x+10,y+20,"Vgui window")
    print("[INFO]Vgui window render request sent to client.")
    return 0
  else:
    print("[ERROR]Window type is not defined.")
    extchk()
    return 1
def func_title(x,y,r,g,b,text):#built-in function,for display a title.
  set_color(r,g,b)
  draw_text(x,y,text)
  print("[INFO]Title displayed.")
  return 0
def func_trigger(minx,miny,maxx,maxy,trgtp):#built-in function,for trigger a specific event.
  global mapslt#map selection needs global var
  if psx>=minx and psx<=maxx and psy>=miny and psy<=maxy:
    if trgtp==1:
      func_title(120,80,255,0,0,"Trigger")
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
  else:pass
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
    else:pass
  elif type==2:
    if inclip357==0 and ammo357>=6:
      reload357=0
      sleep(4)
      ammo357-=6
      inclip357+=6
      reload357=1
    else:pass
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
      draw_text(10,80,"HALF-LIFE²")
      draw_text(10,100,"enter:resume")
      draw_text(10,120,"q:quit game")
      draw_text(150,17,gmver)
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
    g=randint(200,255);b=randint(0,255);r=randint(0,255)
    set_color(g,g,0)
    draw_line(randint(0,500),300,randint(0,500),randint(0,20))
  if a==1:
    for i in range(6):
      g=randint(200,255)
      set_color(g,g,0)
      draw_line(randint(0,500),300,randint(0,500),randint(0,20))
    else:
      pass
  set_color(10,10,10)
  for i in range(1,30):#stage1
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
  for i in range(1,30):#stage2
    set_color(110,110,110)
    fill_rect(posx,posy,20,h)
    fillwindow(posx,posy)
    h=randint(20,40);posx+=20;posy=randint(160,180)
  set_color(110,110,110)
  fill_rect(-20,180,520,520)
  set_color(150,150,150);posy=180;posx=-20
  for i in range(1,30):#stage3
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
  draw_text(150,17,gmver)
  set_pen("thin","solid")
  return(0)
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
def v_hud():#built-in function,for hev hud
  set_color(200,150,50)
  if v_hev!=0:
    draw_text(80,190,v_hev)
    draw_text(80,200,"SUIT")
  return 0
def main():#main function
  debugs=False
  global mapslt,psx,psy,weapon_crb
  use_buffer()
  mainmenu()
  draw_text(10,100,"enter:start")
  draw_text(10,120,"a:quick start")
  draw_text(10,140,"esc:quit")
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
    else:pass
  clear()
  consolelog(4)
  while True:#game logic loop
    global inclp,v_hev,weapon_physcnn,weapon_pst,weapon_357,wpnslt,ammo357,ammo9,inclip9,inclip357,item_suit
    consolelog(1)
    mapstat()#logic check in here,define your trigger in this function.
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
    else:pass
    set_color(0,0,0)
    fill_rect(psx,psy,5,5)
    if item_suit==1:#hud
      v_hud()
      if v_live>=20:
        set_color(200,150,50)
        draw_text(20,190,v_live)
        draw_text(20,200,"HEALTH")
      else:
        set_color(250,100,10)
        draw_text(20,190,v_live)
        draw_text(20,200,"HEALTH")
    set_color(0,0,0)
    fill_rect(psx,psy,5,5)
    if v_live<=0:#death detecting
      set_color(210,10,10)
      fill_rect(0,0,500,300)
      set_color(255,255,255)
      draw_text(20,80,"You died,press e and move to revive")
      k=get_key()
      paint_buffer()
      consolelog(7)
      while get_key()!="esc":
         k=get_key()
         if k=="e":
           v_live = 100
           break
    else:pass
    k=get_key()#key detect loop
    for key in ["g","d","j","l","r","esc","z","h","s","t","u","1","2","0","up","down","left","right"]:
      while k!=key:
        k=get_key()
        if debugs==True:
          clear()
          mapstat()
          set_color(0,0,0)
          draw_text(10,20,"mem free:"+str(gc.mem_free()))
          draw_text(10,35,"mem alloc:"+str(gc.mem_alloc()))
          draw_text(10,55,"cpu tick:"+str(ticks_cpu()))
          draw_text(10,70,"local time:"+str(localtime()))
          draw_text(10,85,"player pos:"+str(psx)+","+str(psy))
          draw_text(10,100,"map id:"+str(mapslt))
          fill_rect(psx,psy,5,5)
          paint_buffer()
        if k=="u":
          if debugs==False:
            debugs=True
            print("[INFO]Debug drawing enabled")
          else:
            debugs=False
            print("[INFO]Debug drawing disabled")
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
        elif k=="z":
          v_hev=v_hev-10
          break
        elif k=="s":
          v_hev+=10
          break
        elif k=="t":
          v_live=v_live-10
          break
        elif k=="h":
          event_ammopick(1,18)
          event_ammopick(2,6)
          break
        elif k=="u":
          v_live+=10
          break
        elif k=="up":
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
          else:pass
          break
        elif k=="0":
          weapon_crb=1
          weapon_physcnn=1
          weapon_pst=1
          weapon_357=1
          item_suit=1
        elif k=="1":
          if item_suit==1:
            pass
          else:
            break
          set_color(120,120,120)
          fill_rect(30,0,15,15)
          set_color(200,150,50)
          draw_text(31,13,"1")
          set_color(120,120,120)
          fill_rect(55,0,15,15)
          set_color(200,150,50)
          draw_text(56,13,"2")
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
            else:pass
        elif k=="2":
          if item_suit==1:
            pass
          else:
            break
          set_color(120,120,120)
          fill_rect(30,0,15,15)
          set_color(200,150,50)
          draw_text(31,13,"1")
          set_color(120,120,120)
          fill_rect(55,0,15,15)
          set_color(200,150,50)
          draw_text(56,13,"2")
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
            else:pass
            paint_buffer()
          break
        elif k=="m":
          while True:#pause menu
            vg0();ky="0"
            paint_buffer()
            k=get_key()
            for ky in["enter","m","q"]:
              while k!=ky:
                k=get_key()
                if k=="enter":
                  clear()
                  fill_rect(500,500,1,1)
                  break
                elif k=="q":
                  consolelog(3)
                  sys.exit()
                  break
                elif k=="g":
                  vwindow(50,50,1)
                  vwindow(50,50,0)
                  paint_buffer()
              break
            break
          break
        paint_buffer()
      break
  return 0
if (__name__=="__main__"):#all program start here.
  print("[PRE-LOAD]Starting console and engine.\n[PRE-LOAD]current resolution:",get_screen_dim())
  while g!="run"or g!="start":
    g=str(input("Console_"))
    if g=="run"or g=="start":
      print("[CONSOLE]Running engine.")
      break
    elif g=="modinit":
      if vtk!=True:
        import gyro_addon_main1 as tk
        vtk=True
        print("[INFO]Mod init success.")
      else:
        print("[WARN]Mod init completed")
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
      print("Gyro engine help page2:\nmodinit:init installed mod.\nrunmod:start mod.\nmodver:get version for mod.")
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
      print("[CONSOLE]Resolution is now:",get_screen_dim())
    elif g=="enableforceexitonerror":
      erxt=1
      print("[CONSOLE]Exit when error enabled.")
      break
    elif g=="version":
      e=get_platform()
      print("Gyro 2D Gaming engine.\n",gmver,"\nComplied in 2025/02/20\nMade by Alex_Nute aka axnut123.\nMade in China.\nCurrent platform:",e,"\nyour Python version:",sys.version,"\nEngine built on Python 3.4.0")
      del e
    elif g=="hwinfo":
      print("mem free",str(gc.mem_free()))
      print("mem alloc",str(gc.mem_alloc()))
      print("cpu tick",ticks_cpu())
    elif g=="help":
      print("Usage: help <1or2>. example: help 1 for page 1.")
    elif g=="cls":
      clear_history()
    else:
      print("[CONSOLE]Unknown command:",g,".type help <page(1/2)> to get help.")
  del g
  print("[CONSOLE]Console is being closed.\n[INFO]Engine is now started.")
  consolelog(2)
  opening()
  consolelog(5)
  if modenb==True:
    clear()
    tk.mod_main()
  else:
    main()
