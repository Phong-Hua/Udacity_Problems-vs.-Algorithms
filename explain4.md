# Problem 4

## Design

We use two variables to keep track of index of next zero and index of next two. Traverse through the list, 
if current number is 0, we swap value at current index with value at index of next zero.
If current number is 2, we swap value at current index with value at index of next two. 

## Time complexity

This solution only traverses through the list once, so time complexity is O(n).

## Space complexity

This is inplace sorted, no extra data space is used except variables to keep track of indexes. So, space complexity is O(1)