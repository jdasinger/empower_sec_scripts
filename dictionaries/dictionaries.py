# dictionaries are a powerful and flexible python data structure



# this function will take a list of dictionaries
# each of these dictionaries will have one key value pair
# instantiate a dictionary that will be returned from the function
# copy each key value pair from the list of dictionaries to the newly instantiated dictionary
# input: [{"name": "billy"}, {"hometown", "Salt Lake City"}, {"eye_color", "blue"}]
# output: {"name": "billy", "hometown": "Salt Lake City", "eye_color": "blue"}
def construct_dictionary(dictionary_list):
	return_dict = {}
	for dictionary in dictionary_list:
		for key,value in dictionary.items():
			return_dict[key] = value
	return return_dict
		# for key in dictionary:
		# 	return_dict[key] = dictionary[key]


# this function is the opposite of the above function
# we will take in a dictionary, and unpack it into a list
# of key value pairs
def unpack_dictionary(packed_dictionary):
	return_val = []
	for key,value in packed_dictionary.items():
			return_val.append({key:value})
	return return_val


# in this function we will pass in two dictionaries
# we will look up the keys associated with the first dictionary in the second dictionary
# we will add each value associated with the key in the second dictionary into a list
# we will return the list of values 
def lookup_values(first_dictionary, second_dictionary):
	return_val = []
	for key in first_dictionary:
		return_val.append(second_dictionary[key])
	return return_val




# in this function we will pass in two dictionaries, and a color
# we will look up the keys associated with the first dictionary in the second dictionary
# if the key in the first dictionary has a value matching the value being passed in
# we will add each value associated with the key in the second dictionary into a list
# we will return the list of values 
def lookup_values_by_color(first_dictionary, second_dictionary, color):
	return_val = []
	for key in first_dictionary:
		if first_dictionary[key] == color:
			return_val.append(second_dictionary[key])
	return return_val




	return return_val








