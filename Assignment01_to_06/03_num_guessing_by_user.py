def main():
    print("Welcome to the number guessing game!")
    print("Think of a number between 1 and 100 (but don't tell me).")
    print("I'll try to guess it!")

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed it in {attempts} attempts.")
            break
        else:
            print("Please enter H, L, or C.")

main()
