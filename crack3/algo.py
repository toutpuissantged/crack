import time
global lettre,long,bou,repo5,num,long2,long3
lettre=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','0','1','2','3','4','5','6','7','8','9','']
long=36
bou=1     
repo5=4
num=3
long2=0
long3=0
# code spagetti enfin fonction X18 pour les thread  
def crack():
    # initialisation des variables a utiliser 
    rec=1
    x,y,z,u=0,0,0,0
    # algo pour traiter les decalage 
    if rec==1:
        long2=0
        long3=2
    elif 2<=rec<=36:
        long2=rec
        long3=rec+2
    x=long2
    while 1:
        bou=1
        t1=time.time()
        user=(lettre[x]+lettre[y]+lettre[z])
        paz=lettre[x]
        payload = dict(username=user, password=paz)  
        x+=1
        # coeur du moteur... va permettre la generation ordonner des logins
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
                file2=open('recov.ck','w')
                file2.write(str(u))
                file2.close()
                if num==3:
                        break
                else :
                        pass
        elif u==long:
                if num==4:
                        break
        print(user)
        
crack()

