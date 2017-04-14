# filter, map and reduce are built in python functions
# filter enables you to extract all elements of a list that pass a truth test
# map applies a function to every element of a list
# reduce applies a function to a list, returning a specific value


import unittest
from filter_map import *


class TestNumbers(unittest.TestCase):

	def test_doubled_list(self):
		result = doubled_list([1, 2, 4, 5, 7, 8])
		self.assertEqual(result, [2, 4, 8, 10, 14, 16])

	#def test_strip_a_from_word(self):
		# result = strip_a_from_word("apple")
		# self.assertEqual(result, "pple")

		# result = strip_a_from_word("pineapple")
		# self.assertEqual(result, "pinepple")

		# result = strip_a_from_word("lemon")
		# self.assertEqual(result, "lemon")

	# def test_split_sentence_remove_a(self):
	# 	result = split_sentence_remove_a("I really like to eat apples while jumping on artichokes.")
	# 	self.assertEqual(result, ['I', 'relly', 'like', 'to', 'et', 'pples', 'while', 'jumping', 'on', 'rtichokes.'])

	# def test_filter_divisable_by_five(self):
	# 	result = filter_divisable_by_five([1, 5, 10, 11, 15, 42])
	# 	self.assertEqual(result, [5, 10, 15])

	# def test_contains_ing(self):
	# 	result = contains_ing("beginning")
	# 	self.assertEqual(result, True)

	# 	result = contains_ing("end")
	# 	self.assertEqual(result, False)

	# def test_filter_contains_ing(self):
	# 	result = filter_contains_ing("Bling bling makes we want to sing")
	# 	self.assertEqual(result, ['Bling', 'bling', 'sing'])


if __name__ == '__main__':
	unittest.main()
