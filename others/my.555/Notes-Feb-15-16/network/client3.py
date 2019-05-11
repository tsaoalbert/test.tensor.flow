# Import socket module 
import socket                
  
def sendCmd(socket, astr):
    str_bytes = bytes(astr,'utf-8')
    socket.send(str_bytes)

    # receive data from the server 
    answer =  socket.recv(1024).decode('utf-8') 
    print('server response: ', answer)

# Create a socket object 
controlSocket = socket.socket()          
  
# Define the port on which you want to connect 
controlport = 12345                
dataport = 12346

def createDataPort():
    datasocket = socket.socket()
    datasocket.bind(('', dataport))	
    datasocket.listen(1)
    datasocket, (ip, port)  = datasocket.accept()	# tuple of IP and Port of client
    return datasocket

# connect to the server on local computer 
controlSocket.connect(('127.0.0.1', controlport)) 

s = createDataPort()

sendCmd(s, 'LIST')
sendCmd(s, 'RETR somfile.txt' )
sendCmd(s, 'STOR thisfile.bin')
sendCmd(s, 'SYSTEM')
sendCmd(s, 'QUIT')

# close the connection 
s.close()        