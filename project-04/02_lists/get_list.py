def main():
    values = []

    value = input("enter a value :(leave blank for print)")
    while value:
       values.append(value)
       value = input("enter a value :")

    print("List of values:", values)


if __name__ == "__main__":
    main()