"""
Your module description
"""
myString="This is a string"
print(myString)
print(type(myString))

print(myString + " is of the data type "+ str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("what is your name? ")
print(name)

color = input("what is your favourite color? ")
animal = input("what is your favorite animal ")

print("{1}, you like a {0} {2}!".format(color, name, animal))