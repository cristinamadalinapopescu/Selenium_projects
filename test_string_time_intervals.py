import unittest
from string_time_intervals import interval_orar


class Interval_orar(unittest.TestCase):
    def test1_interval_orar(self):
        start = 13
        final = 20
        a = interval_orar(start, final)
        assert a == ['13:00 - 14:00', '14:00 - 15:00', '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00',
                     '18:00 - 19:00',
                     '19:00 - 20:00']

    def test2_interval_orar(self):
        start = 'aa'
        final = 'bb'
        a = interval_orar(start, final)
        assert a == 'invalid'

    def test3_interval_orar(self):
        start = 00
        final = 3
        a = interval_orar(start, final)
        assert a == ['00:00 - 01:00', '01:00 - 02:00', '02:00 - 03:00']


if __name__ == '__main__':
    unittest.main()
