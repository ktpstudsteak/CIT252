# Here is an example of a binary search tree:

class BST:
    # This defines what the BST will be. Notice that we delclare the Node class (ie what nodes are) below

    class Node:
        # Each node will have data and pointers to each subtree

         def __init__(self, data):
           # Initialize node and provide data for it
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        # Initialize an empty BST
        self.root = None
    
    """
    Inserting Data Example
    """
    def insert(self, data):
        """
        This function will insert data into the BST. If the BST is 
        empty then the self.root will be equal to the new node. If 
        there is data there, then use recursion to find where to place
        the new node and data.
        """