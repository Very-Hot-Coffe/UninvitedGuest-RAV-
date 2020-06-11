import socket
import asyncio

IP_ADRESS = '127.0.0.1'
PORT = 12220


def send(conn , post_type ,  str_value):
    size = str(len(str_value))
    if size == '0': return False
    if len(size) < 10: size = ('0'* (10 - len(size))) + str(size)
    if len(post_type) != 3 : return False
    request = (post_type + size + str_value).encode()
    print (request)
    conn.send(request)
    return True

def recv(conn):
    post_type = conn.recv(3).decode()    
    size = int(conn.recv(10).decode())
    data = conn.recv(size)
    data = data.decode()
    return (post_type , data) 

s = socket.socket()
s.connect((IP_ADRESS , PORT))
send(s , "WTF" , "")
t , d = recv(s)
print(d)
