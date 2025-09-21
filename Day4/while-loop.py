# while loops

#coins = 5

# while coins > 0:
    #print(f'I have {coins} coins')
    #coins = coins - 1

####################

#while coins > 0:
    #print(f'I have {coins} coins')
    #coins -= 1

#else:
    #yprint("I have no money anymore")


####################

#answer = 'y'

#while answer == 'y':
    #answer = input('Do you want to continue? (y/n)')

#else:
    #print('Thank you')


####################

#answer = 'y'
#while answer == 'y':
    #pass

#print('Hello')

####################

#name = input('Whats your name?')

#for letter in name:
    #if letter == 'i':
        #break
    #print(letter)

####################

name = input('Whats your name?')

for letter in name:
    if letter == 'i':
        continue
    print(letter)


####################


number = 50

# While the number is greater or equal to 0
while number >= 0:
    # Check if the number is divisible by 5
    if number % 5 == 0:
        print(number)   # Show the number if divisible by 5
    # Subtract 1 each loop to avoid infinite loop
    number -= 1

####################

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for number in list_numbers:
    if number < 0:
        break
    print(number)