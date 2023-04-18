import unittest
from city_functions import format_city


class CitiesTestCase(unittest.TestCase):
    def test_format_city(self):
        self.assertEqual(format_city('santiago', 'chile'), 'Santiago, Chile')

    def test_format_city_population(self):
        self.assertEqual(format_city('Santiago', 'Chile', 123),
                         'Santiago, Chile - population 123')


if __name__ == '__main__':
    unittest.main()
