def check_3_digits(number):
    return number in range(100,1000)

sum = 526 + 311
result = check_3_digits(sum)
print(result)

####################

def check_digits(list):

    three_digits_list = []

    for n in list:
        if n in range(100,1000):
            three_digits_list.append(n)
        else:
            pass

    return three_digits_list

result2 = check_digits([555,99,600])
print(result2)