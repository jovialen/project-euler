from math import sqrt


def nextPrime(last, primes):
	i = last
	while True:
		i += 1
		if all(map(lambda prime: i % prime != 0, primes)):
			return i


def prime(n):
	primes = [2]
	while len(primes) < 10001:
		next = nextPrime(primes[-1], primes)
		primes.append(next)
	return primes[-1]


print(prime(6))
