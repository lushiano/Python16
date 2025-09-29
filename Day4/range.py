for num in range(20,31,2):
    print(num)

my_list = list(range(1,100))
print(my_list)


# create the accumulator variable
sum_squares = 0

# loop through numbers from 1 to 15 (inclusive)
for num in range(1, 16):
    square = num ** 2      # square of the current number
    sum_squares += square  # accumulate into sum_squares

print(sum_squares)