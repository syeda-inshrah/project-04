def double(num : int):
    return num * 2

def main():
    num = int(input("enter a num:"))
    num_times_2 = double(num)
    print(f"double that is{num_times_2}")

main()