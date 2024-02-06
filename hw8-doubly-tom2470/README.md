# hw-doubly

## Test
type the code below to execute test_dllist.py
```
make test
```
This code runs test multiple test. The first test testing the of function. Second test empty list on node head and tails. The third test test iteration over listing the elements.Fourth test inserting a node. Fifth test appending a node to the end. Sixth test test inserting a node at the start. Seventh test inserts a node in a empty list. Eighth test test the remove function. Ninth through eleventh test test removing items.The expected output is below
```
python -B run_tests.py
test_append (src.tests.test_dllist.TestDLList)
Start with A-B-C and insert D at the end ... ok
test_empty (src.tests.test_dllist.TestDLList)
Create an empty list (head and tail are None) ... ok
test_getitem (src.tests.test_dllist.TestDLList)
Get individual nodes in the list ... ok
test_insert (src.tests.test_dllist.TestDLList)
Start with A-B-C and insert D before C ... ok
test_insert_at_start (src.tests.test_dllist.TestDLList)
Start with A-B-C and insert D at the beginning ... ok
test_insert_into_empty (src.tests.test_dllist.TestDLList)
Insert into an empty list ... ok
test_instance (src.tests.test_dllist.TestDLList)
Create a list ... ok
test_remove (src.tests.test_dllist.TestDLList)
Remove D from middle of A-B-D-C ... ok
test_remove_from_head (src.tests.test_dllist.TestDLList)
Remove D from the head of D-A-B-C ... ok
test_remove_from_tail (src.tests.test_dllist.TestDLList)
Remove D from the end of A-B-C-D ... ok
test_remove_only_item (src.tests.test_dllist.TestDLList)
Remove D when it's the only element ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.000s

OK
```
## Demo
type the code below to execute test_demo.py
```
make demo
```
This code extensively test iteration, head and tail attributes of the doubled linked list. The result should be as shown below.
```
python -B run_demo.py
test_head (src.tests.test_demo.TestLList) ... ok
test_iter (src.tests.test_demo.TestLList) ... ok
test_tail (src.tests.test_demo.TestLList) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
