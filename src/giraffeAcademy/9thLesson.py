# ************* Lesson 9 **************
# ************* Dictionaries **************

# Dictionaries is a data structure in python that store information in key value pairs
# In reality Dictionaries has a list of words and every word has a definition associated with it
# In Python the word is the "Key" and the definition is the "Value"
# Note : No duplicate keys are allowed(unique)

##### ex: A program that converts Jan >> January , Feb >> February , etc #####
# Dictionary Name = {
# List of keys: the associated values
# }
monthConvertions = {
    "Jan": "January",      # Jan is the Key >> January is the value
    "Feb": "February",
    "Mar": "March",
}
print(monthConvertions["Jan"])

# get is useful as it makes a defult key to the dictionary and returns it when an invalid key is entered insted of error
print(monthConvertions.get("Feb"))
# ex: luv is not a valid key so it will return an "none" as defult
print(monthConvertions.get("luv"))
# here we sat "Not a valid key" to be the defult insted of "none"
print(monthConvertions.get("luv", "Not a valid key"))
