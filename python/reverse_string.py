def reverse_string(string, reversed_string):
	if string == "":
		print reversed_string
	else:
		first = string[0]
		reversed_string = first + reversed_string
		string = string[1:]	
		reverse_string(string, reversed_string)
reverse_string("jason", "")
