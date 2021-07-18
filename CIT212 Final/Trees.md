# Trees

## What are trees?

Trees are a useful tool. They are similar to linked lists in that they point to the next item/node, but differ in that they can point to multiple items.

For example, binary trees can connect to no more than 2 nodes.

Keep the following in mind about trees:

* The highest node is called the **root node**. 
* Nodes that have connections are called **parent nodes**. 
* Nodes that have parent nodes are called **child nodes**.
* Nodes that have no child nodes are called **leaf nodes**.
* And to steal from the reading, "The nodes to the left and right of any parent node form a **subtree**".
* There can only be **one** root node.

Binary search trees vs balanced binary search trees

Consider this image:

![Binary Search Tree](https://byui-cse.github.io/cse212-course/lesson09/binary_tree.jpeg)
 

## Tree use cases
Trees can be used for efficient searching and organizing of data. Especially when combined with recursion.

## Performance

Binary search trees have a BigO of O(N) whereas balanced trees have a BigO of O(logN). 

 

## Examples
Here are examples for inserting items to a BST, get the tree height, and search the tree for data. 

See [treeExample.py](./treeExample.py) for these examples in full context.

### Inserting into a BST

```python
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
```

### Get Tree Height

```python
    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        if node is None:
            return 0
        else:
            right = self._get_height(node.right)
            left = self._get_height(node.left)
            return 1 + max([left, right])

```

### Search the Tree
```python
    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        data provided.
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

```

 

## Problem
Using the provided code in [treeProblem.py](./treeProblem.py) create functions to insert, get the tree height, and search data in the BST.


## Jump to Section:

#### [Welcome](./welcome.md)

#### Queues
* [Queues](./Queues.md)
* [Queue Examples](./queueExample.py)
* [Queue  Problems](./queueProblem.py)

#### Sets
* [Sets](./Sets.md)
* [Set Examples](./setExample.py)
* [Set  Problems](./setProblem.py)

#### Trees
* [Trees](./Trees.md)
* [Tree Examples](./treeExample.py)
* [Tree Problems](./treeProblem.py)