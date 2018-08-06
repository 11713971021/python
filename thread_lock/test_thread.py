import threading
import time 

'''
author :　Mr.wang
需求: 定义一数字 num=100 ,　创建100个线程　使其 num-=1 的其结果为0
     为验证LOCK

'''


def sub():
    global num

    #num -= 1
    b.acquire()
    a = num 
    time.sleep(0.01)
    num = a -1
    b.release()


num = 100
l = []
b = threading.Lock()

# 创建出100个线程来
for i in range(100):
    t = threading.Thread(target=sub)

    t.start()
    l.append(t)





for i in l:
    i.join()

print(num)
