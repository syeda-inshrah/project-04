def add_many_numbers(numbers):
    """
    Add many numbers together.
    """
    total = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            raise ValueError("All elements in the list must be numbers.")
    return total

list_of_num = [1, 2, 3, 4, 5]
result = add_many_numbers(list_of_num)
print(f"the total is {result}")