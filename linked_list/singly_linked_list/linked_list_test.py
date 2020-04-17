import unittest
from list import Node
from list import LinkedList

class TestList(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(12)
        self.n2 = Node(12)
        self.n3 = Node(55)
        self.n4 = Node(12)
        self.n5 = Node(12)
        self.n6 = Node(1000)
        self.n7 = Node(12)
        self.n8 = Node(12)
    
    def test_len_0_elements(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.len(), 0)

    def test_len_1_elements(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)

        self.assertEqual(linked_list.len(), 1)

    def test_len_3_elements(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n3)

        self.assertEqual(linked_list.len(), 3)

    def test_clean(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n3)
        linked_list.clean()

        self.assertEqual(linked_list.len(), 0)

    def test_find_all_1(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.find_all(57), [])

    def test_find_all_2(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.find_all(57), [])

    def test_find_all_3(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)

        self.assertEqual(linked_list.find_all(12), [self.n1])

    
    def test_find_all_4(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)

        self.assertEqual(linked_list.find_all(874), [])

    def test_find_all_5(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n3)
        linked_list.add_in_tail(self.n4)
        linked_list.add_in_tail(self.n5)

        self.assertEqual(linked_list.find_all(12), [self.n1, self.n2, self.n4, self.n5])

    def test_insert_1(self):
        linked_list = LinkedList()

        linked_list.insert(None, self.n1)
        self.assertEqual(linked_list.head, self.n1)
        self.assertEqual(linked_list.tail, self.n1)

    def test_insert_2(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n3)

        linked_list.insert(self.n3, self.n4)

        self.assertEqual(self.n3.next, self.n4)
        self.assertEqual(linked_list.tail, self.n4)

    def test_insert_3(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n3)

        linked_list.insert(self.n2, self.n6)

        self.assertEqual(self.n2.next, self.n6)
        self.assertEqual(self.n6.next, self.n3)

    def test_delete_1(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n3)

        linked_list.delete(12)

        self.assertEqual(linked_list.head, self.n2)
        self.assertEqual(linked_list.tail, self.n3)


    def test_delete_2(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)

        linked_list.delete(12)

        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)
    
    def test_delete_3(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n3)
        linked_list.add_in_tail(self.n4)

        linked_list.delete(12)
        self.assertEqual(linked_list.head, self.n3)
        self.assertEqual(linked_list.tail, self.n3)

    def test_delete_4(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n3)
        linked_list.add_in_tail(self.n4)
        linked_list.add_in_tail(self.n6)
        
        linked_list.delete(12)

        self.assertEqual(linked_list.head, self.n3)
        self.assertEqual(self.n3.next, self.n6)
        self.assertEqual(linked_list.tail, self.n6)

    def test_delete_5(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)

        linked_list.delete(12)
        self.assertEqual(linked_list.head, self.n2)
        self.assertEqual(linked_list.tail, self.n2)

    def test_delete_6(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n3)
        linked_list.add_in_tail(self.n6)
        linked_list.add_in_tail(self.n4)

        linked_list.delete(12)
        
        self.assertEqual(linked_list.head, self.n3)
        self.assertEqual(linked_list.tail, self.n6)
    
    def test_delete_7(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n6)
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n4)

        linked_list.delete(12)
        self.assertEqual(linked_list.head, self.n6)
        self.assertEqual(linked_list.tail, self.n4)

    def test_delete_8(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n4)

        linked_list.delete(12)
        self.assertEqual(linked_list.head, self.n2)
        self.assertEqual(linked_list.tail, self.n4)


    def test_delete_all_1(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)

        linked_list.delete(12, True)
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_delete_all_2(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n3)
        linked_list.add_in_tail(self.n2)

        linked_list.delete(12, True)
        self.assertEqual(linked_list.head, self.n3)
        self.assertEqual(linked_list.tail, self.n3)

    def test_delete_all_3(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n3)
        linked_list.add_in_tail(self.n4)
        linked_list.add_in_tail(self.n5)
        linked_list.add_in_tail(self.n6)
        linked_list.add_in_tail(self.n7)
        linked_list.add_in_tail(self.n8)


        linked_list.delete(12, True)
        self.assertEqual(linked_list.head, self.n3)
        self.assertEqual(linked_list.tail, self.n6)
        self.assertEqual(self.n3.next, self.n6)


if __name__ == '__main__':
    unittest.main()



    