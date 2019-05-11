# Import socket module 
import socket                

maxsize = 1024

def receiveFile():
    
    fd = open('retrfile.txt','w')
    import datetime
    x = datetime.datetime.now()
    fd.write(x.strftime("%c"))
    fd.write('\n')
    while True:
        try:
            s.settimeout(2)
            chunk = s.recv(maxsize)   # read some chunk
            print('recv file line: ', chunk)
            fd.write(chunk.decode('utf-8'))
        except Exception as e:
            print("Exception: ", e)
            s.settimeout(0)
            s.setblocking(True)
            break
    fd.close()


def sendCmd(socket, astr):
    print('sendCmd - ', astr)
    str_bytes = bytes(astr,'utf-8')
    socket.send(str_bytes)

    ss = astr.split()
    if ss[0] == 'RETR':
        receiveFile()
    else:
        # receive data from the server 
        answer =  socket.recv(1024).decode('utf-8') 
        print('server response: ', answer)

# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345            
ftphost = '127.0.0.1'    
  
# connect to the server on local computer 
s.connect((ftphost, port)) 

sendCmd(s, 'LIST')
sendCmd(s, 'RETR somefile.txt' )
sendCmd(s, 'STOR thisfile.bin')
sendCmd(s, 'SYSTEM')
sendCmd(s, 'QUIT')

# close the connection 
s.close()        