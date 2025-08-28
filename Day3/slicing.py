text = "ABCDEFGHIJKLM"
fragment = text[2]
print(fragment)

fragment = text[2:5]
print(fragment)

fragment = text[2:]
print(fragment)

fragment = text[:5]
print(fragment)

fragment = text[2:10:2] #skips selects every x number
print(fragment)

fragment = text[::3]
print(fragment)

fragment = text[::-1]
print(fragment)

fragment = text[::-2]
print(fragment)

sentence = "Controlling complexity is the essence of programming"
print(sentence[0:11])

sentence = "Never trust a computer you can't throw out a window"
print(sentence[8::3])