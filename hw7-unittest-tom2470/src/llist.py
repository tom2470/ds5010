class LList:
    def __init__(self):
        self.head = None;

    @staticmethod
    def of(*args):
        list = LList()
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

    def listme(self):
        l = [self.head]
        next = None
        if self.head is not None:
            next = self.head.next
        while next is not None:
            node = next
            next = node.next
            l.append(node)
        return l

    class Node():
        def __init__(self, value):
            self.value = value
            self.next = None
