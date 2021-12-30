import threading , ctypes
from modules import Crack

class Thread(threading.Thread):
    def __init__(self,rec):
        threading.Thread.__init__(self)
        self.rec=rec
    def run(self): 
        crack =  Crack(self.rec)
        crack.run()

    def stop_all(self):
        for thread in threading.enumerate():
            if thread.isAlive():
                thread.raise_exception()

    def get_id(self):
 
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
  
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
