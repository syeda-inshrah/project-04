import random

def main():
  secret_number = random.randint(1 , 99)
  print("i guess number between 1 to 99 ...")

  guess = int(input("guess the number:"))
  while guess != secret_number:
     if guess < secret_number:
       print("you guess is too low")
    
     else:
       print("you guess is too high")
    
     print()
     guess = input("guess the number:")

  print("congrats! you got it")

main()