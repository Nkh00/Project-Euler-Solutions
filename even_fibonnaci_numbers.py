finalval = 0

fibonnaci_numbers = [1, 2]

while fibonnaci_numbers[-1] < 4000000:
    fibonnaci_numbers.append(fibonnaci_numbers[-1] + fibonnaci_numbers[-2])


for i in fibonnaci_numbers:
    if i % 2 == 0:
        finalval += i

print(finalval)
