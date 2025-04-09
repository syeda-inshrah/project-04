AFFIRMATION : list = [ "I am capable of doing anything I put my mind to." ,
                     "I am strong and resilient.",
    "I am confident in my abilities."]

def main():
    print(f"please print the affirmative:{AFFIRMATION}")
    print("\n" .join(AFFIRMATION))

    user_feedback = input().strip()
    while user_feedback.lower() not in [affirmation.lower() for affirmation in AFFIRMATION]:
        print(f"Oops! That's not quite right. Please try again with one of the affirmations.")
        print(f"Sorry, that's not the affirmative. Please try again.")
        user_feedback = input().strip()
    print("thats right")

main()