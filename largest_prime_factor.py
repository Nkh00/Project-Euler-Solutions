factor_list = []
composite_factors = []
status_val = 0
max_factor = round(600851475143/2)
for possible_factor in range(1, max_factor):   # find factors of 600851475143
    if 600851475143 % possible_factor == 0:
        factor_list.append(possible_factor)
        status_val += 1
        print(status_val)
for possible_prime_factor in factor_list:
    prime_max_factor = round(possible_prime_factor/2)
    for subfactor in range(2, prime_max_factor):
        if possible_prime_factor % subfactor == 0:
            status_val += 1
            print(status_val)
            composite_factors.append(possible_prime_factor)
for incorrect_factor in composite_factors:
    if incorrect_factor in factor_list:
        factor_list.remove(incorrect_factor)
factor_list.sort()
print(factor_list[-1])
