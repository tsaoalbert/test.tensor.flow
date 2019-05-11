class Node:
    def __init__(self, item = None, nextNode = None):
        self.data = item
        self.next = nextNode
        
class OrderedList:
    def __init__(self):
        self.head = None

    def add(self,item):
        
        current = self.head # start at the beginning
        previous = None # at the beginning of the list, there is no previous
        stop = False # we haven't yet found the place to put the new item

        # find where to put item
        while current != None and not stop:

            # if the current data is bigger than the new item, I've found the place
            if current.getData() > item:
                stop = True # so I can stop

            # I haven't yet found the place to add this, so keep going forward
            else:
                previous = current
                current = current.getNext()

        # At this point, we know where to put the item, we just have to do it

        # Create a Node
        temp = Node(item)

        # the correct place to put this is at the beginning
        if previous == None:
            # we have a new head of the list 
            temp.setNext(self.head)
            self.head = temp

        # the new node goes before current and after previous
        else:
            # connect the new node to current (the new next node)
            temp.setNext(current)
            # connect the previous node to the new node
            previous.setNext(temp)

    def search(self,item):

        # start at the beginning
        current = self.head

        # traverse the list until we find, or we should have if we were gonna
        while current != None:

            # did we find it? return True            
            if current.getData() == item:
                return True
            else:
                # are we gonna find it? no?
                if current.getData() > item:
                    return False # just return false

                # it might still be there so move forward
                else:
                    current = current.getNext()

        return False

    
