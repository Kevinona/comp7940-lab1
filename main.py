def main():
	print("Hello World")
	# Ex 1
	# Find the all factors of x using a loop and the operator %.
	x = 52633
	for i in range(x+1):
		if x % i == 0:
			print(i)

# Ex 2
def print_factors(x):
	# Find the all factors of x using a loop and the operator %.
	for i in range(x+1):
		if x % i == 0:
			print(i)

# Ex 3
def factors_in_list(x):
	# Find the all factors of x using a loop and the operator %.
	l = [52633, 8137, 1024, 999]
	for i in l:
		if x % i == 0:
			print(i)

if __name__ == '__main__':
	main()
	print_factors(52633)
	factors_in_list(52633)
