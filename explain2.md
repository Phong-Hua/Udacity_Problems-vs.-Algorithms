# Problem 2

## Design

To solve this problem, we need to find pivot index in input_list, this was done by using binary search algorithm. 
After having pivot, we know where the target will be, and find index of target using binary search algorithm.

## Time complexity

The solution was implemented using binary search algorithm only, so time complexity is O(log n).

## Space complexity

With binary search algorithm, there is no extra space is used, except a local variable to hold value of pivot index,
so space complexity is O(1).
