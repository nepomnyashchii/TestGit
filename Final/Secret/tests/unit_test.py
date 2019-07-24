import unittest

# https://realpython.com/python-testing/#choosing-a-test-runner


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
        # self.assertEqual(fun(3), 3)
