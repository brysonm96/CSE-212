class Stack:
    def __init__(self):
        self.data = []

    # empty() function
    def is_empty(self):
        return len(self.data) == 0

    # pop() function
    def remove(self):
        return self.data.pop()

    # push() function
    def add(self, item):
        self.data.append(item)

my_list = []
stack = Stack()

while True:

    # Ask user to enter an item
    item = input("Enter an item to add to the list: ")
    my_list.append(item)
    stack.add(item)
    print(f"You added {item} to the list.")

    # Option to add or undo item
    print("Would you like to add another item or undo your last item?")
    choice = input("(y = Yes | n = No | u = Undo): ")
    if choice.lower() == "n":
        break

    elif choice.lower() == "u":
        if not stack.is_empty():
            last_item = stack.remove()
            my_list.remove(last_item)
            print(f"Removed {last_item} from the list.")
        else:
            print("No item to undo.")

# Print list to user
print("Your list:")
for item in my_list:
    print(item)
