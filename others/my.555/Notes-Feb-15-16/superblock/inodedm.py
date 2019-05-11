
import superblock as sb
import numpy as np 
import disk



def create_inodebm():
    iarray  = np.zeros(shape=(sb.number_cells, 1),dtype=sb.cell_type)
    for i in range (sb, first_inodebm_block, sb.number_inodebm+sb.first_inode_block):
        write_inodebm_block(iarray, i)

def write_inodebm_block(iarray, blockNbr):
    inodebmblock = iarray.tobytes()
    disk.disk_write(blockNbr, inodeblock)

def read_inodebm_block(inodebm_block):
    aa = disk.disk_read(inodebm_block)
    ddarray = np.frombuffer(aa, dtype=sb.cell_type)
    returnddarray

def init():
    array_size = disk,BLOCK_SIZE // disk.CELL_SIZE
    cell_type = 'int8'
    inodebm = np.zeros(shape)