import random


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
                print(possible_factor)
