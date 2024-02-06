import unittest

# import test modules

from src.tests import test_demo

# initialize test suite

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite

suite.addTest(loader.loadTestsFromModule(test_demo))

# initialize a test runner and run the test suite

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
