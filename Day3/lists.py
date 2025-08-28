my_list = ["a","b","c"]
print(type(my_list))

another_list = ["hello",55,6.1]
print(type(another_list))

result = len(my_list)
print(result)

result = my_list[0]
print(result)

result = my_list[0:2]
print(result)

result = my_list[0:]
print(result)

my_list2 = ["d","e","f"]
print(my_list+ my_list2)

## concatenate
my_list3 = my_list + my_list2
print(my_list3)

## replace
my_list3[0]="alpha"
print(my_list3)

## append
my_list3.append("g")
print(my_list3)

#pop
my_list3.pop(0) # last element or specify
print(my_list3)

deleted = my_list3.pop(0) # last element or specify
print(deleted)

#sort
list1 = ["g","o","b","m","c"]
list1.sort()
print(list1)

list1 = ["g","o","b","m","c"]
list1.reverse()
print(list1)

list2 = list1
print(list2)