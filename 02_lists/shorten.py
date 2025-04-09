max_length = 3

def shorten(lst):
    while len(lst) > max_length:
        last_elem = lst.pop()
        print(f"removed:{last_elem}")

def get_list():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """

    lst = []
    element = input("Please enter an element of the list or press enter to stop.")
    while element != "":
        lst.append(element)
        element = input("Please enter another element of the list or press enter to stop.")
    return lst

def main():
    lst = get_list()
    shorten(lst)
    print(f"Final list: {lst}")

if __name__ == "__main__":
    main()