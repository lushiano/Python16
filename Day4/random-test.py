from random import *

# integers
my_random = randint(1,50)
print(my_random)

# floats
my_uniform = round(uniform(1,5),1)
print(my_uniform)

# random (fraction of integer)
just_random = random()
print(just_random)

# choice from list
color = ['blue','red','green','yellow']

my_choice = choice(color)
print(my_choice)

# shuffle numbers from list
numbers = list(range(5,50,5)) 
print(numbers)

shuffle(numbers)
print(numbers)