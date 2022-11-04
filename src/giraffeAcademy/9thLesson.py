# ************* Lesson 9 **************
# ************* Dictionaries **************

# Dictionaries is a data structure in python that store information in key value pairs
# In Python the word is the "Key" and the definition is the "Value"
# Note : No duplicate keys are allowed(unique)

##### ex: A program that converts Jan >> January , Feb >> February , etc #####
# Dictionary Name = {
# List of keys: the associated values
# }
monthConversions = {
    "Jan": "January",      # Jan is the Key >> January is the value
    "Feb": "February",
    "Mar": "March",
}
print(monthConversions["Jan"]) # this method may cause an error if the key doesn't exist

# get is useful as it makes a default key to the dictionary and returns it when an invalid key is entered instead of error
print(monthConversions.get("Feb"))
# ex: luv is not a valid key so it will return an "none" as default
print(monthConversions.get("luv"))
# here we sat "Not a valid key" to be the default instead of "none"
print(monthConversions.get("luv", "Not a valid key"))
