# Set Draft

The set data structure is different from other data structures such as stacks and queues, 
in the sense that the order of data does not matter; The data has no inherent position.

Another key feature of sets is that they do not allow duplicate values. 
This means that any given value can appear in a set at most once. 
This constraint enables us to store data in a highly efficient manner for testing membership. 
In fact, membership testing is the most crucial operation associated with the set data structure.

So, some common use cases for sets include:

* Removing duplicates from a collection of items
* Checking whether an item is in a collection (membership testing)
* Finding unique values across multiple collections
* Performing set operations such as union, intersection, and difference

We can use a method called hashing to add, remove, and test for membership in O(1) time.

### Hashing

Let's assume we want to store a list of numbers from 0 to 9. If we wanted to add, remove, 
or test this list for membership at O(1) performance, we would consider the ```index(n) = n``` function.

## Info

This will contain information about the dada structure

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

[Solution](set-solution.py)

