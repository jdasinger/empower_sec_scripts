import unittest
import re
from regular_expressions import *


class TestRegularExpressions(unittest.TestCase):

	def test_find_match(self):
		result = identify_match("cats like to wear hats", "hats")
		self.assertEqual(result, True)

		result = identify_match("cats like to wear hats", "fish")
		self.assertEqual(result, False)

	def test_identify_dates(self):
		result = identify_dates("On August 11 I will ride to Arlington, on November 15 I will write a poem")
		self.assertEqual(result, ['August 11', 'November 15'])

	def test_swap_social(self):
		result = swap_social("bill shelton registered with SSN 546-87-1234")
		self.assertEqual(result, "bill shelton registered with SSN XXX-XX-XXXX")

	def test_swap_credit_card(self):
		result = swap_credit_card("the customer purchased a sweater with 5500-0000-0000-0004")
		self.assertEqual(result, "the customer purchased a sweater with XXXX XXXX XXXX XXXX")


if __name__ == '__main__':
	unittest.main()