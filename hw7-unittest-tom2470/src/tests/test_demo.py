from ..llist import LList

import unittest

def some_LList_nodes():
    a = LList.Node("A")
    b = LList.Node("B")
    return a, b

class TestLList(unittest.TestCase):

    def test_instance(self):
        '''Create an instance'''
        a, b = some_LList_nodes()
        x = LList.of(a, b)
        self.assertEquals(x.printme(), "A B")
    
    
