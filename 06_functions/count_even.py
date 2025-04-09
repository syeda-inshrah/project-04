def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
            print(count)

def get_lists_of_inits():
    lst = []
    user = input("enter an integer or press enter to stop:")
    while user != "":
        lst.append(int(user))
        user= input("enter an integer or press enter to stop:")
    return lst

def main():
    lst = get_lists_of_inits()
    count_even(lst)

main()