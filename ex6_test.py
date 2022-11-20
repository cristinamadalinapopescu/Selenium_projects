import unittest
from ex6 import solutie


class FirstDegreeEcuation(unittest.TestCase):
    def test1_solutie(self):
        a = 3
        b = 15
        x = solutie(a, b)
        assert x == -5

    def test2_solutie(self):
        a = 2
        b = 4
        x = solutie(a, b)
        assert x == -2


if __name__ == '__main__':
    unittest.main()
