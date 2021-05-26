from largest_prime_factor import is_prime

primes_generated = 3
test_number = 5

while primes_generated < 10001:
    if is_prime(test_number, 10):
        primes_generated += 1
        print(test_number)
    test_number += 2

print(test_number)
