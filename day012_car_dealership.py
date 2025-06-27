####################################################################################################
#
#   Date Written: 03/23/2023        By: Joseph P. Merten
#   Day 12: Car Dealership
#   Python OOP: Inheritance
#   Objectives: Inheritance, Parent Classes, Derived Classes
#
#   Date Modified: 04/24/2023       By: Joseph P. Merten
#   Removed some debugging code.
#
####################################################################################################
#   imports
import pdb
import sys
import math

####################################################################################################
#   Classes
class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False
    def engine_on(self):
        self.engine_on = True
        print("Starting engine")
    def make_noise(self):
        print("Beep beep!")


class Truck(Vehicle):
    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
        self.cargo = False
    def load_cargo(self):
        print("Loading the truck bed")
        self.cargo = True


class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        Vehicle.__init__(self, make, miles, price)
        self.top_speed = top_speed
    def make_noise(self):
        print("Vroom vroom!")


class Validator:
    def validate_tb():
        """This method will validate that user inputs 't' for truck or 'b' fo bike."""
        my_resp = 'x'
        while my_resp != 'b' and my_resp != 't':
            my_resp = input("Would you like to review bikes or trucks (b/t)?\n> ").lower()
            if my_resp != 'b' and my_resp != 't':
                print("Invalid response, please enter 'b' or 't'...")
        return my_resp

    def validate_int(my_prompt, min, max):
        """This method will display a message and validate that the response is an
        integer within the boundaries specified by min & max"""
        my_resp = min - 5   #force untrue...
        while not min <= my_resp <= max:
            print(my_prompt)
            my_resp = input()
            try:
                my_resp = int(my_resp)
            except:
                my_resp = min - 5
            if not min <= my_resp <= max:
                print("Invalid entry, please try again...")
        return my_resp

    def validate_yn(my_prompt):
        "This METHOD determines if we want to grow the circle larger."
        my_resp = 'x'
        while my_resp != 'n' and my_resp != 'y':
            my_resp = input(my_prompt)
            if my_resp != 'n' and my_resp != 'y':
                print("Invalid response, please enter 'y' or 'n'...")
        return my_resp

    def validate_int(my_prompt, min, max):
        """This method will display a message and validate that the response is an
        integer within the boundaries specified by min & max"""
        while True:
            my_resp = input(my_prompt)
            if my_resp.isnumeric():
                if min<=int(my_resp)<=max:
                    return int(my_resp)
            print(f"Invalid response...  Expecting an integer between {min} and {max}, please try again...")


####################################################################################################
#   Variables
compare_flag = 'l' # initial value = l for list
vehicles_to_compare = []
truck_list = [
    Truck("Toyota", 100000, 55000.00),
    Truck("Chevy", 110000, 44000.00),
    Truck("Mercedes", 120000, 155000.00),
    Truck("Hyundai", 130000, 5000.00)
]
bike_list = [
    Motorcycle("Honda", 1000, 5500.00, 300000), # Speed of light per second...
    Motorcycle("Suzuki", 1100, 4400.00, 343), # speed of sound at sea level
    Motorcycle("Indian", 1200, 15500.00, 1400),
    Motorcycle("Kawasaki", 1000, 500.00, 3187)
]


####################################################################################################
#   Functions
def add_vehicle_to_compare(my_vehicle_list):
    """This function asks the use which vehicle to add to the compare list and removes it from the source list."""
    my_resp = Validator.validate_int(f"Which vehicle would you like to add to the compare? (1-{len(my_vehicle_list)})\n> ", 1, len(my_vehicle_list))
    # print(my_vehicle_list[my_resp-1])
    vehicles_to_compare.append(my_vehicle_list[my_resp-1])
    del my_vehicle_list[my_resp-1]
    # print("-"*80)
    # print(my_vehicle_list)
    # print(vehicles_to_compare)
    # print("-"*80)


def buy_vehicle():
    print("Which vehicle would you like to purchase?")
    print_vehicles(vehicles_to_compare)


def print_vehicles(my_vehicle_list):
    """This function will print a vehicle lisy.  It automatically decides if the list is
    for bikes or trucks based upon the existence of the 'top_speed' value and sets the
    format string appropriately.  I may move this to a method in the vehicle class..."""
    i = 1
    for my_vehicle in my_vehicle_list:
        if hasattr(my_vehicle, 'top_speed'):    # If the top_speed attribute exists, these are motorcycles...
            f_string = f"{i}: {my_vehicle.make}: with {my_vehicle.miles:,.0f} miles and a top speed od {my_vehicle.top_speed:,.0f} costs ${my_vehicle.price:,.2f}"
        else:
            f_string = f"{i}: {my_vehicle.make}: with {my_vehicle.miles:,.0f} miles costs ${my_vehicle.price:,.2f}"
        print(f_string)
        i += 1


def get_compare(my_vehicle_list, compare_flag):
    if compare_flag == 'y': # We already have a first vehicle to compare...
        add_vehicle_to_compare(my_vehicle_list)
        return 'y'
    else:
        compare_flag = Validator.validate_yn("Would you like to compare one of these vehicles toady? (y/n)\n> ").lower()
        if compare_flag == 'n':
            return 'n'
        else:
            add_vehicle_to_compare(my_vehicle_list)
            return 'y'
    # # Testing...
    # print("---=== truck_list ===---")
    # print(truck_list)
    # print("---=== bike_list ===---")
    # print(vehicles_to_compare)
    # print("---=== bike_list ===---")
    # print(bike_list)


def do_compare():
    """This function does the comparison from vehicles_to_compare."""
    print("Hre are your vehicles to compare:")
    for vehicle in vehicles_to_compare:
        print(f"\t- {vehicle.make}: with {vehicle.miles:,.0f} costs ${vehicle.price:,.2f}")
        vehicle.make_noise()

####################################################################################################
#   Lambdas

####################################################################################################
#   Main code
print("Hello\nWelcome to GC bikes & trucks!")
#   List trucks or bikes...
choice = Validator.validate_tb()
if choice == 't':
    comp_list = truck_list
    print_vehicles(truck_list)
elif choice == 'b':
    comp_list = bike_list
    print_vehicles(bike_list)
    #   Does the user want a comparison?
compare_flag = get_compare(comp_list, compare_flag).lower()
if compare_flag == 'y':
    #   They want a comparison - bike or truck?
    choice = Validator.validate_tb()
    if choice == 't':
        comp_list = truck_list
        print_vehicles(truck_list)
    elif choice == 'b':
        comp_list = bike_list
        print_vehicles(bike_list)
    compare_flag = get_compare(comp_list, compare_flag).lower()
    do_compare()
print("Thank you for visiing GC bikes & trucks!")




# if compare_flag == y:
#     pass
# else:
#     choice = Validator.validate_num("Would you like to buy this vehicle?\n> ", 1, len(vehicles_to_compare))
#     print("Thanks for your purchase...")