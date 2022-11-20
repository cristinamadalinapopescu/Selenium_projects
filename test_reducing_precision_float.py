import unittest
from reducing_precision_float import un_float


class Un_float(unittest.TestCase):
    def test1_un_float(self):
        f = 45.87422
        floatul = un_float(f)
        assert floatul == 45.87

    def test2_un_float(self):
        f = 345.4356
        floatul = un_float(f)
        assert floatul == 345.44

    def test3_un_float(self):
        f = 1.8901
        floatul = un_float(f)
        assert floatul == 1.89

    def test4_un_float(self):
        f = 0.756897654
        floatul = un_float(f)
        assert floatul == 0.76


if __name__ == '__main__':
    unittest.main()
