# and
# or
# not 

my_bool = 4 < 5 and 5 == 2+3
print(my_bool)

my_bool = (55 == 55) and ("dog" == "dog")
print(my_bool)

my_bool = 10 == 10 or 3 == 2
print(my_bool)

text = "This sentence is short"
my_bool = ("sentence" in text) or ("python" in text)
print(my_bool)

my_bool = not "a" == "b"
print(my_bool)

print("\n")

sentence = "When something is important enough, you do it even if the odds are against you"

word1 = "success"
word2 = "technology"

my_bool = not word1 == sentence and not word2 == sentence
print(my_bool)