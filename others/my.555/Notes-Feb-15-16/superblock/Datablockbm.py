import superblock as sp 
import numpy as np 
import disk

number_cells=disk.BLOCK_SIZE//disk.CELL_SIZE
cell_type = 'int8'
blockBitmap = np.zeros(shape=(number_cells, 1), dtype=cell_type)

def create_bitmap():
    for i in range (sb, first_inode_block, sb.number_inode_block + sb.first_ bitmap)