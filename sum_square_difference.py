sum_of_squares = 0
square_of_sum = 0
for i in range(1, 101):
    square_of_sum += i
    sum_of_squares += i**2
print((square_of_sum)**2 - sum_of_squares)
