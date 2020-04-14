secret_word = "Giraffe"
guess = ""   # empty string
no_of_guesses = 0
max_no_guesses = (5)  # A tuple to store a constant value

while (guess != secret_word) and (no_of_guesses < max_no_guesses):
    guess = input("Enter a new guess: ")
    no_of_guesses += 1

if no_of_guesses == max_no_guesses:
    print("Wrong... your guess is wrong..")
else:
    print("Congratulations your guess is right!!")
