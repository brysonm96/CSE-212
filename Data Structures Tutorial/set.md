# Set Draft

The set data structure is different from other data structures such as stacks and queues, 
in the sense that the order of data does not matter; The data has no inherent position.

Another key feature of sets is that they do not allow duplicate values. 
This means that any given value can appear in a set at most once. 
This constraint enables us to store data in a highly efficient manner for testing membership. 
In fact, membership testing is the most crucial operation associated with the set data structure.

So, some common use cases for sets include:

* Removing duplicates from a collection of items
* Checking whether an item is in a collection (`Membership Testing`)
* Finding unique values across multiple collections
* Performing set operations such as union, intersection, and difference

We can use a method called `Hashing` to add, remove, and test for membership in O(1) time.

### Hashing

Let's assume we want to store a list of numbers from 0 to 9. If we wanted to add, remove, 
or test this list for membership at O(1) performance, we would consider the ```index(n) = n``` function.
Just plug the number 5 into our function and we would get the index 5. For this to work, our list would need to be size 10
to fit every number. This list is populated in a different way than dynamic arrays. This is called a `Sparse List` because
not every index is required to be filled from left to right. It is important to note that there is only one position per value,
so the set will not allow duplicate values.

If we had a list of much larger values, we can still manage our data without compromising our O(1) performance by incorporating
the modulo (%) operator into our function. To store 10 digit number (memory for a 1 billion sized sparse list)
our function would look something like this ```index(n) = n % 10```.

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

