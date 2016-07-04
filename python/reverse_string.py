def reverse_string(string, reverse_string):
	if string == "":
		print reverse_string
	else:
		first = string[0]
		reversed_string = first + reverse_string
		string = string[1:]
		print string
		print reversed_string
		reverse_string(string, reversed_string)
reverse_string("jason", "")
