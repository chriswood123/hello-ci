import unittest
from hello import say_hello

class test_hello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(say_hello('world'), 'Hello world')

if __name__ == '__main__':
    unittest.main()
