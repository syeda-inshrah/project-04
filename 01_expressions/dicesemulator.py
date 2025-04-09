

num_sides = 6
def dice_roll():
     """
    Simulates rolling two dice and prints their total
    """
     die1= int(input("enter a dice num (1-6)"))
     die2 = int(input("enter a dice num (1-6)"))
     total: int = die1 + die2
     print("total of two dice is ", total)
     return total
def main():
     die1:int = 12
     print(f"die1 in main() start as : {die1}")
     die1 =  dice_roll()
     die1 =  dice_roll()
     die1 =  dice_roll()
     print(f"dice in main() as: {die1}")
main()