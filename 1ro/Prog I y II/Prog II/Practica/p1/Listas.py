
class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class Linked_List():
    def __init__(self):
        self.first = None
        self.last = None
    
    def insert_first(self, data):
        if self.empty():
            self.first = Node(data)
            self.last = Node(data)
        else: 
            self.first = Node(data, self.first)

    def insert_last(self, data):
        if self.empty():
            self.first = Node(data)
            self.last = Node(data)
        else: 
            newNode = Node(data)
            self.last.next = newNode
            self.last = newNode
    
    def empty(self):
        return self.first == None or self.last == None

    def is_element(self, data):
        node = self.first
        while node != None:
            if node.data == data:
                return True
            node = node.next
        return False
    
    def print_elements(self):
        node = self.first
        while node != None:
            print(node.data, end='')
            node = node.next
    
    def del_first(self):
        nodeToDel = self.first
        self.first = nodeToDel.next
    
    def del_last(self):
        node = self.first
        if node == self.last: 
            self.first = None
            self.last = None
        while node.next.next != None:
            node = node.next
        self.last = node
        node.next = None

    def concat(self, list2):
        self.last.next = list2.first
        self.last = list2.last

#falta hacer
class Native_Linked_List():
    def __init__(self):
        self.first = None
        self.last = None
    
    def insert_first(self, data):
        if self.empty():
            self.first = Node(data)
            self.last = Node(data)
        else: 
            self.first = Node(data, self.first)

    def insert_last(self, data):
        if self.empty():
            self.first = Node(data)
            self.last = Node(data)
        else: 
            newNode = Node(data)
            self.last.next = newNode
            self.last = newNode
    
    def empty(self):
        return self.first == None or self.last == None

    def is_element(self, data):
        node = self.first
        while node != None:
            if node.data == data:
                return True
            node = node.next
        return False
    
    def print_elements(self):
        node = self.first
        while node != None:
            print(node.data, end='')
            node = node.next
    
    def del_first(self):
        nodeToDel = self.first
        self.first = nodeToDel.next
    
    def del_last(self):
        node = self.first
        if node == self.last: 
            self.first = None
            self.last = None
        while node.next.next != None:
            node = node.next
        self.last = node
        node.next = None

    def concat(self, list2):
        self.last.next = list2.first
        self.last = list2.last
