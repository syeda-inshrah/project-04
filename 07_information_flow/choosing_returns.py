ADULT_AGE : int = 18

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age = int(input("enter your age:"))
    print(is_adult(age))

main()