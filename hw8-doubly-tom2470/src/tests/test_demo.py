from ..dllist import DLList

import unittest

def some_DLList_nodes():
    a = DLList.Node("A")
    b = DLList.Node("B")
    c = DLList.Node("C")
    d = DLList.Node("D")
    return a, b, c, d

class TestLList(unittest.TestCase):

    def start_test(self):
        '''starting test function'''
        a, b, c, d = some_DLList_nodes()
        x = DLList.of(a, b, c, d)
        self.assertEquals(x.printme(), "A B C D")
    def test_head(self):
        '''test head by removing different elements'''
        a, b, c, d = some_DLList_nodes()
        x = DLList.of(a, b, c, d)
        self.assertEquals(x.head, a)
        x=x.remove(a)
        self.assertEquals(x.head, b)
        x=x.remove(x.tail)
        self.assertEquals(x.head, b)
        x=x.insert(a)
        self.assertEquals(x.head, b)
        x=x.insert(d,b)
        self.assertEquals(x.head, d)
    def test_tail(self):
        '''test tail by removing different elements'''
        a, b, c, d = some_DLList_nodes()
        x = DLList.of(a, b, c, d)
        self.assertEquals(x.tail, d)
        x=x.remove(d)
        self.assertEquals(x.tail, c)
        x=x.remove(b)
        self.assertEquals(x.tail, c)
        x=x.insert(d)
        self.assertEquals(x.tail, d)
        x=x.insert(b,d)
        self.assertEquals(x.tail, d)
    def test_iter(self):
        '''test the iterable attrubutes of double linked list'''
        a, b, c, d = some_DLList_nodes()
        x = DLList.of(a, b, c, d)
        self.assertEquals(list(x),[a,b,c,d])
        for i, node in enumerate([a, b, c, d]):
            self.assertEquals(list(x)[i], node)