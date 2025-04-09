import random

num_sides = 6

def main():
    die1 = random.randint(1 , num_sides)
    die2 = random.randint(1 , num_sides)
    total = die1 + die2

    print("Each dice have", num_sides,"sides")
    print("die1 shows", die1)
    print("die2 shows", die2)
    print("total of two dice", total)

if __name__ == "__main__":
    main()