
# p_map takes a function and a list
# it iterates through every element in the list
# and passes it into the function
# the transformed values are stored in a list
# and returned out of the function
def p_map(func, lst):

	return_value = []

	for element in lst:

		transformed = func(element)
		return_value.append(transformed)

	return return_value



# p_filter taks a function and a list
# it iterates through every element in the list
# and passes it into the function
# if the function returns true
# the value is stored in a list
# and returned out of the function
def p_filter(func, lst):

	return_value = []

	for word in lst:
		transformed = func(word)
		if transformed == True:
			return_value.append(word)


	return return_value


# p_any takes a function and a list
# it iterates through every element in the list
# and passes it into a function
# if ANY element returns True
# the function returns True
# if no element returns True
# the function returns False
def p_any(func, lst):

	for element in lst:
		transformed = func(element)
		if transformed == True:
			return True
	return False

# p_every takes a function and a list
# it iterates through every element in the list
# and passes the element into the function
# if EVERY value returns True
# the function returns True
# if ANY value returns False 
# the function returns False
def p_every(func, lst):

	for element in lst:
		transformed = func(element)
		if transformed == False:
			return False
	return True



# p_contains takes a list and a value
# if the value exists in the list
# the function returns True
# if the value does not exist in the list
# the function returns False
def p_contains(lst, value):

	if value in lst:
		#do something down here
		return True
	return False


# p_reduce takes a function, a list and a starting value
# initially the function takes a starting value, and then an element of the list
# the value returned by the function is then passed back into the function, as well as the next value in the list
# until there are no values left in the list
# the last value returned by the function is returned by p_reduce
def p_reduce(func, lst, start_value):

	return_value = start_value

	for element in lst:
		return_value = func(return_value, element)

	return return_value




