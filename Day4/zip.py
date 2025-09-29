names = ['Hanna','Bruce','Tony']
ages = [65,29,42]
cities = ['NY','Berlin','London']

combination = list(zip(names,ages,cities))

for name,age,city in combination:
    print(f'{name} is {age} years old, and lives in {city}')