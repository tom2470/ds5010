from llist import LList

def some_LList_nodes():
    a = LList.Node("A")
    b = LList.Node("B")
    return a, b

# Create some nodes and an associated 
a, b = some_LList_nodes()
x = LList.of(a, b)

print(x.printme())
