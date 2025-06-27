####################################################################################################
#
#   Date Written: 03/09/2023        By: Joseph P. Merten
#   STUDENT DATABASE
#
#   Date Modified: 03/15/2023 - Bug fixed in name search.
#
# What will the application do?
# 2 Points: Create 3 lists and fill them with student information—one with names values, one with favorite foods values,
#   one with favorite food values. DONE
# 1 Point: Prompt the user to ask about a particular student by number. Convert the input to an integer.
#   Use the integer as the index for the lists. Print the student’s names. DONE
# 1 Point: Ask the user which category to display: Hometown or Favorite food.
#   Then display the relevant information. DONE
# 1 Point: Ask the user if they would like to learn about another student. DONE
#
# Build Specifications:
# 1 Point: Validate user number: Use an if statement to check if the number is out of range,
#   i.e. either less than 1 or greater than the length of the lists.
#   If so, display a friendly message and let the user try again. DONE
# 1 Point: Validate category: Ask the user what information category to display: "favoritefoods" or "Favorite Food".
#   Use an if statement to check that they entered either category names correctly.
#   If they entered an incorrect category, display a friendly message and re-ask the question. (See hints below!) DONE
# 1 Point: List Length: Use the first list’s length property in your code instead of hardcoding it. DONE

# Extended Challenges:
# 1 Point: Provide an option where the user can see a list of all students. DONE
# 2 Points: Allow the user to search by student names (Good challenge but difficult!) DONE
# 1 Point: Category names: Allow uppercase and lowercase; allow portion of
#   word such as "Food" instead of "Favorite Food" DONE
#
####################################################################################################
#   imports
import pdb
import sys

####################################################################################################
#   Variables
names = ["Nirmala", "Jason", "Andrew", "Steven", "Chitra"]
hometowns = ["Boston", "Des Moines", "Spokane", "Cupertino", "Rolla"]
favoritefoods = ["McDonalds", "Burger King", "Wendy's", "White Castle", "Taco Bell"]
db_size = len(names)
check_student = 'y'

####################################################################################################
#   functions
def check_data():
    """This function checks the size of the three lists to ensure they are all the same."""
    if len(names) != len(hometowns) or len(names) != len(favoritefoods):
        print("*" * 50)
        print("*")
        print("*    Fatal internal data error!  ABORT")
        print("*")
        print("*" * 50)
        sys.exit()
    print("Data check passed...")

def get_studentid():
    """This function requests a student id number nutil a valid one is entered."""
    response = 0
    while not (0 < response <= db_size):
        response = int(input(f"Welcome! Which student would you like to learn more about? (enter a number 1-{db_size})\n> "))
        if not (0 < response <= db_size):
            print("I'm sorry, that is not a valid entry, please try again...")
    return response-1

def list_students():
    """This function simply lists all the students.  The program will ask the user again which student number they want."""
    for i in range(db_size):
        print(i+1, names[i])
    return

def name_search():
    """This function will search for a student by name.
    The user will be prompted for part of a name and names matching that string will be returned.
    The user may choose a name listed, or enter an empty string to try searching again.
    The function will return the student id found, or possibly 0 if none are found and the user
    decides not to try another string."""
    response = input("Please enter a partial name to search for: ").lower()
    if not response:
        return 0
    for i in range(db_size):
        if (names[i].find(response) >= 0):
            print(i+1, names[i])
            return i+1
    return 'n'

def get_studentid2():
    """This function is an enhancement of get_studentid().  This implements two enhaancements:
    1 - Provide an option where the user can see a list of all students.
    2 - Allow the user to search by student name
    Note that this function relies in two new functions: list_students() and name_search()"""
    response = 0
    while not (0 < response <= db_size):
        print(f"Welcome! Which student would you like to learn more about? (enter a number 1-{db_size})")
        print("...or... enter the letter 'a' to list all the students")
        print("...or... enter the letter 'n' to search by student names...")
        response = input("> ").lower()
        if response == 'a':
            list_students()
            # response = 0
        elif response == 'n':
            response = name_search()
        else:
            response = int(response)
        if (response != 'a' and response != 'n'):
            if not (0 < int(response) <= db_size):
                print("I'm sorry, that is not a valid entry, please try again...")
        else:
            response = 0
    return response-1

def ask_further_info(st_names):
    """This function determines if the user wants to know about 'hometown' or 'favorite food'"""
    response = ""
    while (response != 'hometown') and (response !='favorite food'):
        response = input(f"Do you want to know about {st_names}'s hometown or favorite food? ").lower()
    return response

def ask_further_info2(st_names):
    """This function is an enhancement to the one above.  It will allow entry of a part of a category."""
    response = "xxxx"
    while (True):   # break out when we get a valid response...
        if ('hometown'.find(response) >= 0):
            return 'hometown'
        elif ('favorite food'.find(response) >= 0):
            return 'favoritefood'
        else:
            if(response != "xxxx"):
                print("Your entry must ne either 'hometowm' or 'favorite food'.  Please try again...")
            response = input(f"Do you want to know about {st_names}'s hometowm or favorite food? ").lower()

####################################################################################################
#   lambdas

####################################################################################################
#   Main routine.
check_data()
while check_student == 'y':
    student_id = get_studentid2()
    print(f"student number {student_id+1} is {names[student_id]}")
    category = ask_further_info2(names[student_id])
    if (category == "favoritefood"):
        print(f"{names[student_id]}'s favorite food is: {favoritefoods[student_id]}")
    elif (category == "hometown"):
        print(f"{names[student_id]}'s hometown is: {hometowns[student_id]}")
    else:
        print(f"Got an invalid category - {category}")
    check_student = input(f"Do you want to know about another student? ").lower()


