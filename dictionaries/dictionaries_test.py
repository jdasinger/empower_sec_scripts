import unittest
from dictionaries import * 

class TestDictionaries(unittest.TestCase):

	def test_construct_dictionary(self):
		dictionary_list = [
							{"name": "Rick Garcia"},
							{"nickname": "Rickopotomus"},
							{"favorite_snack": "Thai food"},
						  ]
		result = construct_dictionary(dictionary_list)
		self.assertEqual(result, {"name": "Rick Garcia", "nickname": "Rickopotomus", "favorite_snack": "Thai food"})

	def test_unpack_dictionary(self):
		packed_dictionary = {
								"name": "Steve Van Woerkom",
								"nickname": "Steezey Steve",
								"favorite_snack": "burrito"
							}
		result = unpack_dictionary(packed_dictionary)
		self.assertEqual(result, [{'nickname': 'Steezey Steve'}, {'name': 'Steve Van Woerkom'}, {'favorite_snack': 'burrito'}])

	def test_lookup_values(self):
		clothes_color = {
							"jacket": "green",
							"pants": "purple",
							"shirt": "green",
							"hat": "red"
					    }

		clothes_price = {
							"jacket": 100,
							"long_sleeve_shirt": 40,
							"insulated_coat": 150,
							"pants": 70,
							"colored_shirt": 40,
							"shirt": 30,
							"bow_tie": 20,
							"hat": 15
					    }

		result = lookup_values(clothes_color, clothes_price)
		self.assertEqual(result, [100, 15, 30, 70])

	def test_lookup_values_by_color(self):
		clothes_color = {
							"jacket": "green",
							"pants": "purple",
							"shirt": "green",
							"hat": "red"
					    }

		clothes_price = {
							"jacket": 100,
							"long_sleeve_shirt": 40,
							"insulated_coat": 150,
							"pants": 70,
							"colored_shirt": 40,
							"shirt": 30,
							"bow_tie": 20,
							"hat": 15
					    }

		result = lookup_values_by_color(clothes_color, clothes_price, "green")
		self.assertEqual(result, [100, 30])


if __name__ == '__main__':
	unittest.main()