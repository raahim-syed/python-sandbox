secret = "Raahim"
guess = ""
count = 0
level = input("Enter Level: ")

def returnTries(level):
    if level.lower() == "easy":
        return 5
    elif level.lower() == "hard":
        return 2
    
guessLimit = returnTries(level)
print("You have: " + str(guessLimit))

while count < guessLimit and guess != secret:
    guess = input("Enter Guess: ")
    if guess != secret:
        print("Wrong!")
        count += 1
        if count == guessLimit:
            print("Out of guesses!")
    else: print("Correct!")
