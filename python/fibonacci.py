def fibonacci(pos):
	if pos <= 1:
		return 1
	else:
		return fibonacci(pos - 1) + fibonacci(pos - 2)

print fibonacci(10)