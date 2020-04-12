# ************* Lesson 2 **************
# ************* Working With Strings **************

phrase = "Giraffe Academy"
print(phrase)              # print the phrase
print(phrase.lower())      # convert the whole string(object) into lower letters
print(phrase.upper())      # convert the whole string(object) into upper letters
print(phrase.isupper())    # return True or False if the string is entirely upper
print(phrase.upper().isupper())
print(phrase + " " + phrase)  # Cancatenation of two strings
print(len(phrase))           # return the length of the string
print(phrase.index("G")) # return the index of specific substring(G) inside the main string(phrase)
print(phrase.index("Acad")) # return the start index of specific substring(Acad) inside the main string(phrase)
phrase2 = phrase.replace("Giraffe", "Cat") # replace a substring inside the main string with another and return the new modified string
print(phrase2)
