####################################################################################################
#
#   Date Written: 03/13/2023        By: Joseph P. Merten
#   Student Database 2.0 (Lists, Dictionaries, Nested Sequences)
#
# Extended Challenges:
# 1 - Allow the user to select students by inputting their name in addition to
#     allowing them to select by index.
# 2 - Add in validation for the initial menu. Print a message and retry if the user
#     inputs something other than "add", "view", or "quit" - DONE
# 3 - Add in validation for the view menu. If a bad index is given or a name isn't
#     present in the list of dictionaries, print an appropriate error message and retry that question. - DONE
# 4 - Add validation for the hometown/favorite food portion of the view,
#     if you get any other inputs, print an error message and try that question again. - DONE
#
####################################################################################################
#   imports
import pdb
import sys

####################################################################################################
#   Variables
student_list = \
    [
        { "name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow" },
        { "name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza" },
        { "name": "Julia", "hometown": "Houston", "favorite_food": "shrimp" },
        { "name": "Nirmala", "hometown": "Boston", "favorite_food": "McDonalds" },
        { "name": "Jason", "hometown": "Des Moines", "favorite_food": "Burger King" },
        { "name": "Andrew", "hometown": "Spokane", "favorite_food": "Wendy's" },
        { "name": "Steven", "hometown": "Cupertino", "favorite_food": "White Castle" },
        { "name": "Chitra", "hometown": "Rolla", "favorite_food": "Taco Bell" }
    ]

####################################################################################################
#   functions
def list_names(students):
    """This function accepts a list and prints out the first element of each row."""
    while True:
        for i in range(len(students)):
            print(f'{i+1}\t{students[i]["name"]}')
        my_resp = input(f"Which student would you like to learn more about? Enter a number 1-{len(students)} or part of a name: ")
        try:
            student_index = int(my_resp)    # If this fails, search by name in the except clause
            if 1 <= student_index <= len(students):
                ask_further_info2(student_index-1)
                break
            else:   # we have an integer, but it is out of bounds
                print("I'm sorry, but that was an invalid response, please try again...")
        except: # try to search by name
            i = 1
            for student in students:
                if my_resp.lower() in student["name"].lower():
                    ask_further_info2(i-1)
                    return
                i += 1
            print("Name not found... try again...")


def get_new_student():
    """This function will ask the user for the data for a new student.  This data will be returned as a dictionary to the caller."""
    my_dict = {}
    my_name = input("Please input a name for the new student:\n> ")
    my_hometown = input("Next please input their hometown:\n> ")
    my_food = input("Last please input their favorite food\n> ")
    ny_dict = { "name": my_name, "hometown": my_hometown, "favorite_food":  my_food  }
    return ny_dict

def get_operation():
    """This function gets the operation that the user wants to perform.  It also allows the user to enter just the first letter of the operaation."""
    while True:
        my_operation = input("Please select which action you'd like to do: a)dd, v)iew, or q)uit\n> ").lower()
        if my_operation == 'q' or my_operation == 'quit':
            return 'quit'
        elif my_operation == 'v' or my_operation == 'view':
            return 'view'
        elif my_operation == 'a' or my_operation == 'add':
            return 'add'
        else:
            print("Sorry - that's not a valid entry, please try again...")

def ask_further_info2(st_index):
    """This function will either print the hometown or favrite food of the identified student."""
    response = "xxxx"
    st_name = student_list[st_index]["name"]
    while (True):   # break out when we get a valid response...
        if ('hometown'.find(response) >= 0):
            dict_index = 'hometown'
            print(f"{st_name}'s home town is: {student_list[st_index][dict_index]}\n\n")
            break
        elif ('favorite food'.find(response) >= 0):
            dict_index = 'favorite_food'
            print(f"{st_name}'s favorite food is: {student_list[st_index][dict_index]}\n\n")
            break
        else:
            if(response != "xxxx"):
                print("Your entry must be either 'hometowm' or 'favorite food'.  Please try again...")
            response = input(f"Do you want to know about {st_name}'s hometowm or favorite food? ").lower()


####################################################################################################
#   lambdas

####################################################################################################
#   main routine
curr_operation = "xxx"
while curr_operation != "quit":
    curr_operation = get_operation()
    match curr_operation:
        case 'view':
            list_names(student_list)
        case 'add':
            student_list.append(get_new_student())
    # print(curr_operation)