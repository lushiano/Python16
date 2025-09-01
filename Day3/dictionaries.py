my_dictionary = {'c1':'value1','c2':'value2'}
print(my_dictionary)

result = my_dictionary['c1']
print(result)

customer = {'name':'John','last_name':'Lennon','weight':88,'height':1.80}

query1 = (customer['last_name'])
print(query1)

query2 = (customer['weight'])
print(query2)

dic = {1:55,2:[10,20,30],3:{'s1':100,'s2':200}}
print(dic[2][1])
print(dic[3]['s2'])

dic2 = {'k1':['a','b','c'],'k2':['d','e','f']}
print(dic2['k1'][2].upper())

dic3 = {1:'a',2:'b'}
print(dic3)

dic3[3] = 'c'
print(dic3)

dic3[2] = 'B'
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())

my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
print(my_dict['points']['points2'][1]) #Use dictionary indices to extract the second item of points2