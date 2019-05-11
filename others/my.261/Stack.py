# Stack

class EmptyStackException(Exception):
    def __init__(self):
        super().__init__('Empty Stack')
        
class Stack:
    def __init__(self):
        self.data = []
        self.length = 0

    def peek(self):
        '''
        Look at the top item

        Return the value on the "top" of the Stack
        '''
        return self.data[self.length - 1]

    def pop(self):
        '''
        Remove the last item
        Return the value on the "top" of the Stack, then delete it
        '''
        if self.is_empty():
            raise EmptyStackException()
        self.length -= 1
        return self.data[self.length]

        pass

    def resize(self, n):
        # make a new 'array'
        new_array = [None] * n
        new_array[:len(self.data)] = self.data[:]
        self.data = new_array
            
    def push(self, x):
        if self.length == len(self.data):
            # ADD MORE CAPACITY
            self.resize(self.length * 2 + 1)

        self.data[self.length] = x
        self.length += 1
        pass

    def is_empty(self):
        return self.length == 0

'''
def func_rec(x = 0):
    print (x)
    return func_rec(x + 1)

func_rec()
'''

x = Stack()
x.push(5)
x.push(6)
x.push(7)
x.push(8)

while not x.is_empty():
    print(x.pop())

x.push('giraffe')
print (x.data)
