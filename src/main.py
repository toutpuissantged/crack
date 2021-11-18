# modules necessaires

import time
from modules import Thread


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