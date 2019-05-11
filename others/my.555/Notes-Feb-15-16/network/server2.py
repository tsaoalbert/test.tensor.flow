import socket			 
import os
from threading import Thread

port = 12345

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print( " New thread started for "+ip+":"+str(port))

    def parse(self, cmdstr):
        if len(cmdstr) == 0:
            cmd = 'NONE'
            arg = 0
        else:
            ss = cmdstr.split()
            print('parse ',cmdstr, ' ', ss)
            cmd = ss[0]
            if len(ss) > 1:
                arg = ss[1]
            else:
                arg = 0
        return cmd, arg

    # read the file line by line and send it line by line
    def retrieveFile(self, filename):
        
        with open(filename, 'r') as fd:
            for aline in fd:
                self.sock.sendall(bytes(aline,'utf-8'))
        
        

    def run(self):
        while True:
            aa = self.sock.recv(1024)
            aa_str = aa.decode('utf-8')
            print('received : ', aa_str)
            # expect this form: cmd a1 
        
            cmd, arg = self.parse(aa_str)
            print('servicing cmd: ',cmd)

            if cmd == 'QUIT':     
                bb = 'Shutdown session'
                print('send response: ',bb)
                bb_bytes = bytes(bb, 'utf-8')
                self.sock.send(bb_bytes)
                self.sock.close()
                break
            elif cmd == 'LIST':
                bblist = os.listdir('.')
                bb = ''
                for a1 in bblist:
                    bb += ' ' + a1 
                bb_bytes = bytes(bb, 'utf-8')
                self.sock.send(bb_bytes)
            elif cmd == 'RETR':
                self.retrieveFile(arg)   # we should check whether arg is real
            else:
                bb = 'response to cmd: ' + cmd + ' is 45'
                print('send response: ',bb)
                bb_bytes = bytes(bb, 'utf-8')
                self.sock.send(bb_bytes)
            

            
s = socket.socket()		 				
s.bind(('', port))		 
print( "socket binded to %s" %(port) )

# put the socket into listening mode 
s.listen(5)	 
print( "socket is listening")			
threads = [] # keep a list of threads so to do a join()

# wait for multiple clients to connect
while True:
    print('server2 waiting on accept')
    conn, (ip, port)  = s.accept()	# tuple of IP and Port of client
    print ('Got connection from ', ip, 'at port: ', port )
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)
    

for t in threads:
    t.join()
print('server2 is done')
     
    

