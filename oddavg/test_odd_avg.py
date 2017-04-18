import unittest
from odd_avg import odd_average

class TestOddAvg(unittest.TestCase):

    def test_odd_avg_function_one_odd_number(self):
        list1 = [3]
        self.assertEqual(odd_average(list1), 3)

    def test_odd_avg_function_one_even_number(self):
        list1 = [4]
        self.assertEqual(odd_average(list1), 'No odd numbers in the list')

    def test_odd_avg_function_zero(self):
        list1 = [0]
        self.assertEqual(odd_average(list1), 'No odd numbers in the list')

    def test_odd_avg_function_more_numbers_unsorted(self):
        list1 = [2, 6, 1, 3, 5, 4]
        self.assertEqual(odd_average(list1), 3)

    def test_odd_avg_function_neg_numbers(self):
        list1 = [1, 2, -3, -4, -5, 6, -1]
        self.assertEqual(odd_average(list1), -2)

if __name__ == '__main__':
    unittest.main()
