import socket
import asyncio

def send(conn , post_type ,  str_value):
    size = str(len(str_value))
    if size == '0': return False
    if len(size) < 10: size = ('0'* (10 - len(size))) + str(size)
    if len(post_type) != 3 : return False
    request = (post_type + size + str_value).encode()

    conn.send(request)
    return True

def recv(conn):
    post_type = conn.recv(3).decode()    
    size = int(conn.recv(10).decode())
    data = conn.recv(size)
    return (post_type , data) 

#get machine ip adress
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

