# Here is an example of a binary search tree:

class BST:
    # This defines what the BST will be. Notice that we delclare the Node class (ie what nodes are) below


    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    ###################
    # Start Problem 1 #
    ###################
    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if node != None:    
            if data != node.data:
                if data < node.data:
                    # The data belongs on the left side.
                    if node.left is None:
                        # We found an empty spot
                        node.left = BST.Node(data)
                    else:
                        # Need to keep looking.  Call _insert
                        # recursively on the left sub-tree.
                        self._insert(data, node.left)
                else:
                    # The data belongs on the right side.
                    if node.right is None:
                        # We found an empty spot
                        node.right = BST.Node(data)
                    else:
                        # Need to keep looking.  Call _insert
                        # recursively on the right sub-tree.
                        self._insert(data, node.right)
    
    #################
    # End Problem 1 #
    #################

    # Adding __iter__, _traverse_forware

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root


        def _traverse_forward(self, node):
            """
            Does a forward traversal (in-order traversal) through the 
            BST.  If the node that we are given (which is the current
            sub-tree) exists, then we will keep traversing on the left
            side (thus getting the smaller numbers first), then we will 
            provide the data in the current node, and finally we will 
            traverse on the right side (thus getting the larger numbers last).

            The use of the 'yield' will allow this function to support loops
            like:

            for value in my_bst:
                print(value)

            The keyword 'yield' will return the value for the 'for' loop to
            use.  When the 'for' loop wants to get the next value, the code in
            this function will start back up where the last 'yield' returned a 
            value.  The keyword 'yield from' is used when our generator function
            needs to call another function for which a `yield` will be called.  
            In other words, the `yield` is delegated by the generator function
            to another function.

            This function is intended to be called the first time by 
            the __iter__ function.
            """
            if node is not None:
                yield from self._traverse_forward(node.left)
                yield node.data
                yield from self._traverse_forward(node.right)
        
    # def __reversed__(self):
    #     """
    #     Perform a formward traversal (in order traversal) starting from 
    #     the root of the BST.  This function is called when a the 
    #     reversed function is called and is frequently used with a for
    #     loop.

    #     for value in reversed(my_bst):
    #         print(value)

    #     """        
    #     yield from self._traverse_backward(self.root)  # Start at the root

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
# After implementing 'no duplicates' rule,
# this next insert will have no effect on the tree.
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)
for x in tree:
    print(x)  # 1, 3, 4, 5, 6, 7, 10