class DLList:
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.n= None;

    @staticmethod
    def of(*args):
        list = DLList()
        for node in args:
            list.insert(node)
        return list

    def insert(self, node, where = None):
        node.next = where
        prev = None
        next = self.head
        while (next != where):
            prev = next
            next = next.next
        if (prev):
            prev.next = node
        else:
            self.head = node
        if (next==None):
          self.tail= node
        return self

    def remove(self, node):
      prev = None
      next = self.head
      while (next != node):
          prev = next
          next = next.next
      if (prev):
          prev.next = node.next;
      else:
          self.head = node.next;
      if(next.next==None):
        self.tail=prev;
      node.next = None
      return self

    def printme(self):
        s = "Empty"
        next = None
        if self.head is not None:
            s = self.head.value
            next = self.head.next
        while next is not None:
            node = next
            next = node.next
            s += " " + node.value
        return s
        
    def __str__(self):
        s = "Empty"
        next = None
        if self.head is not None:
            s = self.head.value
            next = self.head.next
        while next is not None:
            node = next
            next = node.next
            s += " " + node.value
        return f'{s}'
       #return f'{self.head}'

    

    def __iter__(self):
        self.n = self.head
        return self

    def __next__(self):
      if self.n:
        result = self.n
        self.n=self.n.next
        return result
      else:
        raise StopIteration
        
      
            
    def __list__(self):
          l = [self.head.value]
          next = None
          if self.head is not None:
              next = self.head.next
          while next is not None:
              node = next
              next = node.next
              l.append(node.value)
          return l   
      


    class Node():
        def __init__(self, value):
            self.previous= None
            self.value = value
            self.next = None
        def __str__(self):
          return f'{self.value}'