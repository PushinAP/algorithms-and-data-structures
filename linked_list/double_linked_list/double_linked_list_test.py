import unittest
from double_linked_list import Node
from double_linked_list import LinkedList2 as LinkedList

class TestMethodFind(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(12)
        self.n2 = Node(12)
        self.n3 = Node(55)

    # Без узлов
    def test_find(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.find(12), None)
    # Один узел, элемент который ищем
    def test_find_1(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)

        self.assertEqual(linked_list.find(12), self.n1)
    # Несколько узлов
    def test_find_2(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n3)
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)

        self.assertEqual(linked_list.find(12), self.n1)
    # Один узел, нет узла который ищем
    def test_find_3(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n3)

        self.assertEqual(linked_list.find(12), None)


class TestMethodFindAll(unittest.TestCase):
    def setUp(self):
        self.n1 = Node(12)
        self.n2 = Node(12)
        self.n3 = Node(55)
        self.n6 = Node(1000)
        self.n7 = Node(12)

    # Без узлов
    def test_find_all(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.find_all(12), [])
    # Один узел, элемент который ищем
    def test_find_all_1(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)

        self.assertEqual(linked_list.find_all(12), [self.n1])
    # Несколько узлов
    def test_find_all_2(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n3)
        linked_list.add_in_tail(self.n6)
        linked_list.add_in_tail(self.n7)

        self.assertEqual(linked_list.find_all(12), [self.n1, self.n2, self.n7])

    # Один узел, нет узла который ищем
    def test_find_4(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n3)

        self.assertEqual(linked_list.find_all(12), [])


class TestMethodDelete(unittest.TestCase):
    
    def setUp(self):
        self.n1 = Node(12)
        self.n2 = Node(12)
        self.n3 = Node(55)
        self.n4 = Node(12)
        self.n5 = Node(12)
        self.n6 = Node(1000)
        self.n7 = Node(12)
        self.n8 = Node(12)

    #Удаляем узел из пустого списка
    def test_delete(self):
        linked_list = LinkedList()

        linked_list.delete(12)
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    #Удаление узла из списка с одиним узлом, в котором значение равно удаляемому значению
    def test_delete_1(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)

        linked_list.delete(12)
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

        #Удаление узла из списка с одиним узлом, в котором значение равно удаляемому значению
    def test_delete_2(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)

        linked_list.delete(12)
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)
    #Удаление узла из списка с двумя узлами, значения которых равно удаляемому
    def test_delete_3(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)

        linked_list.delete(12)
        self.assertEqual(linked_list.head, self.n2)
        self.assertEqual(linked_list.tail, self.n2)
        self.assertEqual(linked_list.head.prev, None)
        self.assertEqual(linked_list.head.next, None)

    #Удаление узла из середины списка
    def test_delete_4(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n3)
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n6)

        linked_list.delete(12)
        self.assertEqual(linked_list.head, self.n3)
        self.assertEqual(linked_list.tail, self.n6)
        self.assertEqual(self.n3.next, self.n2)
        self.assertEqual(self.n2.prev, self.n3)
 #Удаление узла из середины списка из конца списка
    def test_delete_5(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n3)
        linked_list.add_in_tail(self.n6)
        linked_list.add_in_tail(self.n1)

        linked_list.delete(12)
        self.assertEqual(linked_list.head, self.n3)
        self.assertEqual(linked_list.tail, self.n6)
        self.assertEqual(self.n6.next, None)
        self.assertEqual(self.n6.prev, self.n3)

#Удаление всех узлов, кроме последнего
    def test_delete_all_1(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n3)

        linked_list.delete(12, True)
        self.assertEqual(linked_list.head, self.n3)
        self.assertEqual(linked_list.tail, self.n3)
        self.assertEqual(linked_list.head.prev, None)

#Удаление всех узлов в начале, середине, конце списка. Должно остаться два узла, не попадающих под требования
    def test_delete_all_2(self):
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
        self.assertEqual(self.n6.prev, self.n3)
        self.assertEqual(self.n6.next, None)
        self.assertEqual(self.n3.prev, None)
        self.assertEqual(self.n3.next, self.n6)

#Удаление абсолютно всех узлов
    def test_delete_all_3(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n2)
        linked_list.add_in_tail(self.n7)
        linked_list.add_in_tail(self.n8)

        linked_list.delete(12, True)
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

class TestMethodInsert(unittest.TestCase):
    
    def setUp(self):
        self.n1 = Node(12)
        self.n2 = Node(12)
        self.n3 = Node(55)
        self.n4 = Node(12)
        self.n5 = Node(12)
        self.n6 = Node(1000)
        self.n7 = Node(12)
        self.n8 = Node(12)

# Вставка перед пустым узлом
    def test_insert(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n3)

        linked_list.insert(None, self.n6)
        self.assertEqual(linked_list.head, self.n1)
        self.assertEqual(linked_list.tail, self.n6)
        self.assertEqual(self.n3.next, self.n6)
        self.assertEqual(self.n6.next, None)
        self.assertEqual(self.n6.prev, self.n3)
        
# Вставка в пустой список
    def test_insert_1(self):
        linked_list = LinkedList()

        linked_list.insert(None, self.n6)
        self.assertEqual(linked_list.head, self.n6)
        self.assertEqual(linked_list.tail, self.n6)

# Вставка перед последнимузлом
    def test_insert_2(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n3)

        linked_list.insert(self.n3, self.n6)
        self.assertEqual(linked_list.head, self.n1)
        self.assertEqual(linked_list.tail, self.n6)
        self.assertEqual(self.n3.next, self.n6)
        self.assertEqual(self.n6.next, None)
        self.assertEqual(self.n6.prev, self.n3)

# Вставка перед первым узлом
    def test_insert_4(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n3)

        linked_list.insert(self.n1, self.n6)
        self.assertEqual(linked_list.head, self.n1)
        self.assertEqual(linked_list.tail, self.n3)
        self.assertEqual(self.n1.next, self.n6)
        self.assertEqual(self.n6.next, self.n3)
        self.assertEqual(self.n6.prev, self.n1)
        self.assertEqual(self.n3.prev, self.n6)

class TestMethodAddInHead(unittest.TestCase):   
    def setUp(self):
        self.n1 = Node(12)
        self.n2 = Node(12)
        self.n3 = Node(55)
        self.n4 = Node(12)
        self.n5 = Node(12)
        self.n6 = Node(1000)
        self.n7 = Node(12)
        self.n8 = Node(12)
#Вставка в начало пустого списка
    def test_add_in_head(self):
        linked_list = LinkedList()

        linked_list.add_in_head(self.n6)
        self.assertEqual(linked_list.head, self.n6)
        self.assertEqual(linked_list.tail, self.n6)

#Вставка в начало cписка с двумя узлами
    def test_add_in_head_1(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        linked_list.add_in_tail(self.n3)

        linked_list.add_in_head(self.n6)
        self.assertEqual(linked_list.head, self.n6)
        self.assertEqual(linked_list.tail, self.n3)
        self.assertEqual(self.n1.prev, self.n6)
        self.assertEqual(self.n6.next, self.n1)
        
#Вставку в начало с одним узлом
    def test_add_in_head_2(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(self.n1)
        
        linked_list.add_in_head(self.n6)
        self.assertEqual(linked_list.head, self.n6)
        self.assertEqual(linked_list.tail, self.n1)
        self.assertEqual(self.n1.prev, self.n6)
        self.assertEqual(self.n6.next, self.n1)
        

   
if __name__ == '__main__':
    unittest.main()