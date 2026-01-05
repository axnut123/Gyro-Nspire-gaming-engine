from ti_system import *
import binascii as asc
import sys

version="1.0"
perm=1

def cout(text):
  sys.stdout.write(text+"\n")
  sys.stdout.flush()

def cvar(var,val):
  globals()[var]=val
  return var,val
  
def gvar(var):
  return globals().get(var)
  
def quit(code=None):
  raise SystemExit(code)
  
class Encrypt:
  def __init__(self):pass
  
  @staticmethod
  def EncryptStr(text):
    return int(asc.hexlify(str(text)))
  
  @staticmethod
  def DecryptStr(text):
    return int(asc.unhexlify(str(text)))
    

class Accounts:
  def __init__(self):pass
  
  @staticmethod
  def Login(ids,password,nologin=False,nopw=False):
    global perm
    try:
      LoadedUserIds=recall_value("user"+str(ids))
      LoadedUserPassword=recall_value("pw"+str(ids))
      LoadedBannedStatus=recall_value("banned"+str(ids))
      if LoadedBannedStatus==1:
        cout(">>This account is banned!")
        return 3
    except:
      cout(">>User ID or password incorrect!")
      return 1
    if LoadedUserPassword==0 and LoadedUserIds==0:
      cout(">>Current user ID does not exist!")
      return 2
    DUserPassword=str(Encrypt.DecryptStr(str(LoadedUserPassword)))
    if int(DUserPassword)==int(password) or nopw==True:
      if nologin==False:
        cout(">>User logged in!")
        store_value("loggedinuser",int(ids))
        perm=recall_value("permlvl"+str(ids))
      return 0
    else:
      cout(">>User ID or password incorrect!")
      return 1
    
  @staticmethod
  def Logout():
    store_value("loggedinuser",0)
    cout(">>Logout successful.")
    return 0
    
  @staticmethod
  def Register(ids,password):
    try:
      LoadedUserIds=recall_value("user"+str(ids))
    except:
      LoadedUserIds=0
    if LoadedUserIds==int(ids):
      cout(">>This ID was already used. Try another ID.")
      return 1
    else:pass
    store_value("user"+str(ids),int(ids))
    store_value("permlvl"+str(ids),1)
    store_value("banned"+str(ids),0)
    store_value("pw"+str(ids),int(Encrypt.EncryptStr(password)))
    store_value("newuser"+str(ids),1)
    cout(">>User registeration successful.")
    return 0
  
  @staticmethod
  def DeleteAccount(ids,password,permlvl=True):
    if permlvl==4:
      ignorepw=True
    else:
      ignorepw=False
    if Accounts.Login(ids,password,True,ignorepw)!=0:return 1
    store_value("user"+str(ids),0)
    store_value("pw"+str(ids),0)
    store_value("banned"+str(ids),0)
    store_value("permlvl"+str(ids),1)
    store_value("newuser"+str(ids),0)
    store_value("loggedinuser",0)
    cout(">>Account deletion successful.")
    return 0
    
  @staticmethod
  def _Console():
    while True:
      g=str(input("]"))
      if g=="help 1":
        cout(">>ILCC account manager help.\n>>add 'sudo:' to some commands to forcibly execute it.\n-login: login with an id and password.\n-logout: logout current account\n-register: registet a new account\n-deleteuser: delete an account.\n-currentuser: get current user ID.\n-quit: quit program.\n-help <pages>: get help.\n-version: get version of program.")
      elif g=="sudo":
        cout(">>Usage: sudo:<command>.\n>>To execute commands with admin privileges.")
      elif g=="login":
        a=int(input(">Your ID:"))
        b=int(input(">Your password:"))
        Accounts.Login(a,b)
      elif g=="register":
        a=int(input(">New ID:"))
        b=int(input(">New password:"))
        Accounts.Register(a,b)
      elif g=="logout":
        Accounts.Logout()
      elif g=="deleteuser":
        a=int(input(">Provide an ID:"))
        b=int(input(">The password of the provided ID:"))
        Accounts.DeleteAccount(a,b)
      elif g=="sudo:deleteuser" and perm>=4:
        a=int(input(">Provide an ID:"))
        Accounts.DeleteAccount(a,0,4)
      elif g=="currentuser":
        cout(">>Current user ID is: %s."%(recall_value("loggedinuser")))
      elif g=="stop" or g=="exit" or g=="quit" or g=="esc":
        quit(0)
      elif g=="help":
        cout(">>Usage: help <pages>.")
      elif g=="version" or g=="ver":
        cout(">>IlChelcciCore Account Manager<<\n>>Version: %s."%(version))
      elif g=="":pass
      else:
        cout(">>Unknown command. Use help <pages> to check the command list.")

if __name__=="__main__":
  Accounts._Console()
