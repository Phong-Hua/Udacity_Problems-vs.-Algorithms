"""
HTTPRouter using a Trie

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, 
but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. 
In a dynamic web server, the content will often come from a block of code called a handler.

"""

"""
First we need to implement a slightly different Trie than the one we used for autocomplete. 
Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. 
In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which 
would be responsible for handling requests to that path. 
For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, 
but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. 
A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). 
A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. 
We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

"""

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = dict()
        self.handler = None

    def insert(self, part):
        # Insert the node as before
        if part not in self.children:
            self.children[part] = RouteTrieNode()

    def insert_handler(self, handler):
        # Insert handler
        self.handler = handler

    def get_node(self, part):
        # Get the node contains this part
        return self.children.get(part, None)
    
    def get_handler(self):
        # Get handler for this node
        return self.handler

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.insert_handler(handler)
        self.str_404 = '404 not found'
        
    
    def get_root_handler(self):
        """
        Get root handler
        """
        return self.root.get_handler()

    def insert_root_handler(self, handler):
        """
        Insert handler for root node
        """
        self.root.insert_handler(handler)

    def insert_404(self, handler):
        """
        Insert 404 handler
        """
        self.root.insert(self.str_404)
        node_404 = self.root.get_node(self.str_404)
        node_404.insert_handler(handler)

    def get_404(self):
        """
        Get handler for 404 route
        """
        return self.root.get_node(self.str_404).get_handler()
    
    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        """
        Insert handler for a specific path. path is splitted into a list of parts [].
        """
        current_node = self.root
        for part in parts:
            if part:
                current_node.insert(part)
                current_node = current_node.get_node(part)
        current_node.insert_handler(handler)

    
    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for part in parts:
            if part and current_node:
                current_node = current_node.get_node(part)
        if current_node:
            return current_node.get_handler()
        return None


"""
Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. 
It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character

Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. 
Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

"""

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root_handler)
        self.trie.insert_404(not_found_handler)


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        # handle None
        if path is None:
            return;
        path = str(path).strip()
        # handle root
        if len(path) == 0 or path == '/':
            self.trie.insert_root_handler(handler)
            return;
        parts = self.__split_path__(path)
        self.trie.insert(parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        
        # handle None path
        if path is None:
            return self.trie.get_404()
        path = str(path).strip()

        # home route
        if len(path) == 0 or path == '/':
            return self.trie.get_root_handler()

        parts = self.__split_path__(path)
        handler = self.trie.find(parts)
        if handler:
            return handler
        # Return 404 handler
        return self.trie.get_404()



    def __split_path__(self, path):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return path.split('/')

"""
Test Cases
"""
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# # some lookups with the expected output
# Normal case 1
print("********Path is:'/home'*********")
print("Pass" if router.lookup("/home") == 'not found handler' else 'Fail') # should print 'not found handler' or None if you did not implement one

# Normal case 2
print("********Path is:'/home/about'*********")
print("Pass" if router.lookup("/home/about") == 'about handler' else 'Fail') # should print 'about handler'

# Normal case 3
print("********Path is:'/home/about/'*********")
print("Pass" if router.lookup("/home/about/") == 'about handler' else 'Fail') # should print 'about handler' or None if you did not handle trailing slashes

# Normal case 4
print("********Path is:/home/about/me*********")
print("Pass" if router.lookup("/home/about/me") == 'not found handler' else 'Fail') # should print 'not found handler' or None if you did not implement one

# Edge case 1: None path
print("********Edge case 1: None path*********")
print("Pass" if router.lookup(None) == 'not found handler' else 'Fail') # should print 'not found handler'

# Edge case 2: '' path
print("********Edge case 2: '' path*********")
print("Pass" if router.lookup('') == 'root handler' else 'Fail') # should print 'root handler'

# Edge case 3: '   ' path
print("********Edge case 3: '   ' path*********")
print("Pass" if router.lookup('   ') == 'root handler' else 'Fail') # should print 'root handler'

# Edge case 4: '/' path
print("********Edge case 4: '/' path*********")
print("Pass" if router.lookup("/") == 'root handler' else 'Fail') # should print 'root handler'

# Edge case 5: Insert root handler for '' path
print("********Edge case 5: Insert handler for '' path*********")
router.add_handler('', 'new root handler 1')
print("Pass" if router.lookup("/") == 'new root handler 1' else "Fail") # should Pass

# Edge case 6: Insert root handler for '   ' path
print("********Edge case 6: Insert handler for '  ' path*********")
router.add_handler('    ', 'new root handler 2')
print("Pass" if router.lookup("    ") == 'new root handler 2' else "Fail") # should Pass

# Edge case 7: Insert root handler for '/' path
print("********Edge case 6: Insert handler for '/' path*********")
router.add_handler('/', 'new root handler 3')
print("Pass" if router.lookup("    ") == 'new root handler 3' else "Fail") # should Pass