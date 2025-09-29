name = input("Tell me your name ")

print(f"Ok {name} let's begin!")
print("Guess the number between a an 100, you only have 8 opportunities.")

number = input("What number do you think it is? ")
number = int(number)

correct_answer = 25

tries = 8 

if number == correct_answer:
    print("You won!")

if number < 1 or number >= 100:
    print("You're out of play")

if number < correct_answer and number >= 1:
    print ("Is greater than that")

if number > correct_answer and number <= 99:
    print("Is lower than that")