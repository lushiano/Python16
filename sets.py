my_set = set([1,2,3,4,5])

print(type(my_set))
print(my_set)

my_set = set({1,2,3,4,5})

print(type(my_set))
print(my_set)

my_set = set((1,2,3,4,5))

print(type(my_set))
print(my_set)

other_set = {1,2,3,(4,5,6)} # accepts tuples but not dict or lists

print(type(other_set))

print(len(other_set)) # lenght
print(2 in other_set) # find value

# set joining

s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1.union(s2)
print(s3)

# add element

s4 = {1,2,3}
s4.add(4)

print(s4)

# delete

s5 = {1,2,3}
s5.remove(3)

print(s5)

# discard

s6 = {1,2,3}
s6.discard(6)

print(s6)

# pop

s7 = {1,2,3}
s7.pop()

print(s7)

draw = s7.pop() # store random deleted element
print(s7)

# clear

s8 = {1,2,3}
s8.clear()

print(s8)