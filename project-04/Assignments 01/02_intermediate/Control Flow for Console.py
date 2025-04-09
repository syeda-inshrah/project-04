import random

for i in range(5):
     user_num = int(input("enter a num between 1 and 100:"))
     computer_num = random.randint(1 , 100)
     print(f"your num is:{user_num}")
     print(f"computers num is : ???")

     user = input("Is your num higyher or lower than computers num?(higher / lower):").strip().lower()
     if user_num > computer_num and user == "higher":
          print("you are right!")
     elif user_num < computer_num and user == "lower":
          print("you are right!")
     else:
          print("invalid answer!")
     print(f"computers num was: {computer_num}!")