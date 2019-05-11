
# coding: utf-8

# In[10]:

# Stacks and Queues
# Stack --> LIFO Last in first out
# Queue --> FIFO First in first out

class EmptyStackException(Exception):
    def __init__(self):
        super().__init__('The stack is empty.')
        
class Stack:
    def __init__(self):
        '''
        create a blank stack
        '''
        self.data = [None]
        self.length = 0
    
    def resize(self):
        '''
        resize the "array" to add or subtract necessary capacity
        '''
        if self.length == len(self.data):
            self.data = self.data + [None] * (self.length + 1)
        elif self.length < len(self.data) / 4:
            self.data = self.data[:int(self.length * 2 + 1)]

    def is_empty(self):
        '''
        return true or false that the stack is empty
        '''
        return self.length == 0
    
    def peek(self):
        '''
        view the item at the top of the stack
        '''
        if self.is_empty():
            raise EmptyStackException
            
        return self.data[self.length - 1]
    
    def push(self, x):
        '''
        add an item to the top of the stack
        '''
        self.resize()
        
        self.data[self.length] = x
        self.length += 1
        
    def pop(self):
        '''
        remove and view the top item on the stack
        '''
        self.resize()
        
        if self.is_empty():
            raise EmptyStackException
            
        self.length -= 1
        return self.data[self.length]


class Node:
    '''
    Linked list node
    '''
    def __init__(self, Data = None, Next = None):
        self.data = Data
        self.next = Next

class LinkedStack:
    '''
    Stack but using a linked list
    '''
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def peek(self):
        '''
        view the item at the top of the stack
        '''
        if self.is_empty():
            raise EmptyStackException
            
        return self.head.data
    
    def push(self, x):
        '''
        add an item to the top of the stack
        '''
        self.head = Node(x, self.head)
        
    def pop(self):
        '''
        remove and view the top item on the stack
        '''
        if self.is_empty():
            raise EmptyStackException

        x = self.head.data
        self.head = self.head.next
        return x
        
    
x = LinkedStack()
x.push(1)
x.push(2)
x.push(3)
x.push(5)

while not x.is_empty():
    print(x.pop())
    

# In[ ]:

# Queue
# First in first out

class EmptyQueueException(Exception):
    def __init__(self):
        super().__init__('The queue is empty')

class Queue:
    '''
    array based
    '''

    def __init__(self):
        '''
        create an empty queue
        '''
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if self.is_empty():
            raise EmptyQueueException

        return self.data[0]

    def enqueue(self, x):
        '''
        put an item into the list
        '''
        self.data.append(x)

    def dequeue(self):
        '''
        remove an item and know its value
        removed from the beginning of the list
        First in First out
        '''
        return self.data.pop(0)


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            raise EmptyQueueException

        return self.head.data

    def enqueue(self, x):
        '''
        put an item into the list
        '''
        if self.is_empty():
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next   # new end of queue

    def dequeue(self):
        '''
        remove an item and know its value
        removed from the beginning of the list
        First in First out
        '''
        if self.is_empty():
            raise EmptyQueueException

        x = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        return x


y = LinkedQueue()
y.enqueue(12)
y.enqueue('dog')
y.enqueue(3.14159)

while not y.is_empty():
    print (y.dequeue())



# In[ ]:

# examples of applications
# networking... packet queues
# process models... ordering, shipping, etc.


# In[ ]:



