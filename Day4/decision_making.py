# if
# elif
# else

###############

if 10 > 9:
    print("It is correct")

else:
    print("It is not correct")

###############

x = True

if x:
    print("X it is correct")

###############

if 5 == 2:
    print("IT IS CORRECT")

elif 4>3:
    print("4 IS GREATER THAN 3")

else:
    print("IT IS NOT CORRECT")

###############

pet = "rabbit"

if pet == "cat":
    print("You have a cat")

elif pet == "dog":
    print("You have a dog")

elif pet == "fish":
    print("You have a fish")

elif pet == "spider":
    print("You have a spider")

else:
    print("I don't know what animal you have")

###############

age = 16
school_grade = 9

if age < 18:
    print("You are a minor")
    
    if school_grade >= 7:
        print("Passed")
    
    else:
        print("Failed")

else:
    print("You are an adult")


########

speak_french = True
knows_python = False

if speak_french == True and knows_python == True:
    print("You meet the requirements to apply")

elif speak_french == False:
    print("To apply, you need to speak French")
        
elif knows_python == False:
    print("To apply, you need to know how to program in Python")

else:
    print("To apply, you need to know how to program in Python and speak French")