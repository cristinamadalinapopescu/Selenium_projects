import unittest
from volume_sphere import volumul_sferei


class Volum_sfera(unittest.TestCase):
    def test1_vol_sfera(self):
        pi = 3.14
        r = 4
        volum = volumul_sferei(r)
        assert volum == 803.8399999999999

    def test2_vol_sfera(self):
        pi = 3.14
        r = 5.4
        volum = volumul_sferei(r)
        assert volum == 1977.7478400000002


if __name__ == '__main__':
    unittest.main()
