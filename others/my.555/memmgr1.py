import numpy as np

class MemMgr:
    NOMEMORY = 99
    row_size = 7               # max number of rows
    column_size = 6            # max number of columns
    mgmt_row_size = row_size    # max number of rows for mgmt
    mgmt_column_size = 1        # max number of columns for mgmt
                                #  -- one column of pid
    pid_column = 0              # column for pid

    # memory array to represent memory we manage
    mem = np.zeros(shape=(row_size, column_size), dtype='int8')

    # management of memory - an array of process identifiers pid
    mgmt = np.zeros(shape=(mgmt_row_size, mgmt_column_size), dtype='int32')

    @classmethod
    def get_mem(cls, pid : int, nbr_blocks : int) :
        """ Look for contiguous memory blocks. 
            return a number of blocks in the form of an array
        """
        pass

    @classmethod
    def release_mem(cls, pid : int):
        """ release memory that had been assigned to pid
            no return value
        """
        pass


#
# These are debugging functions
#
    
    @classmethod
    def display_mem(cls):
        """ print out the contents of memory array
        """
        pass

    @classmethod
    def display_mgmt(cls):
         """ Display what is in the management structure
         """


class Merror (Exception):

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)