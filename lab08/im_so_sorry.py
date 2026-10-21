def sum_of_digits(n):
    if n <= 0:
        return 0
    else:
        return sum_of_digits(n // 10) + (n % 10)

print(sum_of_digits(1234))

