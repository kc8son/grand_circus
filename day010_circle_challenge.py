####################################################################################################
#
#   Date Written: 03/22/2023        By: Joseph P. Merten
#   Day 10: Circle Challenge - Python OOP: Classes
#
#   Date Modified: 03/23/2023       By: Joseph P. Merten
#   Added a validator class for the extended challenge.
#
####################################################################################################
#   imports
import pdb
import sys
import math

####################################################################################################
#   Classes
class Circle():
    def __init__(self, radius):
        self.radius = radius
    def calculate_diameter(self):
        return 2 * self.radius
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    def calculate_area(self):
        return math.pi * self.radius * self.radius
    def grow(self):
        self.radius *= 2
    def get_radius(self):
        return self.radius

class Validator():
    def validate_radius():
        """This METHOD will get a valid decimal number."""
        print("Enter a radius:")
        my_radius = -1.0
        while my_radius < 0.0:
            my_response = input("> ")
            try:
                my_radius = float(my_response)
                if my_radius < 0:
                    print("Please enter a positive value.")
            except:
                print("Invalid entry, please enter a floating point number...")
                my_radius = -1
        return my_radius
    def validate_yn():
        "This METHOD determines if we want to grow the circle larger."
        my_resp = 'x'
        while my_resp != 'n' and my_resp != 'y':
            my_resp = input("Would you like your circle to grow?\n> ")
            if my_resp != 'n' and my_resp != 'y':
                print("Invalid response, please enter 'y' or 'n'...")
        return my_resp

####################################################################################################
#   Variables
grow_flag = 'y'
validated_radius = -1.0

####################################################################################################
#   Functions
def input_radius():
    """This function will get a valid decimal number."""
    print("Enter a radius:")
    my_radius = -1
    while my_radius < 0:
        my_response = input("> ")
        try:
            my_radius = float(my_response)
            if my_radius < 0:
                print("Please enter a positive value.")
        except:
            print("Invaslid entry, please enter a floating point number...")
            my_radius = -1
    return my_radius

def output_values(my_circle):
    """This outputs our calculations for the circle."""
    print(f"Diameter: {my_circle.calculate_diameter()}")
    print(f"Circumference: {my_circle.calculate_circumference()}")
    print(f"Area: {my_circle.calculate_area()}")

def get_grow_flag(my_circle):
    "This determines if we want to grow the circle another unit larger."
    my_resp = 'x'
    while my_resp != 'n' and my_resp != 'y':
        my_resp = input("Would you like your circle to grow?\n> ")
    if my_resp == 'y':
        print("Stand by while your circle magically grows")
        my_circle.grow()
    elif my_resp == "n":
        print(f"The last radius of your circle was: {my_circle.get_radius()}")
        print("Goodbye")
    else:
        print("Something is wrong...")
        return "n"
    return my_resp

####################################################################################################
#   Lambdas

####################################################################################################
#   Main code
print("Welcome to the circle Tester")
# g_circle = Circle(input_radius())
g_circle = Circle(Validator.validate_radius())
while grow_flag.lower() == 'y':
    output_values(g_circle)
    # grow_flag = get_grow_flag(g_circle)
    grow_flag = Validator.validate_yn()
    if grow_flag == 'y':
        print("Stand by while your circle magically grows")
        g_circle.grow()
    else:
        print(f"The last radius of your circle was: {g_circle.get_radius()}")
        print("Goodbye")

