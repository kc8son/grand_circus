####################################################################################################
#
#   Date Written: 02/27/2023        By: Joseph P. Merten
#   These are the day 1 exercises.
#
####################################################################################################
#   EXERCISE 1.1: Echo String
str1 = input(">>Enter some text: <<")
print(f">>{str1}")
print()

####################################################################################################
#   EXERCISE 1.2: Adding a number to an integer
num1 = int(input(">>Enter a number: <<"))
print(f">>{num1+1}")
print()

####################################################################################################
#   EXERCISE 1.3: Adding a number to a float
num1 = float(input(">>Enter a number: <<"))
print(f">>{num1+0.5}")
print()

####################################################################################################
#   EXERCISE 1.4: Adding Two Floats
num1 = float(input(">>Enter a number: <<"))
num2 = float(input("Enter another number: <<"))
print(f">>The sum is {num1+num2}")
print()

####################################################################################################
#   EXERCISE 1.5: Multiplying Floats
num1 = float(input(">>Enter a number: <<"))
num2 = float(input(">>Enter another number: <<"))
print(f">>The product is {num1*num2}")
print()

####################################################################################################
#   EXERCISE 1.6: Dividing Integers
num1 = int(input(">>Enter a number: <<"))
num2 = int(input(">>Enter another number: <<"))
print(f">>The result is {num1/num2}")
print()

####################################################################################################
#   EXERCISE 1.7: Entering booleans
bool1 = bool(input(">>Enter a boolean: << "))
print(f">>You entered: << {bool1}")
bool1 = not bool1
print(f">>The opposite of what you entered is: {bool1}")