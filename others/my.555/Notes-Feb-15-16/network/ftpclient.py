from cmd import Cmd
import socket

OK = '200'
BAD = '500'

class MyPrompt(Cmd):

    def __init__(self):
        super().__init__()
        self.myc = None

    def parse_args(self, args):
        if len(args) == 0:
            nn = None
            nnlen = 0
        else:
            nn = args.split()
            nnlen = len(nn)
        return nn,nnlen

    def do_bye(self, args):
        """close connection with remote host"""
        self.myc.bye()
        self.myc = None
        print('connection with remote host CLOSED')

    def do_cd(self, args):
        """Change remote current directory to given path. cd <dir name>
           to go up the directory use: cd ..
        """
        self.myc.send_cmd('CWD', args=args)


    def do_connect(self, args):
        """connect to ftp server. connect <ip> <port>. 
           connect without arguments defaults to localhost and port 21"""

        # default parameters
        
        port = 21
        ip = '127.0.0.1'

        # print('args: ',args)
        nn, nnlen = self.parse_args(args)
        if nnlen > 0:
            ip = nn[0]
            if nnlen == 2:
                port = int(nn[1])  # not many error checking
        
        self.myc = MyConnection(ip, port)
        if self.myc.connect():
            print ("Connection to ", ip, ':', port, ' SUCCESSFUL')
        else:
            print("Connection failure")

    def do_exit(self, args):
        """Exit the program."""
        print ("Exit program.")
        if self.myc != None:
            self.myc.bye()
        raise SystemExit

    def do_ls(self, args):
        """ls - list the contents of current directory: ls """
        
        if self.myc == None:
            print("No connection to host.. Do a 'connect' first ")
        else:
            results = self.myc.send_cmd('LIST',expect_result=True) 
            rarray = results.split()
            count = 0
            print()
            for aa in rarray:
                print(aa.ljust(20), sep='',end='')
                count += 1
                if count >= 3:
                    print()
                    count = 0
            print()
            print()


class MyConnection():

    def __init__(self, ip, port):
        self.controlsocket = None
        self.datasocket = None
        self.ip = ip
        self.controlport = port
        self.dataport = 12345
        self.listensocket = None

    def send_cmd(self, command, expect_result=False, args=None):
        results = ''
        incoming = command
        if args != None:
            incoming += ' ' + args

        aline_bytes = bytes(incoming, 'utf-8')
        self.controlsocket.send(aline_bytes)

        # assume that most status codes are less than 100
        status = self.controlsocket.recv(100)
        print('status: ', status.decode('utf-8'))

        # should check for status but for now ignore

        if expect_result:
            results = self.datasocket.recv(1024)  
                            # clearly I should be getting the whole thing with 
                            # multiple recv
            return results.decode('utf-8')
        return results

    def connect(self):
        self.controlsocket = socket.socket()
        self.controlsocket.connect((self.ip, self.controlport))

        # set up the data port
        self.listensocket = socket.socket()
        self.listensocket.bind(('', self.dataport))
        self.listensocket.listen(1)

        port_cmd = 'PORT ' +  str(self.dataport)
        self.controlsocket.send(bytes(port_cmd,'utf-8'))

        self.datasocket, (ipd, portx) = self.listensocket.accept()

        print('data socket accepted from ',ipd, ' at port ', portx)

        self.controlsocket.send(bytes(OK, 'utf-8'))

        return True

    def bye(self):
        self.controlsocket.close()
        self.listensocket.close()
        self.datasocket.close()
        self.controlsocket.close()

#
#====================================================
#
if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'ftp> '
    prompt.cmdloop('Starting ftp client ...')