import threading
from modules import Crack

class Thread(threading.Thread):
    def __init__(self,rec):
        threading.Thread.__init__(self)
        self.rec=rec
    def run(self): 
        crack =  Crack(self.rec)
        crack.run()
