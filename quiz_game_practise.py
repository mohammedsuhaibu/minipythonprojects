print("Welcome to my mini quiz game (anything goes)!")
print("The rules are: \n" "1. The answer will always be one word \n" 
      "2. cheating allowed" )

user_input = input("Would you like to play? \n")

if user_input.lower() != "yes":
    quit()
    
print("Let's play :)")
score = 0 

answer = input("What is the scientific name for the fear of long words? \n")
if answer.lower() == "hippopotomonstrosesquippedaliophobia":
    print("correct!")
    score += 1  
else:
    print("incorrect!")

answer = input("What is the name of the only mammal capable of sustained flight? \n")
if answer.lower() == "bat":
    print("correct!")
    score += 1  
else:
    print("incorrect!")

answer = input("If two's company and three's a crowd, what are four and five? \n")
if answer.lower() == "nine":
    print("correct!")
    score += 1  
else:
    print("incorrect!")

answer = input("What is the sound of one hand clapping? \n")
if answer.lower() == "silence":
    print("correct!")
    score += 1  
else:
    print("incorrect!")

answer = input("What do you call a bear with no ears? \n")
if answer.lower() == "b":
    print("correct!")
    score += 1  
else:
    print("incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%")