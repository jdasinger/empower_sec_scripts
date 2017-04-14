# the menu of bill's taco shack is going to start changing rapidly
# therefore the code associated with it needs to be refactored to accomodate a rapidly changing menu
# also prices are going to start being changed on a daily basis, and because of that, we want to pass
#prices when we initialize the customer object


import unittest
from customer_refactored import CustomerRefactored

class TestCustomerRefactored(unittest.TestCase):

	def test_init(self):
		test_customer = CustomerRefactored("bill shelton", 15, {"taco": 2,"burrito": 8, "enchilladas": 6})

		self.assertEqual(test_customer.cash_available, 15)
		self.assertEqual(test_customer.prices, {"taco": 2,"burrito": 8, "enchilladas": 6})
		self.assertEqual(test_customer.food, {})

	def test_calculate_purchase_amount(self):
		order = {
			"taco": 5,
			"burrito": 3,
			"enchilladas": 2
		}
		test_customer = CustomerRefactored("bill shelton", 150, {"taco": 2,"burrito": 8, "enchilladas": 6})
		cost = test_customer.calculate_purchase_amount(order)
		self.assertEqual(cost, 46)

	# def test_purchase_food(self):
	# 	order = {
	# 		"taco": 5,
	# 		"burrito": 3,
	# 		"enchilladas": 2
	# 	}
	# 	test_customer = CustomerRefactored("bill shelton", 150, {"taco": 2,"burrito": 8, "enchilladas": 6})
	# 	test_customer.purchase_food(order)
	# 	self.assertEqual(test_customer.cash_available, 104)
	# 	self.assertEqual(test_customer.food, order)

	# def test_eat_food(self):
	# 	order = {
	# 		"taco": 7,
	# 		"burrito": 4,
	# 		"enchilladas": 2
	# 	}
	# 	test_customer = CustomerRefactored("bill shelton", 150, {"taco": 2,"burrito": 8, "enchilladas": 6})
	# 	test_customer.purchase_food(order)
	# 	food_eaten = {
	# 		"taco": 2,
	# 		"burrito": 1,
	# 		"enchilladas": 1
	# 	}
	# 	test_customer.eat_food(food_eaten)
	# 	self.assertEqual(test_customer.food, {
	# 			"taco": 5,
	# 			"burrito": 3,
	# 			"enchilladas": 1
	# 		})		


if __name__ == '__main__':
	unittest.main()