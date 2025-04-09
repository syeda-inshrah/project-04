def print_one_digits(num):
    one_digits = num % 2
    print(f"the one digit is {one_digits}")

def main():
    while True:
     num = int(input("enter your number:"))
     print_one_digits(num)

     continue_input = input("do you want more number(yes/no)").lower()
     if continue_input != "yes":
        break
     else:
        print("error")
main()