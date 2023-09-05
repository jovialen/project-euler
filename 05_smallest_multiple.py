prod = -1
i = 2520
while prod == -1:
	if all([i % j == 0 for j in range(11, 21)]):
		prod = i
	i += 2520

print(prod)
