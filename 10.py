# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

x = 2
for num in range(3, 2000000, 2):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        x += num
print(x)
