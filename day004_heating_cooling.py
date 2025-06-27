####################################################################################################
#
#   Date Written: 03/06/2023        By: Joseph P. Merten
#   Day 4 - Heating & Cooling
#   Thanks Chitra for the direction about having an additional function.
#
####################################################################################################
#   imports

####################################################################################################
#   variables
#actual_tmp = 93     # Test 1 - Run AC
actual_tmp = 55    # Test 2 - run the furnace
desired_tmp = 71
window = 2
default_run_time = 3

####################################################################################################
#   functions
def run_furnace(run_time, actual_temp):
    """This function will run the furnace for the specified number of minutes to raise the temperature"""
    print(f"Running furnace for {run_time} minutes")    # Uses global variable...
    return actual_temp + 3                              # Uses local/passed variable...

def run_ac(run_time, actual_temp):
    """This function will run the ac for the specified number of minutes to lower the temperature"""
    print(f"Running ac for {run_time} minutes")         # Uses global variable...
    return actual_temp - 3                              # Uses local/passed variable...

def run_standby():
    """This function will run neither the ac nor the furnace for the specified number of minutes to maintain the temperature"""
    print("Within our comfort window - standing by...")

def Check_temp(actual_temp, desired_temp):
    """Check the actual vs desired temp and run the appropriate function to heat or cool or standby."""
    print(f"Current temp = {actual_temp}, desired temp = {desired_temp}")
    if actual_temp < desired_temp - window:
        actual_temp = run_furnace(default_run_time, actual_temp)
    elif actual_temp > desired_temp + window:
        actual_temp = run_ac(default_run_time, actual_temp)
    else:
        run_standby()
    print(f"Current temp = {actual_temp}, desired temp = {desired_temp}")
    print("-"*100)
    return actual_temp

def temp_convert(temp, unit):
    match unit.upper():
        case 'C':
            return temp
        case 'K':
            return temp+273.15
        case 'F':
            return temp*9/5 + 32

        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return "Something's wrong."


####################################################################################################
#   main routine
#   We want to allow a window as specified in the window variable.  This will
#   define our comfort window.  I.E. the number of degrees above or below our desired_temp
#   before we start the heat or ac.  I arbitrarily chose to run the function 9 times.
#   In real life, this loop would run in an endless loop. ;-)
for i in range(9):
    actual_tmp = Check_temp(actual_tmp, desired_tmp)

####################################################################################################
#   Extended Challenge - test the conversion function a few times...
#   Have to upgrade python to version 3.10 to use case  statement...
print("Freezing - Celcius:", temp_convert(0, 'c'))
print("Freezing - Farenheit:", temp_convert(0, 'f'))
print("Freezing - Kelvin:", temp_convert(0, 'k'))
print("Invalid unit test:", temp_convert(0, 'x'))

print("Boiling - Celcius:", temp_convert(100, 'c'))
print("Boiling - Farenheit:", temp_convert(100, 'f'))
print("Boiling - Kelvin:", temp_convert(100, 'k'))
print("Invalid unit test:", temp_convert(100, 'x'))
