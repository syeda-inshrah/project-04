
def get_last_element(lst):
    print("last element in this list is start with :", lst[-1])

while True:
    try:
        num_element = int(input("How many words you want to add in your list"))
        break
    except ValueError:
        print("Please enter a number:")

my_list =[]

for i in range(num_element):
    word = input("enter your words")
    my_list.append(word)

get_last_element(my_list)