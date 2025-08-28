text = "We are going to learn six methods today"

result = text.upper()
print(result)

result = text[4].upper()
print(result)

result = text.lower()
print(result)

result = text.split()
print(result)

result = text.split("o")
print(result)

a = "learning"
b = "python"
c = "is"
d = "amazing"
e = "-".join([a,b,c,d])

print(e)

result = text.find("s")
print(result)

result = text.find("q")
print(result)

result = text.replace("to","TO2")
print(result)

word_list = ["Simple","is","better","than","complex."]
a = "Simple"
b = "is"
c = "better"
d = "than"
e = "complex."
f = " ".join([a,b,c,d,e])
print(f)


sentence = "If the implementation is hard to explain, it might be a bad idea."

# Replace words
sentence = sentence.replace("hard", "easy")
sentence = sentence.replace("bad", "good")

print(sentence)