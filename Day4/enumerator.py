my_list = ['a','b','c']
index = 0

for item in my_list:
    print(index,item)
    index += 1

#########

my_list = ['a','b','c']

for index,item in enumerate(my_list):
    print(index,item)

#########

for index,item in enumerate(range(50,55)):
    print(index,item)

#########

mytuples = list(enumerate(my_list))
print(mytuples)

mytuples = list(enumerate(my_list))
print(mytuples[2][0])


list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

# loop through the list with enumerate
for index, name in enumerate(list_names):
    print(f"{name} is found at index {index}")


# string to enumerate
text = "Python"

# create the list of tuples (index, element)
indices_list = list(enumerate(text))

print(indices_list)