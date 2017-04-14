import unittest
from for_and_if import *


class TestForAndIf(unittest.TestCase):

	def test_if_divisable_by_three(self):
		result = if_divisable_by_three([1, 2, 4, 5, 6, 7, 8, 9])

		self.assertEqual(result, [6, 9])

		result = if_divisable_by_three([1, 2, 4, 5, 7, 8])
		self.assertEqual(result, [])

	def test_if_element_length_is_7_or_more(self):
		result = if_element_length_is_7_or_more(["acrobat", "apple", "ace", "artichoke", "akamai", "astronaut", "arizona", "anarchy"])
		self.assertEqual(result, ['acrobat', 'artichoke', 'astronaut', 'arizona', 'anarchy'])

		result = if_element_length_is_7_or_more([[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3]])
		self.assertEqual(result, [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7]])

	def test_unpack_list_of_list(self):

		result = unpack_list_of_list([["a", "b", "c", "d", "e"], ["f", "g", "h", "i", "j"], ["k", "l", "m", "n", "o"], ["p", "q", "r", "s", "t"], ["u", "v", "w", "x", "y"], ["z"]])
		self.assertEqual(result, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

		result = unpack_list_of_list([
								[1, 2, 3, 4, 5],
								[6, 7, 8, 9, 10],
								[11, 12, 13, 14, 15]
							 ])
		self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

	def test_if_key_in_dictionary(self):

		#test case 1

		test_dct = {
			"blue": "ocean",
			"green": "tree",
			"grey": "rock",
			"purple": "flower"
		}

		test_lst = ["blue", "yellow", "purple", "violet"]

		result = if_key_in_dictionary(test_dct, test_lst)
		self.assertEqual(result, ["blue", "purple"])

		#test case 2

		test_dct = {
			"salty": "chips",
			"sweet": "candy",
			"bitter": "dandelion",
			"sour": "lemon"
		}

		test_lst = ["umami", "salty"]

		result = if_key_in_dictionary(test_dct, test_lst)
		self.assertEqual(result, ["salty"])

if __name__ == '__main__':
	unittest.main()
