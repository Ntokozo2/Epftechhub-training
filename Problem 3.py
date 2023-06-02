def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def largestPrimeFactor(n):
    prime = 2
    while n > 1:
        while n % prime == 0:
            n /= prime
        if n == 1:
            break
        while True:
            prime += 1
            if isPrime(prime):
                break
    return prime

print(largestPrimeFactor(600851475143))