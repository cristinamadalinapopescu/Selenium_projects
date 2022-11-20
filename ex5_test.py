import unittest
from ex5 import str_to_float, str_to_float_2


class Str_to_float(unittest.TestCase):
    def test1_str_to_float(self):
        var = "1.234.567,89 Lei"
        var1 = str_to_float(var)
        assert var1 == 1234567.89

    def test2_str_to_float(self):
        var = 'abcde.gh,jg Lei'
        var1 = str_to_float_2(var)

    def test3_str_to_float(self):
        var = '12.334.55677.32,223 Lei'
        var1 = str_to_float(var)
        assert var1 == 123345567732.223


if __name__ == '__main__':
    unittest.main()
