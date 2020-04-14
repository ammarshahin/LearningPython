secret_word = "Giraffe"
guess = ""   # empty string
no_of_guesses = 0

while (guess != secret_word) and (no_of_guesses < 5):
    guess = input("Enter a new guess: ")
    no_of_guesses += 1

print("Congratulations your guess is right!!")
