list = [1, 2]

while True:
	fib = list[-1] + list[-2]
	if fib < 4_000_000:
		list.append(fib)
	else:
		break

print(sum(filter(lambda v: v % 2 == 0, list)))
