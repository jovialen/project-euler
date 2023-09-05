def is_palindrome(x):
	return str(x) == str(x)[::-1]

palindromes = [];
for i in range(1000):
	for j in range(i + 1):
		prod = i * j
		if is_palindrome(prod):
			palindromes.append(prod)

print(max(palindromes))
