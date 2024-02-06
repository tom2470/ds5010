from ..dllist import DLList

import unittest

def create_nodes():
    a = DLList.Node("A")
    b = DLList.Node("B")
    c = DLList.Node("C")
    d = DLList.Node("D")
    return a, b, c, d

class TestDLList(unittest.TestCase):

    def test_instance(self):
        '''Create a list'''
        a, b, c, d = create_nodes()
        x = DLList.of(a, b, c, d)
        self.assertEquals(str(x), "A B C D")
    
    def test_empty(self):
        '''Create an empty list (head and tail are None)'''
        x = DLList.of()
        self.assertEquals(x.head, None)
        self.assertEquals(x.tail, None)
        self.assertEquals(str(x), "Empty")

    def test_getitem(self):
        '''Get individual nodes in the list'''
        a, b, c, d = create_nodes()
        x = DLList.of(a, b, c, d)
        for i, node in enumerate([a, b, c, d]):
            self.assertEquals(list(x)[i], node)
        self.assertEquals(x.head, a)
        self.assertEquals(x.tail, d)

    def test_insert(self):
        '''Start with A-B-C and insert D before C'''
        a, b, c, d = create_nodes()
        x = DLList.of(a, b, c).insert(d, c)
        self.assertEquals(str(x), "A B D C")

    def test_append(self):
        '''Start with A-B-C and insert D at the end'''
        a, b, c, d = create_nodes()
        x = DLList.of(a, b, c).insert(d)
        self.assertEquals(str(x), "A B C D")

    def test_insert_at_start(self):
        '''Start with A-B-C and insert D at the beginning'''
        a, b, c, d = create_nodes()
        x = DLList.of(a, b, c).insert(d, a)
        self.assertEquals(str(x), "D A B C")

    def test_insert_into_empty(self):
        '''Insert into an empty list'''
        a, b, c, d = create_nodes()
        x = DLList.of().insert(d)
        self.assertEquals(list(x)[0], d)
        self.assertEquals(str(x), "D") 

    def test_remove(self):
        '''Remove D from middle of A-B-D-C'''
        a, b, c, d = create_nodes()
        x = DLList.of(a, b, d, c)
        self.assertEquals(str(x), "A B D C")
        x = x.remove(d)
        self.assertEquals(str(x), "A B C")

    def test_remove_from_head(self):
        '''Remove D from the head of D-A-B-C'''
        a, b, c, d = create_nodes()
        x = DLList.of(d, a, b, c)
        self.assertEquals(str(x), "D A B C")
        x = x.remove(d)
        self.assertEquals(str(x), "A B C")

    def test_remove_from_tail(self):
        '''Remove D from the end of A-B-C-D'''
        a, b, c, d = create_nodes()
        x = DLList.of(a, b, c, d).remove(d)
        self.assertEquals(str(x), "A B C")

    def test_remove_only_item(self):
        '''Remove D when it's the only element'''
        a, b, c, d = create_nodes()
        x = DLList.of(d)
        self.assertEquals(str(x), "D")
        x = x.remove(d)
        self.assertEquals(str(x), "Empty")
        self.assertEquals(len(list(x)), 0)
