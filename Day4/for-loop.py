# for loops

my_list = ['a','b','c','d']

for letter in my_list:
    print("Letter: " + letter)

############

for letter in my_list:

    letter_number = my_list.index(letter) + 1
    print(f"Letter: {letter_number}: {letter}")

############

names = ['Paul','Laura','Fede','Louis','Julia']

for name in names:
    if name.startswith('L'):
        print(name)

    else:
        print("This name does not begin with 'L'")

############

numbers = [1,2,3,4,5]
my_value = 0

for number in numbers:

    my_value = my_value + number
    print(my_value)

print(my_value)

############

word = "python"

for letter in "word":
    print(letter)

for numb in [1,2,3]:
    print(numb)

for object in [[1,2],[3,4],[5,6]]:
    print(object)

for a,b, in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

############

dic = {'key1':'a','key2':'b','key3':'c'}
for item in dic.items():
    print(item)

dic = {'key1':'a','key2':'b','key3':'c'}
for item in dic.values():
    print(item)

for a,b in dic.items():
    print(a,b)

############

list_numbers = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

# Start with 0
sum_numbers = 0

# Loop through each number and add it to sum_numbers
for num in list_numbers:
    sum_numbers += num

print("The sum of the numbers is:", sum_numbers)


############


list_numbers = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

sum_even = 0  # to store the sum of even numbers
sum_odd = 0   # to store the sum of odd numbers

for num in list_numbers:
    if num % 2 == 0:       # even
        sum_even += num
    else:                  # odd
        sum_odd += num

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)