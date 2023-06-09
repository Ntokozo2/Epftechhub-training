def largestPrimeFactor(number):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number
print(int(largestPrimeFactor(600851475143)))