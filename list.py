class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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

        if self.len() == 1 and node.value == val:
            self.head = None
        else :
            while node is not None:
                if self.head.value == val:
                    self.head = node.next
                    if not all:
                        break
                elif node.value == val:
                    prev_node.next = node.next
                    if not all:
                        if node == self.tail:
                            self.tail = prev_node
                        break
                else:
                   prev_node = node
                node = node.next

        if self.head is None:
            self.tail = None
        elif self.len() == 1:
            self.tail = self.head
        elif all:
            self.tail = prev_node


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
        if afterNode is None:
            self.head = newNode
            self.tail = newNode
        elif afterNode == self.tail:
            afterNode.next = newNode
            self.tail = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode