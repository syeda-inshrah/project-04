inches_in_foot: int = 12

def main():
    try:
      feet : float = float(input("Enter a num or feet: "))
      inches:float = feet * inches_in_foot
      print("that is", inches , "inches")
    except ValueError:
       print("Invalid input. Please enter a valid number.")  
main()