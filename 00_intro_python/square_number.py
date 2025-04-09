def main():
    try:
       num = int(input("type a num to see its square"))
       print(f" the square of this num is {num ** 2}")
    except ValueError:
        print("Invalid input. Please enter a number.")
main()