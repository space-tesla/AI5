#Q.1) Write a Python program to implement List operations (any 5 operations)


# Define a list
my_list = [10, 20, 30, 40, 50]

# Append an element to the list
my_list.append(60)
print("After appending 60:", my_list)

# Insert an element at a specific index
my_list.insert(2, 25)
print("After inserting 25 at index 2:", my_list)

# Remove an element from the list
my_list.remove(40)
print("After removing 40:", my_list)

# Pop an element from the list
popped_element = my_list.pop()
print("After popping an element:", my_list)
print("Popped element:", popped_element)

# Reverse the list
my_list.reverse()
print("After reversing the list:", my_list)


Output:
After appending 60: [10, 20, 30, 40, 50, 60]
After inserting 25 at index 2: [10, 20, 25, 30, 40, 50, 60]
After removing 40: [10, 20, 25, 30, 50, 60]
After popping an element: [10, 20, 25, 30, 50]
Popped element: 60
After reversing the list: [50, 30, 25, 20, 10]