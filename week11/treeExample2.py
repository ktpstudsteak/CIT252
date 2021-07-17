"""
CSE212 
(c) BYU-Idaho
09-Prove - Problems

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

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

    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

    ###################
    # Start Problem 2 #
    ###################
    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if node != None:
            if data == node.data:
                # print(node.data)
                return True
            elif node.data < data:
                if node.right == None:
                        return False
                else:
                    return self._contains(data, node.right)
            else:
                if node.left == None:
                    return False
                else:
                    return  self._contains(data, node.left)



                
            # else:
            #     if data < node.data:
            #         self._contains(data, node.left)
            #         return 

            #     elif data > node.data:
            #         self._contains(data, node.right)
            #         return
            #     else:
            #         return False

    #################
    # End Problem 2 #
    #################

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