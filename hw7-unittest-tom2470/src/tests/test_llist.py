from ..llist import LList

import unittest

def some_LList_nodes():
    a = LList.Node("A")
    b = LList.Node("B")
    return a, b

def my_some_LList_nodes():
    a = LList.Node("A")
    b = LList.Node("B")
    c = LList.Node("C")
    return a, b, c

class TestLList(unittest.TestCase):

    def test_append(self):
        '''Start with A-B-C and insert D at the end'''
        a, b = some_LList_nodes()
        x = LList.of(a, b)
        self.assertEquals(x.printme(), "A B")
    
    def test_getitem(self):
        '''Get one of the nodes in the list'''
        a, b, c = my_some_LList_nodes()
        x = LList.of(a, b, c).listme()
        z= LList.of(x[0])
        self.assertEquals(z.printme(), "A")
    
    def test_insert(self):
        '''Start with A-B-C and insert D before C'''
        a, b, c = my_some_LList_nodes()
        x = LList.of(a, b, c)
        d = LList.Node("D")
        x.insert(d)
        self.assertEquals(x.printme(), "A B C D")
    
    def test_insert_at_start(self):
        '''Start with A-B-C and insert D at the beginning'''
        a, b, c = my_some_LList_nodes()
        x = LList.of(a, b, c)
        d = LList.Node("D")
        x.insert(d,c)
        self.assertEquals(x.printme(), "A B D C")

    def test_instance(self):
        '''Create an instance'''
        a, b, c = my_some_LList_nodes()
        x = LList.of(a, b, c)
        d = LList.Node("D")
        x.insert(d,a)
        self.assertEquals(x.printme(), "D A B C")
    
    def test_remove(self):
        '''Remove B from middle of A-B-C'''
        a, b, c = my_some_LList_nodes()
        x = LList.of(a, b, c)
        x.remove(b)
        self.assertEquals(x.printme(), "A C")
    