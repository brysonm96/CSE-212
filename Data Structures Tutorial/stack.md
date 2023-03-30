# Stacks

### Key Terms

- Front
- Back
- Push
- Pop

A stack is a data structure that uses "LIFO" (Last in, First out) to determine the order that data is entered and removed.
Chances are you've encountered stacks before, if you've ever messed up while writing a paper and had to undo your error. 

To understand stacks we can visualize them as a plate of pancakes. 
The `Front` of the stack would be the first pancake that was made, or the first item of data that was entered. 
The following data will then enter behind, essentially covering the data before it. 
The `Back` of the stack would be the most recent pancake that was made, or the last item of data that was entered.
When data is added to the stack, it is called a `Push`, and is added to the back.
Whene data is removed from the stack, it is called a `Pop`, and is removed from the back.

![pancake_design](pancake-stack.png)


This is how we are able to press undo while writing a word document and it will remove the last action.
Let's say you write the sentence "The clouds moved and revealed the blue sky". The word "The" would be at the front of the stack, followed by "clouds", then "moved",
and so on. The word "sky" would be at the back of the stack. The undo button would pop "sky" and the word would be removed.

### Python Stacks

In Python, stacks can be defined using lists. The following table displays information about some common python functions regarding stacks.
Note that the performance of stacks is based on the performance of the dynamic array.

| Function          | Code              | Description          | Performance (in Big O)          |
| ----------------- | ----------------- | -------------------- | --------------------- |
| size() | size = len(stack) | return stack size | O(1)  |
| empty() | if len(stack) == 0 | returns whether the stack is empty | O(1)  |
| push() | stack.append(value) | adds item to the back of the stack | O(1)  |
| pop() | value = stack.pop() | return and remove item from the back of the stack | O(1)  |
| full() | print("Is full", stack.full()) | return whether the stack is at max size | O(1)  |





### Stacks and functions

Anytime we uses functions in our software, we are using a stack. Whenever we call a function in our code, there needs to be some 
kind of placeholder to remember where in the code you need to return to after the function has executed. This is why stacks are important.
After calling a function the computer is told to jump to that function and follow the instructions through. The computer then uses the back
of the stack as a reference for where to return in the code when it is done.
This works the same in the case that a call to a function is used inside another function. The original place in the code will always be
stored and wait for the function to finish executing.
The stack keeps track of when functions are called. This is helpful for errors and debugging because we can see where exactly the code encountered the problem.



## Reverse String Example

Let's see an example code using a stack. If you wanted to use a keyword for a password, but you don't want it to be easy to guess, try plugging the word into
a python code that will reverse the word using a stack. First we will create a stack class with an empty list.

```python
class Stack:
    def __init__(self):
        self.data = []        
```

The "__init__(self)" method initializes a list to store the data of the stack.
But we'll need a few more methods for this code to work.

```python
    # empty() function
    def is_empty(self):
        return len(self.data) == 0

    # pop() function
    def remove(self):
        return self.data.pop()

    # push() function
    def add(self, item):
        self.data.append(item)

```

The "is_empty(self) method" returns a Boolean value stating whether the stack is empty or not.
The "remove(self)" method removes and returns the item from the top of the stack.
The "add(self)" method appends the item to the top of the stack.

Now we can add the function to reverse the word

```python
def reverse(string):
    stack = Stack()
    for char in string:
        stack.add(char)

    reversed_string = ''
    while stack.is_empty() is False:
        reversed_string += stack.remove()

    return reversed_string
```

The "reverse(string)" function receives a string and makes an empty stack using the Stack() constructor.
The function iterates through each character of the string and pushes it onto the stack using the add(char) method.
The function then pops each character from the stack using the remove() method and adds it to the reversed_string until the stack is empty.
The function then returns the reversed string.

We're almost done!

```python
# Replace the string with your key word
word = "Rexburg"
reversed_string = reverse(word)
print(reversed_string)
```

Now the code has a word variable to pass to the reverse(string) method.
The reversed word is then printed to the user. Awesome!

## Practice: Grocery List

Let's put what we learned to the test. Write a code that will prompt the user to add an item to a grocery list. 
After adding an item, the user should be asked if they would like to add another item or undo their last item. 
Use a stack list to handle the case where the user undoes the last item added to the list.

### Test Cases

#1\
Enter an item: cheese\
cheese added\
Would you like to add another item or undo your last one? yes\
Enter an item: milk\
milk added\
Would you like to add another item or undo your last one? yes\
Enter an item: bread\
bread added\
Would you like to add another item or undo your last one? no\
Here is your list:\
cheese\
milk\
bread

#2\
Enter an item: chips\
chips added\
Would you like to add another item or undo your last one? yes\
Enter an item: apples\
apples added\
Would you like to add another item or undo your last one? yes\
Enter an item: pasta\
pasta added\
Would you like to add another item or undo your last one? undo\
pasta was removed\
Enter an item: cake mix\
cake mix added\
Would you like to add another item or undo your last one? no\
Here is your list:\
chips\
apples\
cake mix


Here is a sample [Solution](stack-solution.py) code.

