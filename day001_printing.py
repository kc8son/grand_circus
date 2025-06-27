####################################################################################################
#
#   Date Written: 02/27/2023        By: Joseph P. Merten
#   Just experimenting with strings and printing.
#
####################################################################################################
print('Hello')   # This is the first word
print("World")

name = "Fred"
print(name)

name = 'Sally'
print(name)

words = 'This "string" contains duble quotes'
print(words)

words = "This 'string' has single quotes"
print(words)

words = 'This string has both "double" quotes \'single\' quotes'
print(words)

str = "xyz123"
strlen=len(str)
print(strlen)

str = 'abcdefgh'
print(len(str))

print(str[0])
print('abcdefgh'[0])
first = str[0]
print(first)

#   Print first three (0-2)
print(str[0:3])

#   negative indexes
print(str)
print(str[-3:-1])

string1 = 'abc'
string2 = 'def'
bigstr = string1 + string2
print(bigstr)

# other ways to build strings...
print('Joe '*5)
print('%'*40)

#   Multi line string... """ or '''
lstr = """
Alpha
Bravoc
Charlie
Delta
Ech0"""
print(lstr)

lstr = '''
Echo
Foxtrot
Golf
'''
print(lstr)

num = 10
print(num/4)    # float
print(num//4)   # int
print(num/3)    # float
print(num//3)   # int
print(num%3)    # modulo - always int

num = 10
print(num * 3.5)    # float
print(num*3.0)      # float
print(num*3)        # int
print(type(num))

radius = float(input("""
Enter the radius for a cirle.
Make it an integer...
"""))
print("The area is: {}".format(radius*radius*3.1415))