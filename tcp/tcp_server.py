from socket import *
'''
author:Mr.wang
data:2018:8.20
config:python3.5

'''
"s = setblocking() 设置为非阻塞"
s = socket(AF_INET, SOCK_STREAM ,0)
s.bind(('127.0.0.1', 8888))
s.listen(5)
while True:
    c, addr = s.accept()
    data = c.recv(1024)
    print(data.encode())
    while True:
        c.send('hello'.decode())

    c.close()

s.close()
