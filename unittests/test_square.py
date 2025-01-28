from square import square_preceding
import unittest

class TestSquarePreceding(unittest.TestCase):
    def test_empty_list(self):
        values = []
        square_preceding(values)
        self.assertEqual(values, [])
    
    def test_range_of_values(self):
        values = [1, 2, 3]
        self.assertEqual(values, [1, 2, 3])
    
    def test_value_is_to_power_of_preceding_value(self):
        values = [2, 3, 4]
        self.assertEqual(values, [2, 3, 4])

if __name__ == '__main__':
    unittest.main()