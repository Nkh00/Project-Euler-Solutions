result_found = False
possible_value = 46190
factors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

while not result_found:
    if all(possible_value % i == 0 for i in factors):
        result_found = True
        print(possible_value)
    else:
        possible_value += 2
