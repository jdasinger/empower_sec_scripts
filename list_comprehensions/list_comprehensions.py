# list comprehensions follow the format
# [dosomething(num) for num in array if some_condition_is_true]


# use a list comprehension to return only even numbers
def even_numbers(array_numbers):
	return[num for num in array_numbers if num % 2 == 0]

	# return array_numbers



# use list comprehension to return words starting with the letter "a"
def start_with_a(array_strings):
	return[letter for letter in array_strings if letter[0] == "a"]

# use list comprehension to multiply by 11 numbers that are divisable by 3
def multiply_by_11_numbers_divisable_by_three(array_numbers):
	modified_array = [num * 11 for num in array_numbers if num % 3 == 0] 
	return modified_array