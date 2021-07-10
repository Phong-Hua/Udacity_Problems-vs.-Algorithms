# Problem 6

## Design

We use two variable min and max. We loop through the array and compare each element with current min and max 
and find new min and max. After finish the loop once, we have min and max of the array.

## Time complexity

We only need to traverse once, so time complexity is O(n).

## Space complexity

We only need 2 variables to hold value of min and max, so space complexity is O(1).


## Bonus: Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?

To sort a random list of element from 0-9, we loop through the list once. 
If value at current index is 0, we swap with value at index 0.
If value at current index is 1, we swap with value at index 1.
...etc....
With this approach we can sorting a random list of element from 0-9 with O(n) time complexity.