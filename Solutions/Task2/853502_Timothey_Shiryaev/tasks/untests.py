import unittest
from vecmod import Vector
from decorator import *
from fpythtojson import to_json
import filecmp

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('---Creation---')

    def test_fib(self):
        f = fibonacci(5)
        print('\n\n---Test fibonacci---')
        print(f)
        self.assertEqual(f, 5)

    def test_failfib(self):
        f = fibonacci(5)
        print('\n\n---Test fibonacci---')
        print(f)
        self.assertEqual(f, 4)

    def test_addvec(self):
        obj = Vector([12, -5], [13, 8])
        print('\n\n---Test vector + vector---')
        self.assertEqual(obj.sumVec(), [25, 3] )

    def test_failaddvec(self):
        obj = Vector([12, -5], [13, 8])
        print('\n\n---Test vector + vector---')
        self.assertEqual(obj.sumVec(), [207, 2] )

    def test_failtojson(self):
        print('\n\n---Test to_json---')
        self.assertEqual(to_json({"name": "John", "age": 30}), 456)

    def test_successtojson(self):
        print('\n\n---Test to_json---')
        self.assertEqual(to_json(456), '456')

    def test_mergesort(self):
        print('\n\n---Test merge-sort\'а---')
        self.assertEqual(filecmp.cmp('out.txt', 'outtest.txt'), True)

    def test_failmergesort(self):
        print('\n\n---Test merge-sort\'а---')
        self.assertEqual(filecmp.cmp('numbers.txt', 'outtest.txt'), True)


if __name__ == '__main__':
    unittest.main()
