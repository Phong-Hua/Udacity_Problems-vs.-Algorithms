# Problem 5

## Design

Before can implement the autocomplete function, we need to create a working trie for storing strings.
We will create two classes:
* A `Trie` class that contains the root node (empty string)
* A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

## Time Complexity

### TrieNode

#### insert function

This function take O(1) time complexity.

#### get function

This function take O(1) time complexity.

#### suffix function

We do breadth-first traversal to visit all node from the prfix 
to collects the suffix. For worstcase, we might need to travel entire trie. So time complexity is O(n), which n is total node of the trie.

### Trie

#### insert function

Time complexity of this function depends on size of word input.
For worstcase, this can take O(n) time complexity.

#### find function

Time complexity of this function depends on size of prefix input.
For worstcase, this can take O(n) time complexity.

## Space Complexity

### TrieNode

#### insert function

This function take O(1) space complexity.

#### get function

This function take O(1) space complexity.

#### suffix function

Since we need an array to store all suffixes. For worstcase, we might collect all suffixes from root node, and this take O(n) space complexity.

### local variables

For worstcase, this is a root node and can have O(n) space complexity for 'chars'.

### Trie

#### insert function

Space complexity of this function depends on size of word input.
If a charater in word is new, a new TrieNode is created. For worstcase, space complexity is O(n).

#### find function

Space complexity of this function is O(1) as we only need one variable 
reference to the node represent the prefix.

#### local variables

Space complexity O(n) as it has reference to root node.