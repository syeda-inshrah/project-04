import random
def play_game():
    print("Welcome to our numbe guessing game:")

    print("i have choosen to num between 1-100 \n")
    secret_num = random.randint(1 , 100)
    attemps = 0

    while True:
        try:
            user_guess= int(input("enter your guess:"))
            attemps += 1 
            if user_guess < 1 or user_guess > 100:
                print("invalid number")
            elif user_guess > secret_num:
                print("Too high! try a lower number:")
            elif user_guess < secret_num:
                print("Too low! try a higher number:")
            else:
                print(f"congrats! you guess is {secret_num}")
                print(f"Your guess is correct! You got it in {attemps} attempts!")
        except ValueError:
            print("enter a valid number")

play_game()