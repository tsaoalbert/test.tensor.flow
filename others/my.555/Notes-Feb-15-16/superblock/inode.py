import superblock as sb 
import numpy as np 
import disk

idx_valid = 0
idx_size = 1
idx_direct0 = 2
idx_direct1 = 3
idx_direct2 = 4
idx_direct3 = 5
idx_direct4 = 6
idx_indirect = 7

def create_inode():
    iarray  = np.zeros(shape=(sb.number_cells, 1),dtype=sb.cell_type)
    for i in range (sb, first_inode_block, sb.number_inode+sb.first_inode_block):
        write_inode_block(iarray, i)

def write_inode_block(iarray, blockNbr)
    inodeblock = iarray.tobytes()
    disk.disk_write(blockNbr, inodeblock)

def read_inode_block(inode_block)
    aa = disk.disk_read(inode_block)
    ddarray = np.frombuffer(aa, dtype=sb.cell_type)
    returnddarray

def init():
    array_size = disk,BLOCK_SIZE // disk.CELL_SIZE
    cell_type = 'int8'
    inode = np.zeros(shape)
