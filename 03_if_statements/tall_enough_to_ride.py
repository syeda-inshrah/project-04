minimum_height = int(50)

def main():
    height = float(input("enter your height:"))

    if height >= minimum_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride!")

main()