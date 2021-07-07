"""
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. 
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, 
that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None or len(input_list) <= 1:
        return input_list

    last_zero_index = 0
    first_two_index = len(input_list) - 1
    current_index = 0

    while current_index <= first_two_index:
        num = input_list[current_index]
        if num == 0:
            input_list[last_zero_index], input_list[current_index] = input_list[current_index], input_list[last_zero_index]
            current_index += 1
            last_zero_index += 1
        elif num == 2:
            input_list[first_two_index], input_list[current_index] = input_list[current_index], input_list[first_two_index]
            first_two_index -= 1
        else:
            current_index += 1
        
    return input_list


def test_function(test_case):

    print(f"Before sorted {test_case}")

    sorted_array = sort_012(test_case)

    print(f"After sorted {sorted_array}")

    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

def test_normal_cases():
    print("***********************Testing normal cases***********************")
    test_normal_case_1();
    test_normal_case_2();

def test_normal_case_1():
    print("***********************Testing normal case 1***********************")
    arr = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    test_function(arr)

def test_normal_case_2():
    print("***********************Testing normal case 2***********************")
    arr = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
    test_function(arr)

def test_edge_case_1():
    print("***********************Input is empty***********************")
    arr = []
    test_function(arr)

def test_edge_case_2():
    """
    The input list is [0]
    """
    print("***********************Input list is [0]***********************")
    arr = [0]
    test_function(arr)

def test_edge_case_3():
    """
    The input list is [1]
    """
    print("***********************Input list is [1]***********************")
    arr = [1]
    test_function(arr)

def test_edge_case_4():
    """
    The input list is [2]
    """
    print("***********************Input list is [2]***********************")
    arr = [2]
    test_function(arr)

def test_edge_case_5():
    """
    The input list contains only zero
    """
    print("***********************Input list contains only zero***********************")
    arr = [0, 0, 0, 0, 0]
    test_function(arr)

def test_edge_case_6():
    """
    The input list contains only one
    """
    print("***********************Input list contains only one***********************")
    arr = [1, 1, 1, 1, 1]
    test_function(arr)

def test_edge_case_7():
    """
    The input list contains only two
    """
    print("***********************Input list contains only two***********************")
    arr = [2, 2, 2, 2, 2]
    test_function(arr)

def test_edge_case_8():
    """
    The input list is mix of zero and one
    """
    print("***********************Input list is mix of zero and one***********************")
    arr = [1, 0, 0, 0, 1, 1, 1, 0, 0, 1]
    test_function(arr)

def test_edge_case_9():
    """
    The input list is mix of zero and two
    """
    print("***********************Input list is mix of zero and two***********************")
    arr = [2, 0, 0, 0, 2, 2, 2, 0, 0, 2]
    test_function(arr)

def test_edge_case_10():
    """
    The input list contains is mix of one and two
    """
    print("***********************Input list contains is mix of one and two***********************")
    arr = [2, 1, 1, 1, 2, 2, 2, 1, 1, 2]
    test_function(arr)

def test_edge_case_11():
    """
    The input list is a sorted list of zero and one
    """
    print("***********************Input list is a sorted list of zero and one***********************")
    arr = [0, 0, 0, 0, 1, 1, 1, 1]
    test_function(arr)

def test_edge_case_12():
    """
    The input list is a sorted list of zero and two
    """
    print("***********************Input list is a sorted list of zero and two***********************")
    arr = [0, 0, 0, 0, 2, 2, 2, 2]
    test_function(arr)

def test_edge_case_13():
    """
    The input list is a sorted list of one and two
    """
    print("***********************Input list is a sorted list of one and two***********************")
    arr = [1, 1, 1, 1, 2, 2, 2, 2]
    test_function(arr)

def test_edge_case_14():
    """
    The input list is a sorted list of zero, one and two
    """
    print("***********************Input list is a sorted list of zero, one and two***********************")
    arr = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
    test_function(arr)

def test_edge_cases():
    print("***********************Testing edge cases***********************")
    test_edge_case_1();
    test_edge_case_2();
    test_edge_case_3();
    test_edge_case_4();
    test_edge_case_5();
    test_edge_case_6();
    test_edge_case_7();
    test_edge_case_8();
    test_edge_case_9();
    test_edge_case_10();
    test_edge_case_11();
    test_edge_case_12();
    test_edge_case_13();
    test_edge_case_14();

test_normal_cases();
test_edge_cases();
