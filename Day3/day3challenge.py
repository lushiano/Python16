# ask text
fulltext = input("Insert your text: ")
fulltextlower = fulltext.lower()

# ask letters
letters = input("Select 3 letters: ")
lettersdict = list(letters)

# 1. count letters
firstletter = lettersdict[0]
secondletter = lettersdict[1]
thirdletter = lettersdict[2]

countfirstletter = str(fulltextlower.count(firstletter))
countsecondletter = str(fulltextlower.count(secondletter))
countthirdletter = str(fulltextlower.count(thirdletter))

print("The first letter appears " + countfirstletter + " times.")
print("The second letter appears " + countsecondletter + " times.")
print("The third letter appears " + countthirdletter + " times.")


# 2. count all the words
fulltextwords = fulltextlower.split()
fulltextwords = list(fulltextwords)

print("The full text has " + str(len(fulltextwords)) + " words.")


# 3. first and last letter
print("The first letter of the text is " + str(fulltext[0]) + " and the last one is " + str(fulltext[-1]))

# 4. inverted order

listfulltext = list(fulltext)
listfulltext.reverse()
reversedtext = "".join(listfulltext)

print(reversedtext)

# 5. check if python is in the text

findpyton = "Python" in fulltext
print("Python is in the text? " + str(findpyton))