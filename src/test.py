import unittest
from hello_function import hello

class HelloTestCase(unittest.TestCase):
   def test_hello(self):
        result = hello("миша")
        self.assertEqual(result, "Привет, Миша.")

if __name__ == '__main__':
    unittest.main() 