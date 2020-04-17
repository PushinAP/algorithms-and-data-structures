class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head

        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        list_values_found = []
        while node is not None:
            if node.value == val:
                list_values_found.append(node)
            node = node.next
        return list_values_found

    def delete(self, val, all=False):
        node = self.head

        while node is not None:
            if self.head.value == val:
                self.head = node.next
                if self.head is not None:
                    self.head.prev = None

                if self.head is not None and self.head.next is None:
                    self.tail = self.head
                
                if not all: break
            elif node.value == val:
                node.prev.next = node.next
                if node.next is not None: node.next.prev = node.prev
                if node == self.tail:
                    self.tail = node.prev
                if not all: break
            node = node.next
      

        if self.head is None:
            self.tail = None


    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None and self.len() > 1:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        elif afterNode is None:
            self.head = newNode
            self.tail = newNode
        elif afterNode == self.tail:
            newNode.prev = afterNode
            afterNode.next = newNode
            self.tail = newNode
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            afterNode.next = newNode


    def add_in_head(self, newNode):
        if self.head is None:
            newNode.prev = None
            newNode.next = None
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode

        self.head = newNode