phone_book = {}

while True:
    name = input("enter a name:")
    if name == "":
        break
    number = input("enter a number:")
    phone_book[name] = number

for name in phone_book:
    print(f"{name}: {phone_book[name]}")

name_to_lookup = input ("Enter name to lookup:")
if name_to_lookup in phone_book:
    print(f"{name_to_lookup}'s number is: {phone_book[name_to_lookup]}")
else:
    print(f"{name_to_lookup} not found in the phone book.")