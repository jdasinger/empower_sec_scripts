# python is an object oriented language
# objects have attributes (data) and methods
# objects are instances of classes

class Customer(object):

	def __init__(self, name, cash_available, number_of_tacos=0, number_of_burritos=0):
		self.name = name
		# assign cash_available to a variable of customer called cash_available
		self.cash_available = cash_available
		# assign number_of_tacos to a variable of customer called number_of_tacos
		self.number_of_tacos = number_of_tacos
		# assign number_of_burritos to a variable of custmer called number_of_burritos
		self.number_of_burritos = number_of_burritos

	def purchase_tacos(self, number_tacos_purchased):
	# 	#in this function increase number_of_tacos by the amount
		self.number_of_tacos = self.number_of_tacos + number_tacos_purchased
	# 	#decrease available cash by 1.5 * amount
		self.cash_available -= number_tacos_purchased * 1.5


	def eat_tacos(self, number_tacos_eaten):
	# 	#subtract the number of tacos eaten from self.number_of_tacos
		self.number_of_tacos -= number_tacos_eaten
	def purchase_burritos(self, number_burritos_purchased):
	# 	#in this function increase number_of_burritos by the amount
		self.number_of_burritos += number_burritos_purchased 
	# 	#decrease available cash by 7 * amount		
		self.cash_available -= 7 * number_burritos_purchased
	def eat_burritos(self, number_burritos_eaten):
	# 	#subtract the number of burritos eaten from self.number_of_tacos
		self.number_of_burritos -= number_burritos_eaten




