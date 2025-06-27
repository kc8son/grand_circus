####################################################################################################
#
#   Date Written: 03/15/2023        By: Joseph P. Merten
#   SHOPPING LIST  https://docs.google.com/document/d/1e0yQY40vEe_hl-2cksXmAFQSzxh8sHb_XWjpADHqmws/preview
#
####################################################################################################
#   imports
import pdb
import sys

####################################################################################################
#   Variables
menu_dict = {
    "Tomatoes":     2.50,
    "Bread":        1.25,
    "Mushrooms":    5.79,
    "Cereal":       1.89,
    "Butter":       3.15,
    "Eggs":         2.10,
    "Lettuce":      1.35
}
order_dict = {}

####################################################################################################
#   functions
def print_menu():
    i = 1
    print("Today's menu:\nPlease make a selection or type 'checkout'")
    for key in menu_dict.keys():
        print(f"{i} - {key} - ${menu_dict[key]:.2f}")
        i += 1

def get_selection():
    resonse = input("> ")
    #   Test 1 - check for numeric entry
    if resonse.isnumeric():
        iresponse = int(resonse)
        if 0 < iresponse <= len(menu_dict):
            if menu_dict[iresponse] in order_dict:
                order_dict[menu_dict[iresponse]] += 1
            else:
                order_dict[menu_dict[iresponse]] = 1

    print(x)
    #   Test 2 - scan for the full name
    #   Test 3 - scan for partial name.

####################################################################################################
#   lambdas

###################################################################################################
#   Main routine.
print_menu()
get_selection()