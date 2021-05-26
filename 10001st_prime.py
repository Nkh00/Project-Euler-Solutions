from largest_prime_factor import is_prime

primes_generated = 2
test_number = 5

while primes_generated < 10001:
    if is_prime(test_number, 10):
        primes_generated += 1
        print(10001-primes_generated)
    if primes_generated == 10001:
        print(test_number)
    test_number += 2
