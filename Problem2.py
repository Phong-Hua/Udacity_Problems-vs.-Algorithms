"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list == None or input_list == [] or number == None:
        return -1
    
    def find_pivot_index(arr, start, end):
        """
        Use binary search to find index of pivot
        """
        if start == None or end == None or start > end:
            return None
        if start == end:
            return start

        middle = (start + end) // 2
        if arr [middle] == arr[end]:    # because no duplicates in the array, in this case start = end = middle.
            return middle
        elif arr[middle] < arr[end]:  # the pivot is at this middle or in left of middle
            if arr[middle-1] > arr[middle]: # the pivot is at this middle
                return middle
            return find_pivot_index(arr, start, middle-1)
        else:   # arr[middle] > arr[end], the pivot is in right of middle
            return find_pivot_index(arr, middle+1, end)

    def find_target_index(arr, target, start, end):
        """
        Use binary search to find index of target in between start and end indexes of arr.
        """
        if target == None or start == None or end == None or start > end:
            return -1
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:  # search on the left
            return find_target_index(arr, target, start, middle-1)
        else: # search on the right
            return find_target_index(arr, target, middle+1, end)
        

    pivot = find_pivot_index(input_list, 0, len(input_list)-1)
    print(f"pivot_index: {pivot}")
    if input_list[pivot] == number:
        return pivot
    elif input_list[pivot] < number and number <= input_list[-1]:
        return find_target_index(input_list, number, pivot, len(input_list)-1)
    else:
        return find_target_index(input_list, number, 0, pivot-1)  

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    linear_search_index = linear_search(input_list, number)
    rotated_array_search_index = rotated_array_search(input_list, number)

    print(f"linear_search_index: {linear_search_index}")
    print(f"rotated_array_search_index: {rotated_array_search_index}")

    if  linear_search_index == rotated_array_search_index:
        print("Pass")
    else:
        print("Fail")

def test_normal_cases():
    """
    Testing normal cases.
    """
    print("***********************Testing normal cases***********************")
    print("***********************Target is in first index***********************")
    arr_1 = [6, 7, 8, 9, 10, 1, 2, 3, 4]
    target = 6
    print(f"array: {arr_1}")
    print(f"target: {target}")
    test_function([arr_1, target])
    # Pass
    print("***********************Target is pivot***********************")
    target = 1
    print(f"array: {arr_1}")
    print(f"target: {target}")
    test_function([arr_1, target])
    # Pass

    print("***********************Target is in one index before pivot***********************")
    arr_2 = [6, 7, 8, 1, 2, 3, 4]
    target = 8
    print(f"array: {arr_2}")
    print(f"target: {target}")
    test_function([arr_2, target])
    # Pass

    print("***********************Target is pivot***********************")
    target = 1
    print(f"array: {arr_2}")
    print(f"target: {target}")
    test_function([arr_2, target])
    # Pass
    print("***********************Target is not in the list***********************")
    target = 10
    print(f"array: {arr_2}")
    print(f"target: {target}")
    test_function([arr_2, target])
    # Pass

def test_edge_cases():
    """
    Testing edge cases where array is empty, has 1 element, or array has no pivot point
    """
    print("***********************Testing edge cases***********************")
    # Array is empty
    print("***********************Array is empty***********************")
    arr_e_1 = []
    target = 1
    print(f"array: {arr_e_1}")
    print(f"target: {target}")
    test_function([arr_e_1, target])
    # Pass

    # Array only has 1 element
    print("***********************Array only has 1 element***********************")
    arr_e_2 = [1]
    target = 1
    print(f"array: {arr_e_2}")
    print(f"target: {target}")
    test_function([arr_e_2, target])
    # Pass

    # Array has no pivot point
    print("***********************Array has no pivot point***********************")
    arr_e_3 = [1, 2, 3, 4]
    target = 4
    print(f"array: {arr_e_3}")
    print(f"target: {target}")
    test_function([arr_e_3, target])
    # Pass

test_normal_cases();
test_edge_cases();