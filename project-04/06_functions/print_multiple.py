def main():
    message = input("Enter your num:")
    repeat = int(input("enter a num of time you want to repeat message"))

    for i in range(repeat):
       print(message , end= " ")

main()