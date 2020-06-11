import socket
import threading

IP_ADRESS = '127.0.0.1'
PORT = 12220
MAX_LISTENS = 10
RUN = True


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
    size = int(conn.recv(10))
    data = conn.recv(size)
    data = data.decode()
    return (post_type , data) 

#get machine ip adress
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def command_parse(rt , data):
    try:
        if rt == "RTF":
            with open(data , 'r') as f:
               return ("TXT" , f.read())

        elif rt == "WTF":
            data = data.split('\n')
            with open(data[0] , 'w') as f:
                for d in data[1:(len(data))]:
                    f.write(d+'\n')
            return ('TXT' , 'File writed succsessfuly...')
        
        else: 
            return ('TXT' , "Don't can make request.")

    except:
        return ("ERR" , "Ooops")
    
    

def user_service(conn ,adress):
    while RUN:
        try:
            request_type , data = recv(conn)
            answer_type , answer_data = command_parse(request_type , data)
            send(conn, answer_type ,  answer_data)      
        except:
            conn.close()
            return


def listen_connections(sock):
    s.listen( MAX_LISTENS )
    while RUN:
        conn ,adress = sock.accept()
        threading.Thread(user_service(conn ,adress)).run()

        


s = socket.socket()
s.bind((IP_ADRESS , PORT))
threading.Thread( listen_connections(s)).run()