def power_digit_sum(power):
    return sum([int(d) for d in str(2 ** power)])


print(power_digit_sum(1000))
