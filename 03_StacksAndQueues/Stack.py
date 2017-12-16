#Stack implemneted with singly linked list
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


class Stack(object):

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        new_node = Node(data)
        new_node.set_next(self.top)
        self.top = new_node

    def pop(self):
        value = self.top.get_data()
        self.top = self.top.get_next()
        return value

    def peek(self):
        if self.top:
            return self.top.get_data()
        else:
            return None

    def printStack(self):
        current = self.top
        while current:
            print current.get_data()
            current = current.get_next()
