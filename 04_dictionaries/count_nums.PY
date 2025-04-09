counts = {}

while True:
    num = (input("Enter a Num:"))
    if num == "":
        break
    elif num in counts :
        counts[num]  += 1
    else:
        counts[num] = 1

for num , count in counts.items():
    print(f"{num} appear {counts} time")