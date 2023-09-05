from math import sqrt, floor


for c in range(1, 1001):
	d = c**2 + 2000 * c - 1_000_000

	if d < 0:
		continue
	
	a = (-c - sqrt(d) + 1000) / 2
	b = (-c + sqrt(d) + 1000) / 2

	if a == floor(a) and b == floor(b):
		print(f"{a}**2 + {b}**2 = {c},  product ({a * b * c})")
