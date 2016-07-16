def fibonacci(pos)
	return 1 if pos <= 1
	fibonacci(pos - 1) + fibonacci(pos - 2)
end


p fibonacci(10)