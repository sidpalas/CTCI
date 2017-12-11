#singly linked list
#https://github.com/johnshiver/algorithms/tree/master/linked_list

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        if self.tail == None:
            self.tail = new_node

    #added an append method to add things to the tail
    def append(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.insert(data)
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def printList(self):
        current = self.head
        while current:
            print current.get_data()
            current = current.get_next()
