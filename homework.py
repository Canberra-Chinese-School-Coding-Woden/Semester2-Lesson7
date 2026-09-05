# In class, we have made two functions: find_largest and find_smallest. Using the same idea/code structure, write a function "find_sum" that finds the sum of a number list.
# The two functions "find_largest" and "find_smallest" are here for your information. You don't need these two functions to write the "find_sum" function.

int_list = [3, 4, 9, 2]

def find_largest(ls):  # ls means list
    largest = ls[0]
    for i in ls:
        if i > largest:
            largest = i
    return largest

def find_smallest(ls):
    smallest = ls[0]
    for i in ls:
        if i < smallest:
            smallest = i
    return smallest

def find_sum(ls):
    # TODO

print("smallest = " + find_smallest(int_list))
print("largest = " + find_largest(int_list))
print("sum = " + find_sum(int_list))









