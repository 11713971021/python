import threading
import time

'''
author:Mr.wang
data:2018/8/6
sssssssssssssssssssssssssssssssssssssssssss
'''


class Lock1(threading.Thread):

    def A1(self):
        a.acquire()
        print(self.name)
        b.acquire()
        time.sleep(2)
        b.release()
        print('拿Ａ')
        a.release()



    def B1(self):
        b.acquire()
        print(self.name)
        print('我是１１')
        a.acquire()


    def run(self):
        self.A1()
        self.B1()

# 创建两把锁
a = threading.Lock()
b = threading.Lock()

l = []
for i in range(5):
    t = Lock1()
    t.start()

    l.append(t)

for t in l:
    t.join()
