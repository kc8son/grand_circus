####################################################################################################
#
#   Date Written: 03/02/2023        By: Joseph P. Merten
#   Day 3 - Powers Table
#   This was interesting because I learned about the end= argument to the print() function.
#       ref: https://docs.python.org/3/library/functions.html#print
#
####################################################################################################
#   imports

#   variables
count = 1
continue_flag = 'y'

#   main routine
print("Learn your squares and cubes!\n")

####################################################################################################
#   Outer loop to request limit...
while (continue_flag.lower() == 'y'):
    limit = int(input("Enter an integer: "))
    print("""
    Number\t\tSquared\t\tCubed
    =======\t\t=======\t\t======""")
    ####################################################################################################
    #   inner loop to print each number & powers
    while (count <= limit):
        print(f"\t{count}\t\t{count**2}\t\t{count**3}")
        count+=1
    print("-"*100+"\n")
    ####################################################################################################
    #   Add a multiplication table - first print the headings.
    print("Multiplication Table:\n----------------------")
    for i in range(limit):
        print(f"\t{i+1}", end="")   #   Add 1 to i sinde range() is zero relative
    print("")
    for i in range(limit):
        print(f"\t=", end="")
    print("")
    ####################################################################################################
    #   first loop to get the first multiplicand.
    for i in range(limit):
        print(f"{i+1} |", end="")
        ####################################################################################################
        #   Second loop for the second multiplicand and then print the product.
        for j in range(limit):
            print(f"\t{(i+1)*(j+1)}", end="")
        print("")   # Extra print to start a new line since we're forcing print() on one line.
    print("")   # Another extra print to start a new line since we're forcing print() on one line.
    count = 1   # Reset our counter and see if we want to go again.
    continue_flag = input("\n\nContinue? (y/n): ")


