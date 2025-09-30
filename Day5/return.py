def multiply(number1,number2):

    total = number1 * number2

    print(total)
    return total

a = 100
b = 200

result = multiply(a,b)
print(result)

####

def reverse_word(word):
    # Use reversed() and join the characters
    return "".join(reversed(word)).upper()

word = "Python"
print(reverse_word(word))  # Output: NOHTYP