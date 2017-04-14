# the menu of bill's taco shack is going to start changing rapidly
# therefore the code associated with it needs to be refactored to accomodate a rapidly changing menu
# also prices are going to start being changed on a daily basis, and because of that, we want to pass
#prices when we initialize the customer object


class CustomerRefactored(object):

	def __init__(self, name, cash_available, prices, food={}):
		self.name = name
		# assign cash_available to a variable of customer called cash_available
		self.cash_available = cash_available
		# assign prices to a variable of customer named prices
		self.prices = prices
		# assign food to a variable of custmer named food
		self.food = food


	def calculate_purchase_amount(self, order):
	# 	#the order object is a dictionary, with food types and amounts
	# 	# {
	# 	# 	"burritos": 1,
	# 	# 	"tacos": 3,
	# 	# 	"enchiladas" 1
	# 	# }
	# 	# this function uses self.prices to calculate the cost of all the food in an order
	# 	# and then returns that amount
# loop through order, look up price in self.prices, multiplying order by self.prices
		total_amount = 0
		for key, value in order.items():
			total_amount += self.prices[key] * value
		return total_amount



	# def purchase_food(self, order):
	# 	# use calculate_purchase_amount to calculate the cost of food
	# 	# remove the purchase price of food from self.cash_available
	# 	# add food ordered to the self.food variable


	# def eat_food(self, food_eaten):
	# 	#remove from self.food the food in the food_eaten object 
