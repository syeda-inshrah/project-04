import random
def main():
    print("Welcome to the ultimate rock ,  paper , scissor game🎮")
    print("you vs. the mighty computer. lets see who will win: ")
    while True:
        user = input("choose your weapon (rock , paper , scissor)").lower()
        if user  not in ["rock" ,  "paper" , "scissor"]:
            print("invalid choice")
            continue
        com_choice = random.choice(["rock" ,  "paper" , "scissor"])
        print(f"🧍your selected {user}")
        print(f"🤖computer selected {com_choice}")
        if user == com_choice:
            print(" ⚖️ its a tie")
        elif (
             (user == 'rock' and com_choice == 'scissor')or
             (user == 'rpaper' and com_choice == 'rock')or
             (user == 'scissor' and com_choice == 'paper')
                ):
            print("ypu win:")
        else:
            print("computer wins , try again")
        play_again = input("you want to play again(yes/no) ").lower()
        if play_again != "yes":
            print("alright!, thanks for playing")
            print("see you again")
            break
main()