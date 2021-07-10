# Problem 3

## Design

To solve this problem, first we need to sort the input. This was done by using merge_sort() algorithm.
After the input is sorted, we create two numbers which their total are maximum. This is done in
create_numbers() function.
 
## Time complexity

### merge_sort funtion

Time complexity of this function depends on number_of_comparisons_per_iteration * number_of_iterations.
    1. number_of_comparisons_per_iteration depends on number_of_elements at each iteration.
        If 1 element => 0 comparisons.
        If 2 elements => 1 comparisons.
        If 3 elements => 2 comparisons.
        ..........
        If n elements => n-1 comparisons.
    2. number_of_iterations, depends on size of array.
        If 1 element => 0 iteration.
        If 2 elements => 1 iteration.
        If 3,4 elements => 2 iterations.
        If 5 - 8 elements => 3 iterations.
        ..........
        If n elements => log2(n) iterations.
Time complexity of merge_sort is O(n log n).

### create_numbers function

This function take sorted array as input, and loop through all elements of that array to create two required numbers.
So, time complexity of this function is O(n).

### Total time complexity

Time complexity of solution is total time complexity of two functions above, O(n log n) + O(n), which is O(n), linear complexity.

## Space complexity

### merge_sort function

Space complexity of this merge_sort depends on space complexity of merge() function.
Every time the merge() function is executed, a new array is created which has all elements of two arrays input. 
Assume, we discards all arrays were created in the middle steps and only keep the array created in final step, 
the space complexity is O(n).

### create_numbers function

Space complexity of this function is O(n), because we create a two numbers from the input array.

### Total space complexity

Space complexity of this solution is total space complexity of two functions above, O(n) + O(n) = O(n), which is linear complexity.