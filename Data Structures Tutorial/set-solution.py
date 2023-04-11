#create set
names = set()

#set length
SET_MAX = 5

#user prompt
while True:
    print("\nNames:", names)
    print("Add a name (1)")
    print("Remove a name (2)")
    print("Exit (3)")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        name = input("Enter the name to add: ")

        #check to see if name exists
        if name in names:
            print("This name exists already")
            continue

        #check if set is full
        if len(names) >= SET_MAX:
            response = input("The set is full, would you like to increase the set size? (y/n): ")
            if response.lower() == "y":
                SET_MAX += 1
                print("Set size increased to", SET_MAX)
            else:
                print("Exiting...")
                break

        #add the name to the set
        names.add(name)
        print("Name added")

    elif choice == "2":
        name = input("Enter a name to remove: ")

        #check to see if name exists
        if name not in names:
            print("This name doesn't exist")
            continue

        #remove the name
        names.remove(name)
        print("Name removed")

    elif choice == "3":
        print("End")
        break

    else:
        print("Invalid choice, please try again")

print("Set of names:", names)
