dic = {'key1':100,'key2':500}

a = dic.popitem()

print(a)
print(dic)

#####

test = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"
b=test.lstrip(",:%_#")
print(b)

#####

fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
fruits.insert(4,"orange")

#####

phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

isolated_sets = phone_brands.isdisjoint((tv_brands))