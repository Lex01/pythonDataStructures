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
        self.head == None
    def add(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
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
    def append(self, item):
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        node = Node(item)
        current.setNext(node)

class OrderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        self.head == None
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def remove(self, item):
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

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData > item:
                stop = True
            else:
                current = current.getNext()
        return found
    def add(self, item):
        current = self.head
        previous = None
        while current != None and current.getData() < item:
            previous = current
            current = current.getNext()
            
        node = Node(item)

        if previous == None:
            node.setNext(current)
            self.head = node
        else:
            previous.setNext(node)
            node.setNext(current)

aList = OrderedList()
aList.add(1)
aList.add(5)
aList.add(3)
aList.remove(5)
print(aList.size())



# temp = Node(23)
# print(temp.getData())
#
# newList = UnorderedList()
# newList.add(1)
# newList.add(2)
# newList.add(3)
# print(newList.size())
# print(newList.search(5))
# newList.remove(2)
# newList.append(6)
# newList.append(6)
# print(newList.size())


