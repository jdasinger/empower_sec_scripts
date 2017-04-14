

def if_divisable_by_three(lst):
	# return_array = []
	# for num in lst:
	# 	if num % 3 == 0:
	# 		return_array.append(num)
	# return return_array

	return [num for num in lst if num % 3 == 0]

def if_element_length_is_7_or_more(lst):
	# return_array = []
	# for element in lst:
	# 	if len(element) >= 7:
	# 		return_array.append(element)
	# return return_array

	return [element for element in lst if len(element) >= 7]

def unpack_list_of_list(lst):
	# return_array = []
	# for lists in lst:
	# 	for element in lists:
	# 		return_array.append(element)
	# return return_array

	return [element for lists in lst for element in lists]



def if_key_in_dictionary(dct, lst):
	# return_array = []
	# for color in lst:
	# 	for key, value in dct.items():
	# 		if key == color:
	# 			return_array.append(color)
	# return return_array	

	return [color for color in lst for key,value in dct.items() if key == color]








