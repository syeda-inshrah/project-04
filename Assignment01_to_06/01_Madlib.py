import random

def main():
    print("Welcome to our story creator")
    print("-"* 60)
    name = input("what is your name?")
    something = input("name something you once dislike:")
    negative_feelings = input("how did it feel:")
    object = input("mention an object that intrigued you :")
    content = input("what was inside it:")
    lesson_learned = input("A life lesson in a few words:")
    challenge = input("another word for a challenge:")
    positive_outcome = input("A word for a positive change:")

    sentence = [
      "from that day on,every challenge is felt like a puzzle waiting to be solved "
      "She realized that every obstacle was just a stepping stone to something greater.",
      "That moment taught her that change, no matter how small, can lead to big results.",
      "What once seemed impossible became just another chapter in her journey.",
      "Through her struggles, she discovered the strength she never knew she had."
     ]
    random_sentence = random.choice(sentence)

    story = f"""Aisha always thought {something} was {negative_feelings} until she found {object} filled with {content}. 
That day, she realized {lesson_learned} and from then on, every {challenge} became {positive_outcome}.
"""
    {random_sentence}
    print("\""* 60)
    print("your story")
    print("-"*60)
    print(story)
    print("-"*60)
main()