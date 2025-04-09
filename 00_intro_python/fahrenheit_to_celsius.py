def main():
    try:
        fahrenheit = int(input("enter the num of fahrenheit"))
        celsius = (fahrenheit - 32) * 5/9 / 9.0
        print(f"temperatur {fahrenheit}F = {celsius}C")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
main()