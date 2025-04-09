def add_three_copies(lst , data):
      for i in range (3):
        lst.append(data)

message = input("enter an integer message to copy:")
my_list = []

print("list before", my_list)
add_three_copies(my_list , message)
print("list after", my_list)





