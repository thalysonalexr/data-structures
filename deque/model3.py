__author__ = 'Thalyson A. R. de Sousa'
__date__ = '2017-02-28'

'''
Lista duplamente encadeada (lista encadeada cabeça-cauda).
'''


class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None
        self.prev = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, pointer):
        self.__next = pointer

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, pointer):
        self.__prev = pointer


class Deque(Node):
    def __init__(self, elem_class):
        self.elem_class = elem_class
        self.__length = 0
        self.head = None
        self.tail = None

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, pointer):
        self.__head = pointer

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, pointer):
        self.__tail = pointer

    def __len__(self):
        return self.length

    def check_type(self, elem):
        if type(elem) != self.elem_class:
            raise TypeError('Invalid type. The list is %s.' % self.elem_class.__name__)

    def is_empty(self):
        return self.head is None

    def insert_value(self, idx, value):
        node = self.head
        i = 0
        while node is not None:
            if idx == i:
                node.value = value
                return
            i += 1
            node = node.next

    def index_of(self, idx):
        node = self.head
        i = 0
        while node is not None:
            if idx == i:
                return node.value
            i += 1
            node = node.next

    def insert_head(self, value):
        self.check_type(value)
        newnode = Node(value)
        if self.is_empty():
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.__length += 1

    def insert_tail(self, value):
        self.check_type(value)
        newnode = Node(value)
        if self.is_empty():
            self.head = self.tail = newnode
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        self.__length += 1

    def remove_head(self):
        if self.is_empty():
            return None
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.pre = None
        self.__length -= 1

    def remove_tail(self):
        if self.is_empty():
            return None
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.__length -= 1

    def linear_search(self, value):
        self.check_type(value)
        if self.is_empty():
            return None
        node = self.head
        i = 0
        while node is not None:
            if value == node.value:
                return i
            node = node.next
            i += 1
        return -1

    def search_binary(self, value):
        self.check_type(value)
        if self.is_empty():
            return None
        first = 0
        last = self.__length-1
        while first <= last:
            mid = (first + last) // 2
            if value > self.index_of(mid):
                first = mid + 1
            elif value < self.index_of(mid):
                last = mid - 1
            else:
                return mid
        return -1

    def slice_list(self, idx, right=True):
        newlist = Deque(self.elem_class)
        if right:
            while idx < self.__length:
                newlist.insert_tail(self.index_of(idx))
                idx += 1
        else:
            idx -= 1
            while idx >= 0:
                newlist.insert_head(self.index_of(idx))
                idx -= 1
        return newlist

    def insertion_sort(self):
        if self.is_empty() or self.__length == 1:
            return None
        for i in range(1, self.__length):
            element = self.index_of(i)
            j = i
            while j > 0 and element < self.index_of(j-1):
                temp = self.index_of(j-1)
                self.insert_value(j-1, self.index_of(j))
                self.insert_value(j, temp)
                j -= 1

    def selection_sort(self):
        if self.is_empty() or self.__length == 1:
            return None
        for i in range(self.__length):
            smaller = i
            for j in range(i, self.__length):
                if self.index_of(j) < self.index_of(smaller):
                    smaller = j
            temp = self.index_of(i)
            self.insert_value(i, self.index_of(smaller))
            self.insert_value(smaller, temp)

    def bubble_sort(self):
        if self.is_empty() or self.__length == 1:
            return None
        for i in range(self.__length):
            swapped = False
            for j in range(self.__length-1):
                _current = self.index_of(j)
                _next = self.index_of(j+1)
                if _current > _next:
                    self.insert_value(j, _next)
                    self.insert_value(j+1, _current)
                    swapped = True
            if not swapped:
                return

    def print_elements_left(self):
        if self.is_empty():
            return None
        node = self.tail
        print('| ', end='')
        while node is not None:
            print(node.value, end=' | ')
            node = node.prev

    def print_elements_right(self):
        if self.is_empty():
            return None
        node = self.head
        print('| ', end='')
        while node is not None:
            print(node.value, end=' | ')
            node = node.next

d = Deque(int)
# d.insert_head(1)
# d.insert_tail(2)
# d.insert_tail(3)
# n = d.slice_list(2, False)
# n.print_elements_right()
# d.remove_tail()
# d.remove_head()
# d.check_type(1)
# d.search_binary(3)
# d.linear_search(2)
# d.is_empty()
# d.insert_value(0, 5)
# d.index_of(2)
# d.insertion_sort()
# d.selection_sort()
# d.bubble_sort()
# d.print_elements_right()
# d.print_elements_left()
