def main():
    try:
        prompt = (input("what is your fav animal?"))
        if not prompt.isalpha():
           raise ValueError (" Invalid input. Please enter a valid string.")
        
        print (f"My fav animal is also {prompt}")

    except ValueError as e:
        print(e)
main()