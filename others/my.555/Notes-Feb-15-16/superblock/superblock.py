import numpy as np 
import disk

def init_superblock():
    blocks = {'Megic_number':12345,
              'Number of Blocks':64,
              'Number of inodes per block':32,
              'Number of inodes':3,
              'Directory inode(dentry)':0,
              'DataBlock bitmap':2,
              'First datablock':6,
              'First inode block':6}
    number_cells=disk.BLOCK_SIZE//disk.CELL_SIZE
    cell_type = 'int32'
    sb_array = np.zeros(shape=(number_cells, 1), dtype=cell_type)

    for i, k in blocks.items():
        print(i,k)
        sb_array[i]=k

    to_bytes = sb_array.tobytes()

    #print(to_bytes)

    print('before')
    #disk.disk_write(0, to_bytes)
    print('after')
    return to_bytes