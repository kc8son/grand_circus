multi_test = lambda x, y: x*y
print(multi_test(3, 7))

my_list = [x for x in range(5)]
print(my_list)
print(type(range(5)))

my_list2 = [range(5)] # This returns a list of range objects, not a list of integers!
print(type(my_list2))
