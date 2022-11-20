import unittest
from area_circle import aria_cercului


class Aria_cercului(unittest.TestCase):
    def test1_aria_cercului(self):
        pi = 3.14

    r = 2
    aria = aria_cercului(r)
    assert aria == 12.56

    def test2_aria_cercului(self):
        pi = 3.14

        r = 50
        aria = aria_cercului(r)
        assert aria == 7850

    def test3_aria_cercului(self):
        pi = 3.14

        r = 400
        aria = aria_cercului(r)
        assert aria == 502400


if __name__ == '__main__':
    unittest.main()
