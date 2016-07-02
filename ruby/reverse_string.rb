def reverse_string(str, reverse_string)
	return reverse_string if str == ""
	first = str[0]
	reversed_string = first + reverse_string
	str = str[1..-1]
	reverse_string(str, reversed_string)
end

reverse_string("Jason", "")