
"""
Fibonacci number generator
When given a position, the function returns the fibonacci at that position in the sequence.
The zeroth number in the fibonacci sequence is 0. The first number is 1
Negative numbers should return None
"""
def fibonacci(position):
	if position < 0:
		return None
	elif position == 0:
		return 0
	elif position == 1:
		return 1
	else:
<<<<<<< HEAD
		return fibonacci(position - 1) + fibonacci(position - 2)
=======
        return fibonacci(position - 1) + fibonacci(position - 2)
#hello



>>>>>>> e49754a51cc9961db6cd056162a5e95cc4f6e6ac

