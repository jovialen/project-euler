from functools import lru_cache


@lru_cache(maxsize=128)
def num_paths(endx, endy):
	num = 1 if endx == 0 and endy == 0 else 0

	if endx > 0:
		num += num_paths(endx - 1, endy)
	if endy > 0:
		num += num_paths(endx, endy - 1)

	return num


print("Num paths through 2x2 grid:", num_paths(2, 2))
print("Num paths through 20x20 grid:", num_paths(20, 20))
