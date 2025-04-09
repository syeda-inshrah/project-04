import random
import string
def pasword_genrator(lenght):
    if lenght < 4 :
        return "pasword should be at least 4 character long"
    characters = string.ascii_letters + string.digits + string.punctuation
    pasword = ''.join(random.choice(characters) for i in range(lenght))
    return pasword

def main():
    print("🔐 Welcome to the Secure Password Generator 🔐")
    try:
        lenght = int(input("enter the lenght of the pasword:"))
        pasword = pasword_genrator(lenght)
        print(f"\n🧾 Your generated password is:\n👉 {pasword}")
    except ValueError:
        print("plz enter a valid number of lenght")

main()