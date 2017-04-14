import unittest
from underscore import *

class TestUnderscore(unittest.TestCase):

	def test_map(self):

		def multiply_2(num):
			return num * 2

		reindeer = [3, 4, 5, 6, 7]
		res = p_map(multiply_2, reindeer)

		self.assertEqual(res, [6, 8, 10, 12, 14])

		def multiply_3(num):
			return num * 3

		input_list = [3, 4, 5, 6, 7]
		res = p_map(multiply_3, input_list)

		self.assertEqual(res, [9, 12, 15, 18, 21])

	def test_filter(self):
	    def start_with_a(word):
	    	if word[0] == "a":
	    		return True 
	    	return False

	    input_list = ["artichoke", "orangatang", "kiwi", "orange"]
	    res = p_filter(start_with_a, input_list)

	    self.assertEqual(res, ["artichoke"])

	    def contains_a(word):
	    	if "a" in word:
	    		return True
	    	return False

	    input_list = ["artichoke", "orangatang", "kiwi", "orange"]
	    res = p_filter(contains_a, input_list)

	    self.assertEqual(res, ["artichoke", "orangatang", "orange"])

	def test_any(self):
		def greater_than_10(number):
			if number > 10:
				return True
			return False

		input_list = [8, 5, 9, 11]
		res = p_any(greater_than_10, input_list)
		self.assertEqual(res, True)

		input_list = [8, 5, 9, 3]
		res = p_any(greater_than_10, input_list)
		self.assertEqual(res, False)

	def test_every(self):
		def greater_than_10(number):
			if number > 10:
				return True
			return False

		input_list = [11, 15, 19, 21]
		res = p_every(greater_than_10, input_list)
		self.assertEqual(res, True)

		input_list = [11, 15, 19, 3]
		res = p_every(greater_than_10, input_list)
		self.assertEqual(res, False)

	def test_contains(self):
		input_list = [3, 4, 5, 6]
		res = p_contains(input_list, 6)
		self.assertEqual(res, True)

		input_list = [3, 4, 5, 6]
		res = p_contains(input_list, 11)
		self.assertEqual(res, False)


	def test_reduce(self):

		def summer(num_1, num_2):
			return num_1 + num_2

		input_list = [8, 5, 9, 11]
		res = p_reduce(summer, input_list, 0)
		self.assertEqual(res, 33)

		def subtractor(num_1, num_2):
			return num_1 - num_2

		input_list = [8, 5, 9, 11]
		res = p_reduce(subtractor, input_list, 78)
		self.assertEqual(res, 45)



if __name__ == '__main__':
    unittest.main()