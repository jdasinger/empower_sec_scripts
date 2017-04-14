import unittest
from list_comprehensions import *


class TestNumbers(unittest.TestCase):

	def test_even_numbers(self):
		result = even_numbers([1, 2, 4, 5, 7, 8])
		self.assertEqual(result, [2, 4, 8])

	def test_start_with_a(self):
		result = start_with_a(["apple", "orange", "carrot"])
		self.assertEqual(result, ["apple"])

	def test_multiply_by_11_numbers_divisable_by_three(self):
		result = multiply_by_11_numbers_divisable_by_three([1, 2, 4, 9, 7, 12])
		self.assertEqual(result, [99, 132])

if __name__ == '__main__':
	unittest.main()