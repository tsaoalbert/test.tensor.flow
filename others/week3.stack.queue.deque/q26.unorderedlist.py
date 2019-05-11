#!/usr/bin/env python
"""
3.26. Design and implement an experiment that will compare the performance of the Python list based stack and queue 
  with the linked list implementation.
"""
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
            
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
        
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
                
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
mylist = UnorderedList()

num_repeats=1
time_mylist_enqueue = timeit.Timer("for i in L: lis.enqueue(i)", "from __main__ import lis,L")
time_mylist_dequeue = timeit.Timer("for i in L: lis.dequeue(i)", "from __main__ import lis,L")
print("%8d: %15.5f %15.5f " %(n, time_mylist_enqueue, time_mylist_dequeue  ))
