"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. 
You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. 
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, 
return any one.

Here is some boilerplate code and test cases to start with:
"""

def create_numbers(input_list):
    """
    This function take in a sorted input_list and create an array of two number which their sum is maximum.
    The number of digits in both the numbers cannot differ by more than 1.
    """
    number_1, number_2 = '', ''
    append_number_1 = True

    for index in range(len(input_list)-1, -1, -1):
        if append_number_1:
            number_1 += str(input_list[index])
        else:
            number_2 += str(input_list[index])
        append_number_1 = not append_number_1
    try:
        return [int(number_1), int(number_2)]
    except:
        return [None, None]

def merge_sort(input_list):
    """
    Sort input_list using merge_sort algorithm.
    """

    def merge(left, right):
        """
        Compare the element of left and right, and merge them together, in ascending order.
        """
        result = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        result += left[left_index:]
        result += right[right_index:]
        return result

    if not input_list or len(input_list) <= 1:
        return input_list
    
    middle = len(input_list) // 2
    left = input_list[:middle]
    right = input_list[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_input = merge_sort(input_list)
    return create_numbers(sorted_input)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Testing normal case
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Pass

# Testing normal case
test_function([[6, 2], [6, 2]])
# Pass

# Testing edge case, input of [0, 0]
test_function([[0, 0], [0, 0]])
# Pass

# Testing edge case, input are already sorted
test_function([[1, 2, 3, 4, 5], [542, 31]])
# Pass

# Testing edge case, input is an array of 1 number, [2, 2, 2, 2, 2]
test_function([[2, 2, 2, 2, 2], [222, 22]])
# Pass