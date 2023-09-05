from math import sqrt, ceil

def smallest_prime_factor(n):
	if n % 2 == 0:
		return 2

	for factor in range(3, int(ceil(sqrt(n)))):
		if n % factor == 0:
			return factor

	return int(n)

def factors(n):
	out = []
	while n != 1:
		smallest = smallest_prime_factor(n)
		n /= smallest
		out.append(smallest)
	return out

print(max(factors(600851475143)))
