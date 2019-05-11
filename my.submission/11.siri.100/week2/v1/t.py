
class newDeque:
    def __init__(self):
        self.items = doublyLinkedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def addFront(self, item):
        self.items.addFront (item)

    def addRear(self, item):
        self.items.addRear (item)

    def removeFront(self):
        return self.items.removeFront()

    def removeRear(self):
        return self.items.removeRear()

    def size(self):
        return self.items.length()


class newStack:
    def __init__(self):
        self.items = doublyLinkedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def __str__(self):
      return str ( self.items )

    def push(self, item):
        self.items.addRear(item)

    def pop(self):
        return self.items.removeRear()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def testNewStack (n):
    x = newStack()
    for i in range (n):
        x.push(i)
    print (x)
    for i in range (n):
        x.pop()
    assert (x.isEmpty())

testNewStack(10)



class newQueue:
    def __init__(self):
        self.items = doublyLinkedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def enqueue(self, item):
        self.items.addRear(item)
        
    def dequeue(self):
        return self.items.removeFront()

    def size(self):
        return len(self.items)


def testNewQueue(n):
    x = newQueue()
    for i in range (n):
        x.enqueue(i)
    print (x)
    for i in range (n):
        x.dequeue()  
    assert (x.isEmpty())
testNewStack(10)


