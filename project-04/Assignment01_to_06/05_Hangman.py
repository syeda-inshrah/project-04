import random

def hangman():
 print("🎉 Welcome to Fruit Hangman Game! 🎉")
 print("Guess letters for the secret fruit!")


words = (["apple", "banana","cherry", "grape", "mango", "orange"])

word = random.choice(words)

guessed = ["_"] * len(word)

attempts = 6

guessed_letters = []

while attempts > 0 and "_" in guessed:
    print("\nWord: " + " ". join(guessed))

    guess = input("Please guess a letter: "). lower()

    if not guess. isalpha() or len(guess) != 1:

      print(" ❌ Enter a single valid letter ")

      continue

    if guess in guessed_letters:

       print("🔁You guessed that letter already.")
       continue
    guessed_letters. append(guess)

    if guess in word:
      print("✅ Correct guess!")
      for i in range(len(word)):
        if word[i] == guess:
          guessed[i] = guess
        else:
          print("❌ Wrong guess.")
          attempts -= 1
          if "_" not in guessed:
            print(f"\n🎊 Congratulations! You guessed the word: {word.upper()} 🎉")
          else:
            print(f"\n😢 You lost! The word was: {word.upper()}")