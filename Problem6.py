"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. 
Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == None or ints == []:
        return (None, None)
    if len(ints) == 1:
        return (ints[0], ints[0])

    min = None
    max = None
    for num in ints:
        if min == None or min > num:
            min = num
        
        if max == None or max < num:
            max = num
    
    return (min, max)
    

## Example Test Case of Ten Integers
import random


def test_normal_cases():
    
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    
    random.shuffle(l)
    
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

def test_edge_cases():
    """
    Testing edge cases: with None or empty list
    """

    print("************Edge case: Input list is None************")
    arr_1 = None
    print ("Pass" if ((None, None) == get_min_max(arr_1)) else "Fail")

    print("************Edge case: Input list is []************")
    arr_2 = []
    print ("Pass" if ((None, None) == get_min_max(arr_2)) else "Fail")

    print("************Edge case: Input list has only one number************")
    arr_3 = [1]
    print ("Pass" if ((1, 1) == get_min_max(arr_3)) else "Fail")

    print("************Edge case: Input list has only one type of digit************")
    arr_4 = [2, 2, 2, 2]
    print ("Pass" if ((2, 2) == get_min_max(arr_4)) else "Fail")

    print("************Edge case: Input list has None element************")
    arr_5 = [None, 2, 4, 6, 3, 1]
    print ("Pass" if ((1, 6) == get_min_max(arr_5)) else "Fail")


test_normal_cases();
test_edge_cases();