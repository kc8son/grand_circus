####################################################################################################
#
#   Date Written: 03/06/2023        By: Joseph P. Merten
#   Day 4 - extra challenge
#   https://docs.google.com/document/d/167KLhqFAsxP_cERHREmoIgPUKIdXChdbeY59iRPf81E/preview
#
####################################################################################################
#   imports
import math

####################################################################################################
#   variables

####################################################################################################
#   functions
def  get_area_circle(radius):
    """"Takes a radius parameter. It calculates and returns the area of a circle with that radius."""
    return math.pi * radius ** 2

def get_circumference(radius):
    """"Calculates and returns the circumference of a circle with that radius."""
    return 2.0 * radius * math.pi

def get_area_square(side):
    """Calculates and returns the area of a square with that side length."""
    return side ** 2

def get_area_triangle(base, height):
    """Calculates and returns the area of a triangle with that base and height.
    For this function, create default values of 1.0 for both base and height."""
    return base * height / 2.0




####################################################################################################
#   Main routine
#   Call each of these functions and print the result to the console.
#   (NOTE: None of these functions should use print within them.
#   Instead, they must return the calculated value.)
print("Area - Circle", get_area_circle(1))
print("Circumference - Circle", get_circumference(1))
print("Area - Square", get_area_square(4))
print("Area - Triangle", get_area_triangle(5, 10))
