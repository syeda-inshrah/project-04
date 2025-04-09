# Sample list with different elements
sample_list = [10, "apple", 3.14, "banana", 42]

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

# Function to modify an element at a specific index
def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range"

# Function to slice the list
def slice_list(lst, start_index, end_index):
    try:
        return lst[start_index:end_index]
    except IndexError:
        return "Index out of range"

# Game interaction - prompting the user for operations
def game():
    print("Welcome to the List Operation Game!")
    print("Select an operation:")
    print("1. Access Element")
    print("2. Modify Element")
    print("3. Slice List")

    # Get the operation choice from the user
    operation = input("Enter the number corresponding to the operation: ")

    # Execute the operation based on the user's choice
    if operation == "1":
        # Access an element
        index = int(input("Enter the index to access: "))
        result = access_element(sample_list, index)
        print(f"Accessed element: {result}")
        
    elif operation == "2":
        # Modify an element
        index = int(input("Enter the index to modify: "))
        new_value = input("Enter the new value: ")
        result = modify_element(sample_list, index, new_value)
        print(f"Updated list: {result}")
        
    elif operation == "3":
        # Slice the list
        start_index = int(input("Enter the start index: "))
        end_index = int(input("Enter the end index: "))
        result = slice_list(sample_list, start_index, end_index)
        print(f"Sliced list: {result}")
        
    else:
        print("Invalid operation. Please try again.")

# Call the game function
game()
