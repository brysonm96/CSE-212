# Trees

Trees are similar to linked list in the sense that it uses nodes and pointers to connect them. The difference is that trees
can connect to multiple different nodes. In computing, trees are used for sorting and searching, becuse they provide a hierarchal structure.
We will take a look at a few different types of trees, as well as some of their common operations.

## Binary Tree

A `Binary Tree` is a type of tree where each node can have up to two connections to other nodes.\
The highest node in the tree is called the `Root Node`. There is always only one root node.\
Nodes with connected nodes are called `Parent Nodes`.\
The node that is connected to the parent is known as a `Child Node`.\
Nodes without any connected nodes are called `Leaf Nodes`.\
The group of nodes on the left or right side of the parent node form a `Subtree`


![binary tree](binary-tree.png)

## Binary Search Tree

A `Binary Search Tree` (BST) is like a binary tree, but it follows specific rules for storing the data entered.
Data is stored in the BST by comparing it to the value of the parent node. When the data is of lower value than the parent,
it is stored in the left subtree. If the data is of greater value than the parent, it is stored in the right subtree. 
This process always starts at the root node, and continues until the data has found its place.

![binary search tree](binary-search-tree.png)

If we have a linked list or dynamic array containing values, we would have a performance of O(n) as we search for
the location to insert our data.
By incorporating a BST, we are increasing efficiency and performance; we are essentially removing a subtree per comparison.
This results in a better performance of O(log n).


## Examples

This will contain examples about the data structure

## Table

|   X   |   X   |   X   |
|  ---  |  ---  |  ---  |
|  ---  |  ---  |  ---  |
|  ---  |  ---  |  ---  |
|  ---  |  ---  |  ---  |
|  ---  |  ---  |  ---  |

## Code Problem

This will contain a problem to solve with code

[Solution](tree-solution.py)

