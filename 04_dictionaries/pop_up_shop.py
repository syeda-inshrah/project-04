fruit_prices ={"apple" :31 ,  "banana":32 , "orange":33, "kiwi":34 , "durian":35}

total_cost = 0
for fruits, price in fruit_prices.items():
    quantity = input(f"how many {fruit_prices} you want to buy")

    if quantity.isdigit():
       quantity = int(quantity)
       total_cost += price * quantity 
       print(f"your total cost is {total_cost}")
    else:
      print("Invalid quantity. Please enter a number.")