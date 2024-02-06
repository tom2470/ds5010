## hw-unittest assignment


* Read the documentation of [unitttest](https://docs.python.org/3/library/unittest.html) to see how it works.
  * Pay special attention to the [Basic Example](https://docs.python.org/3/library/unittest.html#basic-example)
  * Make sure that you understand it and that you can run it yourself.
* Then practice creating some tests as follows...
  * [Linked List](https://observablehq.com/@mbostock/linked-lists) implements a linked list algorithm in JavaScript.
  * The file `src/app.py` demonstrates a Python version of that linked-list algorithm, which is in `src/llist.py`.
  * The file `src/tests/test_demo.py` uses unittest to implement one unittest of the algorithm in `src/llist.py`.
  * And `make demo` runs that test using the unittest framework
  * Assignment: 
    * Create a new branch
    * In that branch, add the file `src/test/test_llist.py` by first making a copy of `src/test/test_demo.py`
    * Then add 5 additional tests to `test_llist.py` to verify the following
    * If you start a linked list containing with 3 nodes `a, b, c` that have labels "A", "B", "C", then...
    * (1) the `listme()` method can be used to get the first node in the linked list,
    * (2) if node d has label "D", then `.insert(d)` returns "A B C D"
    * (3) if node d has label "D", then `.insert(d, c)` returns "A B D C"
    * (4) if node d has label "D", then `.insert(d, a)` return "D A B C"
    * (5) `.remove(b)` returns "A C"
  * Finally: add `src/test/test_llist.py` to your repo from a branch with a pull request
  * Leave that pull request for your instructor to merge into the main branch.
* Your implementation should produce the following output:
```
$ make test
python -B run_tests.py
test_append (src.tests.test_llist.TestLList)
Start with A-B-C and insert D at the end ... ok
test_getitem (src.tests.test_llist.TestLList)
Get one of the nodes in the list ... ok
test_insert (src.tests.test_llist.TestLList)
Start with A-B-C and insert D before C ... ok
test_insert_at_start (src.tests.test_llist.TestLList)
Start with A-B-C and insert D at the beginning ... ok
test_instance (src.tests.test_llist.TestLList)
Create an instance ... ok
test_remove (src.tests.test_llist.TestLList)
Remove B from middle of A-B-C ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

## Best practices

* [Good practice for `__init.py__`](https://stackoverflow.com/questions/448271/what-is-init-py-for)
* [Naming & where to put unittests](https://stackoverflow.com/questions/61151/where-do-the-python-unit-tests-go)
* `./solution` has unit tests that follow the style of Kylie Bemis's Python "Containers" repo.

## References

* [Linked List](https://observablehq.com/@mbostock/linked-lists) -- mbostock notebook
* [Graphviz](https://observablehq.com/@observablehq/dot) -- mbostock notebook
* [Containers](https://github.com/kuwisdelu/containers) by Kylie Bemis -- github

## JavaScript references

Each of these MDN references can be found by googling two words -- "javascript" and the relevant keyword

* [Defining classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)
* [new operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)

## Recall from 5001...

* **Linked List**
  * A linked list is a "linear" collection of elements whose order is not related to their physical location in memory
  * It is a data structure consisting of a collection of "nodes" which together represent a "sequence"
  * Each node contains data and a "reference" (i.e., a "link") to the next node in the sequence.
  * The structure allows efficient insertion and removal of elements during iteration for any position in the sequence.
  * Benefit:
    * unlike arrays, element insertion and removal doesn't require reallocation or reorganization of the entire structure
  * Drawbacks: 
    * access time is linear
    * random access is not possible
    * arrays have better "cache locality"
  * [Linked List](https://en.wikipedia.org/wiki/Linked_list) -- wikipedia
* **Array**
  * a data structure consisting of a collection of elements identified by at least one array index or key
  * each elements position can be computed from its index "tuple" by a mathematical formula
  * the simplest type of array is a linear (i.e, one-dimensional) array
  * [Array Data Structure](https://en.wikipedia.org/wiki/Array_data_structure) -- wikipedia
