from functools import lru_cache


def next_collatz(n):
	if n % 2 == 0:
		return n // 2
	else:
		return 3 * n + 1


@lru_cache(maxsize=1024)
def sequence_len(n):
	if n == 1:
		return 1

	return 1 + sequence_len(next_collatz(n))


n = 0
best = 0
for i in range(1_000_000, 1, -1):
	len = sequence_len(i)
	if len > best:
		n = i
		best = len

print(n, best)
