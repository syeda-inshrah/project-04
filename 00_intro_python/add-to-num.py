def main():
    try:
        num1 = int(input("enter your 1st number"))
        num2 = int(input("enter your 2nd number"))
        total = num1 + num2
        print(f"your answer is {num1} + {num2} = {total}")
    except ValueError:
        print("Invalid ! please enter a valid integer")
main()