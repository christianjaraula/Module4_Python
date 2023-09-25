import unittest

def check(x):
    return x>=100

class TestMultiply(unittest.TestCase):
    def test(self):
        self.assertTrue( check(69))
if __name__== '__main__':
    unittest.main()