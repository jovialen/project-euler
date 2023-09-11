from math import sqrt


def divisors(n):
	count = 0
	for i in range(1, int(sqrt(n))):
		if n % i == 0:
			if n / i == i:
				count += 1
			else:
				count += 2
	return count


def more_divisors_than(n):
	i = 0
	tri = 0
	best = 0
	while True:
		i += 1
		tri += i
		count = divisors(tri)

		if count > best:
			best = count
			progress = min(best / n, 1)
			print(f"[{'*' * round(progress * 20)}{' ' * round((1 - progress) * 20)}] n = {count} for tri = {tri}\r", end = "")
		
		if count > n:
			print()
			break


more_divisors_than(5)
more_divisors_than(500)
