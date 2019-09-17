import math


def prime_sieve(sieve_size):
    # returns list of primes using sieve of eratosthenes
    sieve = [True] * sieve_size
    sieve[0] = False  # zero and one are not primes
    sieve[1] = False

    # create the sieve
    # print("THIS:", int(math.sqrt(sieve_size)))
    for i in range(2, int(math.sqrt(sieve_size)) + 1):
        pointer = i * 2
        while pointer < sieve_size:
            sieve[pointer] = False
            pointer += i

    # compile list of primes
    primes = []
    for i in range(sieve_size):
        if sieve[i]:
            primes.append(i)

    return primes


p = prime_sieve(1000000)
print(p[10000])

# print(prime_sieve(10001))


