import random
factor_list = []
'''
factor_list = []
composite_factors = []
max_factor = round(600851475143/2)
for possible_factor in range(1, max_factor):   # find factors of 600851475143
    if 600851475143 % possible_factor == 0:
        factor_list.append(possible_factor)
for possible_prime_factor in factor_list:
    prime_max_factor = round(possible_prime_factor/2)
    for subfactor in range(2, prime_max_factor):
        if possible_prime_factor % subfactor == 0:
            composite_factors.append(possible_prime_factor)
for incorrect_factor in composite_factors:
    if incorrect_factor in factor_list:
        factor_list.remove(incorrect_factor)
factor_list.sort()
print(factor_list[-1])
'''


def is_prime(n, k):
    if (n % 10) in [0, 2, 4, 5, 6, 8]:
        return False
    else:
        for i in range(0, k+1):
            a = random.randint(2, n-2)
            if a**(n-1) % n != 1:
                return False
    return True


if __name__ == '__main__':
    for possible_factor in range(4, 600851475143):
        if is_prime(possible_factor, 10):
            if 600851475143 % possible_factor == 0:
                factor_list.append(possible_factor)
                print(possible_factor)
