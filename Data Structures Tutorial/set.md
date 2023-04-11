# Sets

The set data structure is different from other data structures such as stacks and queues, 
in the sense that the order of data does not matter; The data has no inherent position.

Another key feature of sets is that they do not allow duplicate values. 
This means that any given value can appear in a set at most once. 
This constraint enables us to store data in a highly efficient manner for `Membership Testing`. 
In fact, membership testing is the most crucial operation associated with the set data structure.

We can use a method called `Hashing` to add, remove, and test for membership in O(1) time.

### Hashing

Let's assume we want to store a list of numbers from 0 to 9. If we wanted to add, remove, 
or test this list for membership at O(1) performance, we would consider the ```index(n) = n``` function.
Just plug the number 5 into our function and we would get the index 5. For this to work, our list would need to be size 10
to fit every number. This list is populated in a different way than dynamic arrays. This is called a `Sparse List` because
not every index is required to be filled from left to right. It is important to note that there is only one position per value,
so the set will not allow duplicate values.

If we had a list of much larger values, we can still manage our data without compromising our O(1) performance by incorporating
the modulo (%) operator into our function. For example, if we wanted to store 581,731,089 in a sparse list with a size of 10,
our function would look something like this ```index(581,731,089) = 581,731,089 % sparse_list_size``` = 9 (in this case the sparse-list-size is 10).
If we added a few more large numbers, our sparse list would look like this. 

|   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
|  ---  |  823,056,481  |  ---  |  613,082,973  |  ---  |  ---  |  ---  |  198,734,527  |  ---  |  581,731,089  |

The index(n) = n % sparse_list_size function works well for numbers, but we can also use this function for strings and floats as well.
To accomplish this, we can convert non-integer values so that the modulo operation applies to them. This is done by using a `Hashing Function`. Python has a built-in hash function. Our index function would then look like this ```index(n) = hash(n) % sparse_list_size```.

### Python Sets

In the Python programming language, sets are defined by using curly braces ```my_set = {1,2,3,4,5}```.
An empty set is a little bit different.\
We would create it like this ```empty_set = set()```.
The performance of sets is determined by the performance of the hashing algorithm.\
Below are a few examples of common set operations.

| Function | Code | Description | Performance |
|  ---  |  ---  |  ---  |  ---  |
|  member()  |  if value in my_set:  |  Determine if the value is in the set  |  O(1) |
|  add()  |  my_set.add()  |  Add a value to the set  |  O(1)  |
|  remove()  |  my_set.remove()  |  Remove a value from the set  |  O(1)  |
|  size()  |  length = len(my_set)  |  Return the number of values in the set  |  O(1)  |

### Set Operations

There are mathematical operations we can perform to interact with set data in useful ways known as `Unions` and `Intersections`.
Unions help us find all of the unique values between multiple sets.
Intersections help us find all of the common values between multiple sets.

```Python
set1 = {2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9}

set3 = intersection(set1, set2)
#alternatively the intersection could be written this way: set3 = set1 & set2  
#result is {5, 6}


set4 = union(set1, set2)
#alternatively the intersection could be written this way: set4 = set1 | set2  
#result is {2, 3, 4, 5, 6, 7, 8, 9}
```

To recap, some common use cases for sets include:

* Removing duplicates from a collection of items
* Checking whether an item is in a collection (Membership Testing)
* Finding unique values across multiple collections
* Finding common values across multiple collections

## Remove Duplicates Example

Let's say we were given a list of values and our task is to remove the duplicate values.

Here is our given list 
```Python
my_list = [1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 6, 7, 7, 8]
```

We can solve this by using a set. First let's convert our list into a set.

```Python
my_set = set(my_list)
```

Now that our list is a set, there are no duplicates.

```Python
print("Original list:" my_list)
print("List without duplicates:" my_set)
```

The results should be 

```Python
Original list: [1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 6, 7, 7, 8]
List without duplicates: {1, 2, 3, 4, 5, 6, 7, 8}
```

Let's throw another list in there and say we want only the common numbers between the two sets.

```Python
my_list = [1, 2, 2, 2, 3, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8]

my_set = set(my_list)

new_list = [2, 5, 5, 5, 7, 8, 9, 9, 9]

new_set = set(new_list)
```

We cannot perform an intersection on lists, so we convert them to sets.
Now we perform the intersection operation and print it to the user.

```Python
#create intersection
common_values = my_set & new_set

#print intersected set
print("Common values: ", common_values)
```

(Notice that although the number 5 is listed in each set at least twice, it still only shows in the output once.)

## Name Set

Let's put what we learned to the test. Write a code that creates a set and allows the user to add names to the set, using the add() function we learned about.
The user should not be able to add duplicate names to the set. The user should also be able to view the set of names and remove a name if desired, using the 
remove() function. If the user exceeds the set size, give the user the option to increase the set size. Once the user is done, the set of names is printed
to the user.

###Test Case #1

Add name 1.
Remove name 2.
Done 3.
Enter your choice: 1
Enter the name to add to your set: matthew
matthew was added

Names: {matthew}
Add name 1.
Remove name 2.
Done 3.
Enter your choice: 1
Enter the name to add to your set: mark
mark was added

Names: {matthew, mark}
Add name 1.
Remove name 2.
Done 3.
Enter your choice: 1
Enter the name to add to your set: luke
luke was added

Names: {matthew, mark, luke}
Add name 1.
Remove name 2.
Done 3.
Enter your choice: 1
Enter the name to add to your set: john
john was added

Names: {matthew, mark, luke, john}
Add name 1.
Remove name 2.
Done 3.
Enter your choice: 3

Final Set: {matthew, mark, luke, john}

###Test Case #2

Add name 1.
Remove name 2.
Done 3.
Enter your choice: 1
Enter the name to add to your set: matthew
matthew was added

Names: {sarah}
Add name 1.
Remove name 2.
Done 3.
Enter your choice: 1
Enter the name to add to your set: jean
jean was added

Names: {sarah, jean}
Add name 1.
Remove name 2.
Done 3.
Enter your choice: 1
Enter the name to add to your set: brad
brad was added

Names: {sarah, jean, brad}
Add name 1.
Remove name 2.
Done 3.
Enter your choice: 2
Enter the name to remove from your set: brad
brad was removed

Names: {sarah, jean}
Add name 1.
Remove name 2.
Done 3.
Enter your choice: 3

Final Set: {sarah, jean}

[Solution](set-solution.py)

