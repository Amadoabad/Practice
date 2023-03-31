import time
from contextlib import contextmanager
class ExecutionTime:
 def __init__(self):
     pass

 def __enter__(self):
     self.t_before=time.time()
     return self.t_before

 def __exit__(self,exc_type,exc_val,exc_tb):
     self.t_after= time.time()
     print("Func excuted in ",self.t_after-self.t_before)

def test():
 for i in range(0,1000):
     print(i)

with ExecutionTime() as f:
 test()

@contextmanager
def excution_time():
 try:
     t_before = time.time()
     yield t_before
 finally:
     t_after = time.time()
     print("Func excuted in ",t_after-t_before)

def test():
 for i in range(0,1000):
     print(i)

with excution_time() as f:
 test()
input()
