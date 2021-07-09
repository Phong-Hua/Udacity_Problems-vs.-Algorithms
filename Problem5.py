#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.chars = dict()
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.chars:
            self.chars[char] = TrieNode()
    
    def get(self, char):
        ## Get a child node contains this char
        return self.chars.get(char)
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        if word is None:
            return;

        current_node = self.root
        for char in word:
            current_node.insert(char)
            current_node = current_node.get(char)
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if prefix is None:
            return None

        current_node = self.root
        for char in prefix:
            if not current_node:
                return None
            current_node = current_node.get(char)
        return current_node

# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

from queue import Queue

def suffixes(self, suffix = ''):
    ## Recursive function that collects the suffix for 
    ## all complete words below this point
    result = []
    # use queue to do breadth-first traversal
    # item in queue is tuple of TrieNode and prefix
    queue = Queue()
    queue.put((self, ''))
        
    def find_suffixes_recursive(queue, result):
        """
        Use queue to do breadth-first traversal and add item to result
        """
        if not queue.empty():
            item = queue.get()
            trie_node, prefix = item
            # add node to result if it is word and prefix is not empty
            if trie_node.is_word and len(prefix) > 0:
                result.append(prefix)
                # adding new items to queue
            for char, child_node in trie_node.chars.items():
                new_prefix = prefix + char
                queue.put((child_node, new_prefix))
                    
            find_suffixes_recursive(queue, result)
        
    find_suffixes_recursive(queue, result)
    return result

TrieNode.suffixes = suffixes


def test_function(prefix = '', trie=Trie()):
    if prefix != '':
        prefixNode = trie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(str(prefix) + " not found")
    

def test_normal_cases():

    print("************************************************")
    print("**************Testing normal cases**************")
    print("************************************************")

    MyTrie = Trie()
    wordList = [
        "a", "ant", "anthology", "antagonist", "antonym", 
        "fun", "function", "factory", 
        "trie", "trigger", "trigonometry", "tripod"
    ]

    for word in wordList:
        MyTrie.insert(word)

    

    print("**************Finding for prefix 'f'**************")
    test_function('f', MyTrie)
    # un, actory, unction

    print("**************Finding for prefix 'a'**************")
    test_function('a', MyTrie)
    # nt, nthology, ntagonist, ntonym


def test_edge_cases():


    print("**********************************************")
    print("**************Testing edge cases**************")
    print("**********************************************")

    def edge_case_1():
        """
        Testing with an empty trie
        """
        MyTrie = Trie()
        print("**************Finding for prefix 'f'**************")
        test_function('f', MyTrie)
        # f not found

    def edge_case_2():
        """
        Insert None to Trie
        """
        MyTrie = Trie()
        MyTrie.insert(None)
        print("**************Insert None to Trie**************")
        test_function('f', MyTrie)
        # f not found
    
    def edge_case_3():
        """
        Testing with word is None
        """
        MyTrie = Trie()
        wordList = ["a", "ant", "anthology", "antagonist", "antonym"]
        for word in wordList:
            MyTrie.insert(word)
        print("**************Testing with word is None**************")
        test_function(None, MyTrie)
        # None not found

    edge_case_1();
    edge_case_2();
    edge_case_3();

test_normal_cases();
test_edge_cases();