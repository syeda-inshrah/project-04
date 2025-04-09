def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today, it makes me want to {word}.")
    elif part_of_speech == 2:
        print(f"Part of speech must be 0 (noun), 1 (verb), or 2 (adjective)! Can't make a sentence.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    print("Is this word a noun, verb, or adjective?")
    
    while True:
        user_input = input("Type 0 for noun, 1 for verb, 2 for adjective: ")
        
        if user_input.isdigit():
            part_of_speech = int(user_input)
            if part_of_speech in [0, 1, 2]:  # Only valid values are 0, 1, or 2
                make_sentence(word, part_of_speech)  # Correct function call
                break  # Exit loop after valid input
            else:
                print("❌ Please enter only 0 (noun), 1 (verb), or 2 (adjective). Try again.")
        else:
            print("❌ Invalid input! Please enter a number (0, 1, or 2).")


main()
