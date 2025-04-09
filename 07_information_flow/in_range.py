def is_in_range(n , low , high):
    if low <= n <= high:
        return True
    return False

def main():
  print("Test 1:", is_in_range(5, 1, 10))  
  print("Test 2:", is_in_range(15, 1, 10))

main()