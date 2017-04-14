#don't worry to much about edge cases, worry about passing the tests

import re

# write a function that returns True or False
# based on whether a pattern exists in an input string
def identify_match(input_str, pattern):
	if re.search(pattern, input_str):
		return True
	else:
		return False

# write an a function that scans a text string
# and returns an array of all dates that follow the following format;
# month day, example June 4 or November 11
#don't worry about potential false positives like Hamburger 7, or Artichoke 45
#def identify_dates(input_str):



# write a function that looks for the pattern of a social security number
# 345-54-3455
# if it finds it, it swaps it with XXX-XX-XXXX
#def swap_social(input_str):




#write a function that looks for the pattern associated with a VISA credit card number
# swap it with the following pattern XXXX XXXX XXXX XXXX
#def swap_credit_card(input_str):

