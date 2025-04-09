def main():
    name = str(input("enter your name"))
    print (greet(name))

def greet(name):
    return f"Greeting {name}"
main()