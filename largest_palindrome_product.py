possible_numbers = []

for x in reversed(range(100, 999)):
    for y in reversed(range(100, 999)):
        if str(x * y) == str(x * y)[::-1]:
            possible_numbers.append(x*y)

print(max(possible_numbers))
