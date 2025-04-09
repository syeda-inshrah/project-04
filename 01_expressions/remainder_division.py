def main():
    dividend : int = int(input("Enter an integer value to be deviden")) 
    divisor : int = int(input("Enter an integer value to divide by"))

    quotient: int = dividend // divisor
    reminder : int = dividend % divisor

    print(f"the result of this division is {quotient} with {reminder}")

if __name__ == "__main__":
    main()