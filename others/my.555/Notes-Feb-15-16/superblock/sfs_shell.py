from cmd import Cmd
import disk
import superblock as sb

class MyPrompt(Cmd):
    prompt = 'sfs> '
    intro = "Welcome to simple file system shell! \n Type ? to list commands"

    # disk commands from disk.py
    def do_disk_init(self, inp):
        """
        createa file and initialize with blocks of data
        do an open file and close file
        """
        disk.disk_init()

    def do_disk_open(self, inp):
        """
        open a file for disk interface. Do a mount of a file system
        """
        disk.disk_open()

    def do_disk_close(self, tnp):
        """
        close a file for disk interface. An unmount of a file system
        """
        disk.disk_close()

    def do_write_nbr(self, inp):
        """
        Write a number < 256  to a given block number
        writeNbr <blockNumber> <aNumber>
        """
        blockNbr, anumber = inp.split(" ")
        print('blockNbr = ',blockNbr, '    anumber = ', anumber)
        blockNbr = int(blockNbr)
        anumber = int(anumber)
        disk.writeNbr(blockNbr, anumber)

    def do_sb_init(self, inp):
        """
        sb functionality
        """
        sb.init_superblock()


    def do_disk_read(self, inp):
        """
        read from a given block
        display contents of block
        """
        blocknbr = int(inp)
        buffer = disk.disk_read(blocknbr)
        print('blocknbr[',blocknbr,'] buffer: ',buffer, end='\n\n')


    def do_exit(self, inp):
        """
        exit the sfs shell
        """
        print('Exit sfs interactive shell\n\n')
        return True

if __name__ == "__main__":
    MyPrompt().cmdloop()
    print('after')
