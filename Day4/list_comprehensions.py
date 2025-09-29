word = 'python'
my_list= []

for letter in word:
    my_list.append(letter)
print(my_list)

#################

my_list2 = [letter for letter in word]
print(my_list2)

#################

my_list3 = [x for x in "antartida"]
print(my_list3)

#################

my_list4 = [number for number in range(1,100,5)]
print(my_list4)

#################

my_list5 = [n/2 for n in range(1,21,2)]
print(my_list5)

#################

my_list6 = [na if na * 2 > 10 else 'no' for na in range(0,21,2)]
print(my_list6)

#################

feet = [10,20,30,40,50]
meters = [f * 0.3048 for f in feet]

print(meters)