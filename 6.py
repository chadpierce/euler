#sum of squares 1^2 + 2^2.....= 385
#square of the sum (1+2....)^2 = 3025

one_thru_hundred = list(range(1,101))
#max = 101
#sum_of_squares = 0
#square_of_sum = 0

sum_of_squares = sum(i**2 for i in one_thru_hundred)
#for i in range(1,max):
#    sum_of_squares += i**2

square_of_sums = sum(one_thru_hundred)**2
#for i in range(1,max):
#    square_of_sum += i
#square_of_sum = square_of_sum**2

print("sum of squares:",sum_of_squares)
print("square of sums:",square_of_sums)
print("difference:",square_of_sums - sum_of_squares)
