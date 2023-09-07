from math import sqrt


def primes_to(n):
    primes = [2]

    for i in range(3, n, 2):
        prime = True

        for x in range(3, int(sqrt(i)) + 1, 2):
            if i % x == 0:
                prime = False
                break

        if prime:
            primes.append(i)

    return primes


print(sum(primes_to(2_000_000)))
# print(sum(primes_to(10)))
