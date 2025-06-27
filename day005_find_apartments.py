####################################################################################################
#
#   Date Written: 03/08/2023        By: Joseph P. Merten
#   Find an Apartment Functions - Default & Named Params, Lambdas
#
####################################################################################################
#   imports
import pdb

####################################################################################################
#   Variables

####################################################################################################
#   functions
def apt_search1(city, max_rent, min_beds, pets_allowed):
    """This function returns a string message returning the search criteria in plain language."""
    my_str = f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments{pet_test(pets_allowed)}, all within a budget of ${max_rent} per month..."
    return(my_str)

def apt_search2(city, max_rent, min_beds=2, pets_allowed=False):
    """This is the same function, except that it has default values for min_beds and pets_allowed."""""
    my_str = f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments{pet_test(pets_allowed)}, all within a budget of ${max_rent} per month..."
    return(my_str)

####################################################################################################
#   lambdas
plus_one_hundred = lambda x: x+100      # Write a lambda function that adds 100 to any given number
square_num = lambda x: x**2             # Write a lambda function that squares any given number
concatenate = lambda x: "-"+x           # Write a lambda function that concatenates “- “ before any string
divide_by_three = lambda x: x/3.0       # Write a lambda function that divides any number by 3
pet_test = lambda x: " that allow pets" if x else ""

####################################################################################################
#   Main routine.
print("---===*** Part 1 - functions ***===---")
print(apt_search1(city="Grand Forks", max_rent=300, min_beds=1, pets_allowed=False))
print(apt_search1("Minneapolis", max_rent=800, min_beds=2, pets_allowed=True))

print("\n---===*** Part 2 - named & default parameters 2 ***===---")
print(apt_search2(city="Seattle", max_rent=300))                # Call this function once with arguments for min_beds and pets_allowed both omitted.
print(apt_search2(city="Dallas", max_rent=800, min_beds=3))    # Then call it with just min_beds and no pets_allowed
print(apt_search2(city="Detroit", max_rent=500, pets_allowed=True)) # Now call it with just pets_allowed and not min_beds (You’ll want to use named arguments for this one).

print("\n---===*** Part 3 - lambdas ***===---")
# tests should look like this:
print(plus_one_hundred(30))  # 130
print(square_num(4))  # 16
print(concatenate('hello'))  # - hello
print(divide_by_three(9))  # 3.0

print(help(apt_search1))