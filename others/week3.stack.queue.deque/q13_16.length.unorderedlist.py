#!/usr/bin/env python
"""
To implement the length method, we counted the number of nodes in the list. An alternative strategy would be to store the number of nodes in the list as an additional piece of data in the head of the list. Modify the UnorderedList class to include this information and rewrite the length method.

Implement the remove method so that it works correctly in the case where the item is not in the list.

Modify the list classes to allow duplicates. Which methods will be impacted by this change?

Implement the __str__ method in the UnorderedList class. What would be a good string representation for a list?
"""
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.count = 0
        self.head = None

    def isEmpty(self):
        return self.count == 0
        #return self.head == None
            
    def add(self,item):
        self.count += 1
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def __getitem__(self,i):
        cnt = 0 
        current = self.head
        while current != None and cnt < i :
            current = current.getNext()
            cnt += 1
        if ( current==None):
          return None
        else:
          return current.getData()
        
    def __str__(self):
        ans = []
        current = self.head
        while current != None:
            ans.append( current.getData() )
            current = current.getNext()
        return str (ans)
        
    def length(self): 
        return self.count

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
        self.count -= 1
        previous = None
        found = False
        while current!=None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
          if previous == None:
            self.head = current.getNext()
          else:
            previous.setNext(current.getNext())
        else:
          print ( "Cannot remove %d" % (item) )
            
mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print("length=", mylist.length())
print("search(93)=", mylist.search(93))
print("search(100)=", mylist.search(100))

mylist.add(100)
print("search(100)=", mylist.search(100))
print("length=", mylist.length())

mylist.remove(54)
print("length=", mylist.length())
mylist.remove(93)
print("length=", mylist.length())
mylist.remove(31)
print("length=", mylist.length())
print("search(93)=%d"% (mylist.search(93)))
mylist.remove(93)
print("myList=%s"% (mylist))
print("myList[0]=%s"% (mylist[0]))
