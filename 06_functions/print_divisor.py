def print_divisor(num:int):
    print(f"here are divisor of {num}")
    for i in range(1 ,num+1):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("enter a num:"))
    print_divisor(num)

main()