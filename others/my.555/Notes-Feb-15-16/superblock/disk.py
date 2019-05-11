BLOCK_SIZE = 128 # change to any size but make sure 
                # it is divisible by 4
NUMBER_BLOCKS = 32 # number of blocks 

FILENAME = "disk.sfs"

dff = 0     # deal iwth only one instance of a disk
            # this variable is returned to the caller 

# constants for cell size within each block required
# by superblocks and inodes

CELL_SIZE = 4  # 4 bytes per cell.


def writeNbr(blockNbr, anumber):
    """
    Write a number to the designated block number
    """
    buffer = bytearray(BLOCK_SIZE)
    for i in range(0,BLOCK_SIZE):
        buffer[i] = anumber
    disk_write(blockNbr, buffer)

#
# low level file IO functions to emulate a disk 
#

def disk_open() :
    """
    open the file as a disk. Essentially doing a mount
    """
    global dff
    dff = open(FILENAME, 'rb+')


def disk_read( blocknum ) :
    """
    read a particular diskblock into memory.
    Error handling of bad reads are not handled. It's up to you
    """
    global dff
    offset = blocknum * BLOCK_SIZE
    try:
        dff.seek(offset,0)
        b2 = dff.read(BLOCK_SIZE)
        return b2
    except IOError as e:
        print('read exception: ', e.errno, " : ",e.strerror)
    except:
        print("other read errors")
    return None


def disk_write( blocknum, data ) :
    """
    Write a given data to a given block on disk. Size of data has to BLOCK_SIZE
    Error handling of bad writes are not handled. It's up to you.
    If everything is good, return True else False
    """
    global dff
    offset = blocknum * BLOCK_SIZE
    try:
        dff.seek(offset, 0)
        dff.write(data)
        return True
    except IOError as e:
        print('write exception: ', e.errno, " : ",e.strerror)
    except Exception as ex:
        print("other write errors: ", ex.__str__)
    return False


def disk_close():
    """
    Close the disk. Essentially an unmount.
    """
    global dff
    dff.close()
    
def disk_init():
    """
    Initialize a given file with filename as a virtual disk.
    Do this only once. File is closed after operation.
    """
    b1 = bytearray(BLOCK_SIZE)
    with open(FILENAME, "ab+") as df:
        [df.write(b1) for ii in range(NUMBER_BLOCKS)]
